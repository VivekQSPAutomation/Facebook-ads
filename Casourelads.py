import datetime
import os

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.advideo import AdVideo
from facebook_business.api import FacebookAdsApi

from Config import App_data


class Carosuel_creation:

    def __init__(self):
        FacebookAdsApi.init(access_token=App_data.access_token)

    def creation_campaginandAdset(self):
        params = {
            "name": "Facebook-and-Instagram-campaign-Carousel",
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
                "name": "FacebookandInsta-Adset-Carousel",
                "campaign_id": campaign_result["id"],
                "bid_amount": 100,
                "billing_event": "IMPRESSIONS",
                "optimization_goal": "REACH",
                "targeting": {
                    "geo_locations": {"countries": ["US"]},
                    "publisher_platforms": ["facebook", "instagram"],
                    "facebook_positions": ["story",'feed','facebook_reels', 'video_feeds','marketplace'],
                    "instagram_positions": ["story", 'reels'],
                },
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        adset.remote_create(params={"status": "PAUSED"})

        return adset['id']

    def creative_ads(self, adset):
        creative = AdCreative(parent_id=App_data.ad_account_id)
        video = AdVideo(parent_id=App_data.ad_account_id)
        video[AdVideo.Field.filepath] = f"{os.getcwd()}/blank.mp4"
        video.remote_create()
        video_id = video[AdVideo.Field.id]
        carousel_data = [
            {
                "link": "https://google.com",
                "name": "First Image",
                "description": "First image Description",
                "picture": "https://free-images.com/lg/672a/pennsylvania_landscape_scenic_97427.jpg",
            },
            {
                "link": "https://google.com",
                "name": "Second image",
                "description": "Second image Description",
                "picture": "https://free-images.com/lg/672a/pennsylvania_landscape_scenic_97427.jpg",
            },
            {
                "link": "https://google.com",
                "name": "First Video",
                "description": "First video Description",
                "video_id": video_id,
                "picture": "https://free-images.com/lg/672a/pennsylvania_landscape_scenic_97427.jpg",
                "video_type": "video"
            },
            {
                "link": "https://google.com",
                "name": "Second Video",
                "description": "Second video Description",
                "video_id": video_id,
                "picture": "https://free-images.com/lg/672a/pennsylvania_landscape_scenic_97427.jpg",
                "video_type": "video"
            },
        ]

        params = {
            "name": "Facebook-and-Insta-ads",
            "object_story_spec": {
                "page_id": App_data.page_id,
                "link_data": {
                    "child_attachments": carousel_data,
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

        ad = Ad(parent_id=App_data.ad_account_id)
        params = {
            "name": "Carousel Ad",
            "adset_id": adset,
            "creative": {
                "creative_id": adcreative["id"]
            },
            "status": "PAUSED"
        }
        ad.remote_create(params=params)


if __name__ == '__main__':
    carousel_creator = Carosuel_creation()
    ad_set = carousel_creator.creation_campaginandAdset()
    carousel_creator.creative_ads(ad_set)
