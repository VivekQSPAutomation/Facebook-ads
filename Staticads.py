import datetime
import os
import secrets
import string
import warnings

import requests
from facebook_business.adobjects import ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

from Config import App_data
from preview import preview_ads


class Static_ads:

    def __init__(self):
        FacebookAdsApi.init(access_token=App_data.access_token)

    def create_campaignandadset(self):
        params = {
            "name": "Facebooak-and-Instgram-campaign",
            "objective": "OUTCOME_AWARENESS",
            "status": "PAUSED",
            "special_ad_categories": ["NONE"],
            "lifetime_budget": 8400,
        }

        campaign_result = AdAccount(App_data.ad_account_id).create_campaign(params=params)
        print(campaign_result)

        today = datetime.date.today()
        start_time = str(today)
        end_time = str(today + datetime.timedelta(weeks=1))

        adset = AdSet(parent_id=App_data.ad_account_id)
        adset.update(
            {
                "name": "FacebookandInsta-Adset",
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

    def create_Ads(self, adset):
        image = AdImage(parent_id=App_data.ad_account_id)
        image[AdImage.Field.filename] = f"{os.getcwd()}/check.jpg"
        image.remote_create()

        image_hash = image[AdImage.Field.hash]
        print(image)

        params = {
            "name": "Facebook-and-Insta-ads",
            "object_story_spec": {
                "page_id": App_data.page_id,
                "link_data": {
                    "image_hash": image_hash,
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
                "instagram_actor_id": App_data.instagram_account_id,
            },
            "degrees_of_freedom_spec": {
                "creative_features_spec": {
                    "standard_enhancements": {"enroll_status": "OPT_OUT"}
                }
            },
        }

        adcreative = AdAccount(App_data.ad_account_id).create_ad_creative(params=params)
        print(adcreative)

        params = {
            "name": f'testing_static_ads{"".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))}',
            "adset_id": adset,
            "creative": {"creative_id": adcreative["id"]},
            "status": "PAUSED",
        }

        print(AdAccount(App_data.ad_account_id).create_ad(params=params))

        preview = preview_ads(adcreative= adcreative['id'])
        print(preview)


if __name__ == '__main__':
    static = Static_ads()
    warnings.filterwarnings("ignore")
    ad_set = static.create_campaignandadset()
    static.create_Ads(ad_set)
