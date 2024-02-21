import requests, subprocess, os



# Set PYTHONDONTWRITEBYTECODE to prevent generation of __pycache__ directories
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'


# Verify GitHub token
def is_valid_token(token):
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False



def repo_exists(repository):
    response = requests.get(f'https://api.github.com/repos/{repository}')
    if response.status_code == 200:
        return True
    else:
        return False



def model_exists(model):
    try:
        output = subprocess.check_output(["ollama", "list"], text=True)
        if model in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False