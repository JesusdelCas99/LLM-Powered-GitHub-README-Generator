# LLM powered README generator for GitHub
This repository provides a powerful script tailored for effortlessly generating READMEs for GitHub repositories. Leveraging the capabilities of Ollama language models, it combines the content of all files within a specified GitHub repository, excluding certain files and folders, and generates a README.md file based on a provided prompt template.


## Setup and Configuration <!-- -->

Project setup and configuration:

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


## Usage

Run `main.py` script to generate README file based on `config.file` configuration. This application automatically saves repository content, files list, and README file as text files to the `/data/` and `/output` directories, respectively:

```
python ./main.py
```

## Files

Project files and folder structure:

- `/data`: Contains text files storing repository file list and content.
- `/output`: Stores the generated README file as a text file.
- `main.py`: Main Python script responsible for README generation.
- `src/infoToken.py`: Python module for checking GitHub rate limits and calculating time until reset.
- `src/testConfig.py`: Python module for verifying GitHub tokens, checking repository existence, and Ollama model availability.

## Acknowledgments

This project utilizes the following libraries and tools:

- `langchain` for generating text using language models.
- `langchain_community` for community-contributed language models.
- `requests` for making HTTP requests.
- `configparser` for reading configuration files.
- `base64` for decoding file content.
- `os` and `sys` for system-related operations.
- `subprocess` for executing shell commands.

For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!
