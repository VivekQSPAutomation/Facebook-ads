import datetime
import os

import requests
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.advideo import AdVideo
from facebook_business.api import FacebookAdsApi

from Config import App_data
from preview import preview_ads


class Story_creation:
    video_upload_url = "https://graph-video.facebook.com/v18.0/111068308711654/videos"
    page_access_token = "EABk16zooH64BO7XDM1BuI5goC9Q9VSxfTC5HvA0wEjQRuhsjAPmJOmzXlK7fO97U1w0xVJN5KMzqXTY5HBE9gtO6gemJZAYZAZA9OUPUTHhmdxj6ABdPa8WpDitbzJ7a8hkfQ6me2p7MTrGNLAImWUgDqeI8sXRYY0LOAIXh4tQTEbGhZCa6Xk17uDZBCQpTEfsaUzDcZD"
    video_file_path = f"{os.getcwd()}/blank.mp4"
    max_retries = 3


    def __init__(self):
        FacebookAdsApi.init(access_token=App_data.access_token)

    def upload_video_with_retry(self, url, token, video_path, retries):
        for _ in range(retries):
            try:
                response = requests.post(
                    url,
                    data={"access_token": token},
                    files={"source": open(video_path, "rb")},
                )

                if response.status_code == 200:
                    return response.json()
                else:
                    print(
                        f"Video upload failed with status code {response.status_code}"
                    )
                    print(f"Response content: {response.text}")
            except Exception as e:
                print(f"Error during video upload: {str(e)}")

            print("Retrying...")
        print("Max retries reached. Video upload failed.")

    def creation_campaign(self):
        params = {
            "name": "StoryAds-Facebooak-and-Instgram-campaign",
            "objective": "OUTCOME_AWARENESS",
            "status": "PAUSED",
            "special_ad_categories": ["NONE"],
            "lifetime_budget": 8400,
        }
        campaign_result = AdAccount(App_data.ad_account_id).create_campaign(params=params)
        print(campaign_result)
        return campaign_result

    def creation_adset(self, campaign_result):
        today = datetime.date.today()
        start_time = str(today)
        end_time = str(today + datetime.timedelta(weeks=1))

        adset = AdSet(parent_id=App_data.ad_account_id)
        adset.update(
            {
                "name": "StoryADs-FacebookandInsta-Adset",
                "campaign_id": campaign_result["id"],
                "bid_amount": 100,
                "billing_event": "IMPRESSIONS",
                "optimization_goal": "REACH",
                "targeting": {
                    "geo_locations": {"countries": ["US"]},
                    "publisher_platforms": ["facebook", "instagram"],
                    "facebook_positions": [ "story",'facebook_reels','video_feeds'],
                    "instagram_positions": ["story",'reels'],
                },
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        adset.remote_create(params={"status": "PAUSED"})
        print(adset)
        return adset['id']

    def creation_ad_creative(self, adset):
        video = AdVideo(parent_id=App_data.ad_account_id)
        video[AdVideo.Field.filepath] = f"{os.getcwd()}/output_file.mp4"
        video.remote_create()
        video_id = video[AdVideo.Field.id]

        params = {
            "name": "Story-Ad",
            "adset_id": adset,
            "creative": {
                "object_story_spec": {
                    "page_id": App_data.page_id,
                    "video_data": {
                        "call_to_action": {
                            "type": "LEARN_MORE",
                            "value": {"link": "https://google.com"},
                        },
                        "video_id": video_id,
                        "image_url": "https://free-images.com/md/fc7f/adorable_animal_background_164489.jpg",
                        "link_description": "Testing Story Ads",
                        "message": "testing story ads",
                        "title": "This is Headline"
                    },
                    "instagram_actor_id": App_data.instagram_account_id,
                },
                "degrees_of_freedom_spec": {
                    "creative_features_spec": {
                        "standard_enhancements": {"enroll_status": "OPT_OUT"}
                    }
                },
            },
            "status": "PAUSED",
        }

        ad = Ad(parent_id=App_data.ad_account_id)
        ad.update(params)
        ad.remote_create()

        preview = preview_ads(adcreative=ad['id'])
        print(preview)


if __name__ == "__main__":
    video_creator = Story_creation()
    campaign_details = video_creator.creation_campaign()
    adset_details = video_creator.creation_adset(campaign_details)
    video_creator.creation_ad_creative(adset_details)
