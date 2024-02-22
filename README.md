# AI-Powered-README-Generator
 Craft Compelling READMEs: AI-Powered README Generator (Ollama LLM Platform)


### Setup

1. **Install Dependencies**

   You can install the required dependencies using either `requirements.txt` or `environment.yml`. Choose one of the following methods:

   - Using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

   - Using `environment.yml`:
     ```
     conda env create -f environment.yml
     conda activate dapt
     ```
2. **Generate GitHub Personal Access Token based on GitHub repository**

Generate a personal access token on GitHub with the necessary permissions (`contents:read`) and update the `config.cfg` file with your access token.

3. **Customize `config.cfg file`**

Customize  `config.cfg` file according to your requirements. Be sure to provide the following parameters at least: `repository` (GitHub repository), `access_token` (Personal Access Token), `model` (Ollama model) and `prompt_template` (prompt template for LLM). Optionally, parameters such as `folders` (excluded folders) and `files` (excluded files) can be specified based on specific needs.

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
