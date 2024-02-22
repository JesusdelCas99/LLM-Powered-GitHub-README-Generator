# AI-Powered-README-Generator
 Craft Compelling READMEs: AI-Powered README Generator (Ollama LLM Platform)


## Setup and Configuration <!-- -->

1. **Install Ollama**

   Visit the official [Ollama website](https://ollama.com/download) and follow the instructions to download and install Ollama for your operating system. After installing Ollama, use the following command to download the model of your choice:

     ```
     ollama pull <model>
     ```

     Replace `<model>` with the name of the Ollama model you want to use from the [Ollama model library](https://ollama.com/library).
   
2. **Install project dependencies**

   Install the required dependencies using either `requirements.txt` or `environment.yml`:

   - Using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

   - Using `environment.yml`:
     ```
     conda env create -f environment.yml
     conda activate readmeEnv
     ```
     
3. **Generate Personal Access Token**

    Generate Personal Access Token (PAT) with the required permissions (`contents:read`) based on your GitHub repository and update `config.cfg` file with your access token.

4. **Configuration**

   Customize `config.cfg` file according to your requirements. Specify the GitHub repository, access token, model, excluded files, excluded folders, and other parameters.

   In the `config.cfg` file, you can specify the following parameters:
   
   - `access_token`: Your GitHub personal access token.
   - `repository`: The GitHub repository in the format 'username/repository'.
   - `model`: The Ollama model to use for generating README content.
   - `files`: A comma-separated list of filenames to exclude from combination.
   - `folders`: A comma-separated list of folder names to exclude from combination.
   - `prompt_template`: The template for the prompt to be used for generating README content. Ensure it contains `{data}` to represent the repository content.


### Acknowledgments

This project utilizes the following libraries and tools:

- `langchain` for generating text using language models.
- `langchain_community` for community-contributed language models.
- `requests` for making HTTP requests.
- `configparser` for reading configuration files.
- `base64` for decoding file content.
- `os` and `sys` for system-related operations.
- `subprocess` for executing shell commands.

For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!
