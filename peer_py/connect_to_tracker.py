import requests
from .logger import console_logger


def send_request(url, payload):
    try:
        response = requests.post(url, json=payload)
    except requests.exceptions.RequestException as e:
        console_logger.error(f"Error: {e}")
        return None
    return response.json()
