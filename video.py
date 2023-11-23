import datetime
import os

import requests
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.advideo import AdVideo
from facebook_business.api import FacebookAdsApi

from Config import App_data


class Video_creation:
    video_upload_url = "https://graph-video.facebook.com/v18.0/139571262574677/videos"
    page_access_token = "EAAOmtky97ZA0BO7DEcBt2g09tVDdVEL0CNPZCmwPs4EXK2gZBQVIEomXXwc7egmq7ZAoch8sZALp20gtTA3pWXC77qpLbBB61Haj6X356623Cqg9obAzRZCwcAol4rI7PJZBrwiKMjKkrsYMzCrZAeFBDhgvOLZBqFwMBFNG7aT1joQShian62Ambm3QWpWDF6lWO"
    video_file_path = f"{os.getcwd()}/blank.mp4"
    max_retries = 3

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

    def __init__(self):
        FacebookAdsApi.init(access_token=App_data.access_token)

    def creation_campaign(self):
        params = {
            "name": "Videosads-Facebooak-and-Instgram-campaign",
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
                "name": "Videoads-FacebookandInsta-Adset",
                "campaign_id": campaign_result["id"],
                "bid_amount": 100,
                "billing_event": "IMPRESSIONS",
                "optimization_goal": "REACH",
                "targeting": {
                    "geo_locations": {"countries": ["US"]},
                    "publisher_platforms": ["facebook", "instagram"],
                    "facebook_positions": ["feed", "story", 'marketplace','instream_video','video_feeds'],
                    "instagram_positions": ['story', 'stream', 'explore', 'reels'],
                },
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        adset.remote_create(params={"status": "PAUSED"})
        return adset['id']

    def creation_ad_creative(self, adset):
        video = AdVideo(parent_id=App_data.ad_account_id)
        video[AdVideo.Field.filepath] = f"{os.getcwd()}/output_file.mp4"
        video.remote_create()
        video_id = video[AdVideo.Field.id]

        params = {
            "name": "Video-Ad",
            "adset_id": adset,
            "creative": {
                "object_story_spec": {
                    "page_id": App_data.page_id,
                    "video_data": {
                        "call_to_action": {
                            "type": "LEARN_MORE",
                            "value": {"link": "https://google.com"},
                        },
                        "link_description": "Testing Videos ADs",
                        "video_id": video_id,
                        "image_url": "https://free-images.com/md/fc7f/adorable_animal_background_164489.jpg",
                        "message": "Latest videos Ads testing",
                    },
                    "instagram_actor_id": App_data.instagram_account_id,
                    "plugged_in_events": [
                        "INSTAGRAM_FEED",
                        "INSTAGRAM_STORIES",
                        "INSTAGRAM_EXPLORE",
                        "INSTAGRAM_REELS",
                    ],
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




if __name__ == "__main__":
    video_creator = Video_creation()
    campaign_details = video_creator.creation_campaign()
    adset_details = video_creator.creation_adset(campaign_details)
    adcreative_details = video_creator.creation_ad_creative(adset_details)
    # ad_details = video_creator.creation_ad(adset_details, adcreative_details)
