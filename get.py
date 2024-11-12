import json
import os
import sys
import requests

def main():
    # Extract the tool's `url` argument from the env
    url = os.getenv('URL')
    if not url:
        raise ValueError('A URL must be provided')

    # Send the GET request and capture the response
    response = requests.get(url)

    # Return the response details by printing them to stdout
    print(json.dumps({
        'url': response.request.url,
        'method': response.request.method,
        'status_code': response.status_code,
        'content': response.text
    }))

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        # Print err to stdout to return the error to the assistant
        print(f"Error: {err}")
        sys.exit(1)
