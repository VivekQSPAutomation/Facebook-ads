import os
from  datetime import datetime as dt
import datetime
import secrets
import string
import pandas as pd
import requests
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

from Config.config import TestData


class Static_ads:

    def __init__(self):
        # Read the CSV file
        df = pd.read_csv(f'{os.getcwd()}/fb_token.csv')
        access_token = df['Token'].iloc[0]
        created_date_str = df['created_date'].iloc[0]
        print(access_token, created_date_str)
        created_date = dt.strptime(created_date_str, '%Y-%m-%d')
        today = dt.now()
        days_diff = (today - created_date).days
        print(days_diff)

        if days_diff < 58:
            FacebookAdsApi.init(access_token=access_token)
        else:
            exchange_url = "https://graph.facebook.com/v18.0/oauth/access_token"
            params = {
                "grant_type": "fb_exchange_token",
                "client_id": "1027726831906205",
                "client_secret": "cfbcca04aa930c2b26d4926495a62d09",
                "fb_exchange_token": access_token
            }
            response = requests.get(exchange_url, params=params)
            new_access_token = response.json()["access_token"]
            print("New Access Token:", new_access_token)
            df['Token'].iloc[0] = new_access_token
            df['created_date'].iloc[0] = today.strftime('%Y-%m-%d')
            df.to_csv(f'{os.getcwd()}/fb_token.csv', index=False)
            FacebookAdsApi.init(access_token=new_access_token)


    def create_campaignandadset(self, brandname):
        params = {
            "name": f"{brandname}-campaign",
            "objective": "OUTCOME_AWARENESS",
            "status": "PAUSED",
            "special_ad_categories": ["NONE"],
            "lifetime_budget": 8400,
        }

        campaign_result = AdAccount(TestData.ad_account_id).create_campaign(params=params)
        print(campaign_result)

        today = datetime.datetime.today()
        start_time = str(today)
        end_time = str(today + datetime.timedelta(weeks=1))

        adset = AdSet(parent_id=TestData.ad_account_id)
        adset.update(
            {
                "name": f"{brandname}-Adset",
                "campaign_id": campaign_result["id"],
                "bid_amount": 100,
                "billing_event": "IMPRESSIONS",
                "optimization_goal": "REACH",
                "targeting": {
                    "geo_locations": {"countries": ["US"]},
                    "publisher_platforms": ["facebook", "instagram"],
                    'facebook_positions': ['feed', 'facebook_reels', 'story', 'marketplace', 'video_feeds'],
                    'instagram_positions': ['story', 'stream', 'explore', 'reels'],
                },
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        adset.remote_create(params={"status": "PAUSED"})
        return adset['id']

    def create_Ads(self, adset, brandname, image_url):
        params = {
            "name": f"{brandname}-ads",
            "object_story_spec": {
                "page_id": TestData.page_id,
                "link_data": {
                    "picture": image_url,
                    "link": "https://google.com",
                    "message": "Testing Message",
                    "call_to_action": {
                        "type": "LEARN_MORE",
                        "value": {
                            "link": "https://google.com",
                        },
                    },
                    "name": "Click here to View",
                    "description": "Testing ADs With Script",
                },
                "instagram_actor_id": TestData.instagram_account_id,
            },
            "degrees_of_freedom_spec": {
                "creative_features_spec": {
                    "standard_enhancements": {"enroll_status": "OPT_OUT"}
                }
            },
        }

        adcreative = AdAccount(TestData.ad_account_id).create_ad_creative(params=params)
        print(adcreative)
        params = {
            "name": f'{brandname}{"".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))}',
            "adset_id": adset,
            "creative": {"creative_id": adcreative["id"]},
            "status": "PAUSED",
        }

        AdAccount(TestData.ad_account_id).create_ad(params=params)

        preview = self.preview_ads(adcreative=adcreative['id'])
        return preview

    def preview_ads(self, adcreative):
        ad_format = 'DESKTOP_FEED_STANDARD'
        api_endpoint = f'https://graph.facebook.com/v18.0/{adcreative}/previews'
        api_params = {
            'ad_format': ad_format,
            'access_token': TestData.access_token,
        }
        response = requests.get(api_endpoint, params=api_params)
        data = response.json()
        preview_url = data.get('data', [{}])[0].get('body')

        return preview_url

#
if __name__ == '__main__':
    static = Static_ads()
    ad_set = static.create_campaignandadset(brandname="")
    static.create_Ads(ad_set, brandname="", image_url="")
