import requests
import os
import sys
import string
import random
from time import sleep


def random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(32))


def main():

    secret = os.environ['CHECK_API_SECRET']

    post_url = 'https://europe-west1-checkson-cadf1.cloudfunctions.net/checkpubsub'
    get_url = 'https://api.checkson.io/api/pubsub-check'

    identifier = random_string()

    post_response = requests.post(post_url, json={'identifier': identifier}, headers={'Authorization': f'Bearer {secret}'})
    post_response.raise_for_status()

    sleep(3)

    get_response = requests.get(get_url)
    get_response.raise_for_status()

    response_identifier = get_response.text

    if response_identifier != identifier:
        print(f'Returned identifier {response_identifier} does not match sent identifier {identifier}')
        sys.exit(1)

    print(f'Requested identifier {identifier} and received identifier {response_identifier} match')
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'There was an error: {e}')
        sys.exit(1)
