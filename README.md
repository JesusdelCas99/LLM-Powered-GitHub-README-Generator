# AI-Powered-README-Generator
 Craft Compelling READMEs: AI-Powered README Generator (Ollama LLM Platform)


### Setup

1. **Install Ollama**
 
    Visit the official Ollama website (https://ollama.com/download) and follow the instructions to download and install Ollama for your operating system. After installing Ollama, use the following command to download the model of your choice using the provided command, tailored to your preferences and requirements.

     ```
     ollama pull <model>
     ```

     Replace `<model>` with the name of the Ollama model you want to use from the Ollama model library (https://ollama.com/library) and update `config.cfg` file to include it.
   
3. **Install Dependencies**

   Install the required dependencies using either `requirements.txt` or `environment.yml`. Choose one of the following methods:

   - Using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

   - Using `environment.yml`:
     ```
     conda env create -f environment.yml
     conda activate readmeEnv
     ```
     
4. **Generate Personal Access Token**

    Generate Personal Access Token (PAT) with the required permissions (`contents:read`) based on your GitHub repository and update `config.cfg` file with your access token.

5. **Configuration**

    Customize `config.cfg` file according to your requirements. Specify the GitHub repository, access token, model (Ollama model), excluded files, excluded folders, and other parameters.

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
