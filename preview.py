import requests

from Config import App_data


def preview_ads(adcreative):
    ad_format = 'DESKTOP_FEED_STANDARD'
    api_endpoint = f'https://graph.facebook.com/v18.0/{adcreative}/previews'
    api_params = {
        'ad_format': ad_format,
        'access_token': App_data.access_token,
    }

    response = requests.get(api_endpoint, params=api_params)
    data = response.json()
    preview_url = data.get('data', [{}])[0].get('body')

    return preview_url
