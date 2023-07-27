import requests
import os
import sys


def main():

    url_to_check = os.environ['URL']
    category = os.environ.get('CATEGORY', 'performance')
    strategy = os.environ.get('STRATEGY', 'desktop')
    score_treshold = float(os.environ['SCORE_TRESHOLD'])

    if strategy not in ['mobile', 'desktop']:
        raise ValueError('STRATEGY must be "mobile" or "desktop"')

    if category not in ['ACCESSIBILITY', 'best-practices', 'performance', 'pwa', 'seo']:
        raise ValueError('CATEGORY must be "accessibility", "best-practices", "performance", "pwa", or "seo"')

    if score_treshold < 0 or score_treshold > 1:
        raise ValueError('SCORE_TRESHOLD must be between 0 and 1')

    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    url = f'{base_url}?url={url_to_check}&strategy={strategy}&category={category}'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    score = float(data['lighthouseResult']['categories'][category]['score'])

    if score < score_treshold:
        print(f'{category} score of {score} is below threshold of {score_treshold}')
        sys.exit(1)

    print(f'{category} score of {score} is above threshold of {score_treshold}, everything is fine')
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'There was an error: {e}')
        sys.exit(1)
