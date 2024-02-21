import requests
from datetime import datetime, timezone


def check_rate_limit(access_token):
    """
    Checks the rate limit of GitHub API usage for the provided access token.

    Parameters:
        access_token (str): Personal Access Token for GitHub API authentication.

    Returns:
        dict: A dictionary containing rate limit information.
    """
    url = "https://api.github.com/rate_limit"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to check rate limit: {response.status_code}")
        return None


def time_until_reset(reset_time):
    """
    Calculates the time until the rate limit reset time.

    Parameters:
        reset_time (int): Unix timestamp indicating the time when rate limit resets.

    Returns:
        tuple: A tuple containing the number of hours and minutes until reset time.
    """
    current_time = datetime.now(timezone.utc).timestamp()
    time_until_reset_seconds = reset_time - current_time
    hours = int(time_until_reset_seconds // 3600)
    minutes = int((time_until_reset_seconds % 3600) // 60)
    return hours, minutes