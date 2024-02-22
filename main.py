from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
import requests, base64

from src.infoToken import *
from src.testConfig import *
import os, sys, configparser



def combine_files_content_recursive(repository, excluded_files, excluded_folders, access_token):
    """
    Recursively combines the content of all files within the specified repository,
    excluding files listed in the `excluded_files` parameter and folders listed in the `excluded_folders` parameter.

    Parameters:
        repository (str): The GitHub repository in the format 'username/repository'.
        excluded_files (list): A list of filenames to exclude from combination.
        excluded_folders (list): A list of folder names to exclude from combination.
        access_token (str): Personal Access Token for GitHub API authentication.

    Returns:
        str: A string containing the combined content of all non-excluded files.
    """
    combined_content = ""
    files = []

    # Get contents of the repository recursively
    url = f"https://api.github.com/repos/{repository}/git/trees/main?recursive=1"  # Assuming the main branch
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tree = response.json()["tree"]
        for item in tree:
            if item["type"] == "blob":
                file_path = item["path"]
                # Check if the file path or any parent folder is in the excluded_files list
                if not any(file_path.startswith(excluded_file.lower() + "/") for excluded_file in excluded_folders):
                    if file_path.lower() not in excluded_files:
                        # Download file content
                        file_content_response = requests.get(item["url"], headers=headers)
                        if file_content_response.status_code == 200:
                            files.append(file_path)
                            file_content = file_content_response.json()["content"]
                            # Decode base64 content
                            file_content = base64.b64decode(file_content).decode("utf-8")
                            # Append the content with a marker indicating a new file
                            combined_content += f'-- NEW FILE: {file_path}\n\n{file_content}\n\n\n'
    else:
        print(f"\033[91mError: Failed to retrieve repository content: {response.status_code}\033[0m")

    return combined_content, files



def save_content(data, files, output):
    """
    Save repository content, list of files, and output text to separate text files.
    
    Args:
        data (str): The repository content to be saved.
        files (str): The list of files to be saved.
        output_text (str): The output text to be saved.
    """
    # Save repository content to a text file
    file_path_content = os.path.join('./data', 'repository_content.txt')
    with open(file_path_content, 'w') as file:
        file.write(data)

    # Save list of files to another text file
    file_path_files = os.path.join('./data', 'repository_files_list.txt')
    with open(file_path_files, 'w') as file:
        file.write('\n'.join(files))

    # Save output text to file
    file_path_output = os.path.join('./output', 'output_readme.txt')
    with open(file_path_output, 'w') as file:
        file.write(output['text'])



if __name__ == "__main__":

    # Create a ConfigParser object and read the config.cfg file
    config = configparser.ConfigParser()
    config.read('config.cfg')

    # Access configuration values
    try:
        excluded_files = config['excluded']['files'].split(',')
        excluded_folders = config['excluded']['folders'].split(',')
    except:
        excluded_files = []
        excluded_folders = []


    # Check if access_token, repository, prompt_template and model are empty
    try:
        access_token = config['github']['access_token']
    except:
        print("\033[91mError: Please fill in your Personal Access Token in the config.py file.\033[0m")
        sys.exit()

    try:
        repository = config['github']['repository']
    except:
        print("\033[91mError: Please specify your GitHub repository in the config.py file.\033[0m")
        sys.exit()
    
    try:
        model = config['github']['model']
    except:
        print("\033[91mError: Please specify the Ollama model to use in the config.py file.\033[0m")
        sys.exit()

    try:
        template = config['prompt']['prompt_template']
    except:
        print("\033[91mError: Please specify prompt template.\033[0m")
        sys.exit()

   
    # Check if the provided access token is valid
    if not is_valid_token(access_token):
        print("\033[91mError: Access token not valid. Please generate a new one.\033[0m")
        sys.exit()
    
    # Check if the provided repository exists
    if not repo_exists(repository):
        print("\033[91mError: Repository name not valid. Try a new one\033[0m")
        sys.exit()

    # Check if the specified model exists
    if not model_exists(model):
        print("\033[91mError: Model name not valid or not installed.\033[0m")
        sys.exit()

    if not '{data}' in template:
        print("\033[91mError: Please specify a valid prompt template as found in the GitHub repository.\033[0m")
        sys.exit()


    print("\033[94mInfo: Reading repository content...\033[0m")

    # Combine the content of files in the repository
    data, files = combine_files_content_recursive(repository, excluded_files, excluded_folders, access_token)

    if len(files) > 0:
        print(f"Found {len(files)} files in repository...")
        for i in range(len(files)):
            print(files[i])

    else: 
         print(f"\033[91mError: No files were found in repository\033[0m")

    # Initialize LLM model
    llm = Ollama(base_url='http://localhost:11434', model=model)
    
    # Initialize LLMChain
    prompt = PromptTemplate(template = template, input_variables = ["data"])
    llm_chain = LLMChain(llm = llm, prompt = prompt)

    print("\033[94mInfo: Generating output README from GitHub repository...\033[0m")

    # Run LLMChain with data from the template
    output = llm_chain.invoke({"data": data})

    # Save content fo files
    save_content(data, files, output)

    print("\033[92mSuccess: README file successfully generated.\033[0m")
    print(f"Navigate to {os.path.abspath('output')} to view it.")

    # Verify token rate limit
    print("\033[94mInfo: Checking token rate limit...\033[0m")
    rate_limit_info = check_rate_limit(access_token)

    if rate_limit_info:
        remaining_requests = rate_limit_info["rate"]["remaining"]
        limit = rate_limit_info["rate"]["limit"]
        reset_time = rate_limit_info["rate"]["reset"]

        print(f"(GitHub API Info) Remaining requests: {remaining_requests}/{limit}")
        hours, minutes = time_until_reset(reset_time)
        print(f"(GitHub API Info) Time until reset: {hours} hours and {minutes} minutes")
    

    print("\033[94mInfo: Generated README...\033[0m")
    print(output['text'])