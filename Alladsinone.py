import datetime
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi
from Config import App_data
from Casourelads import Carosuel_creation
from Staticads import Static_ads
from storyads import Story_creation
from video import Video_creation

class AllinOne:

    def __init__(self, access_token):
        FacebookAdsApi.init(access_token=access_token)

    def creative_camapignandadset(self):
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
                    "facebook_positions": ["feed", "story", 'marketplace', 'video_feeds'],
                    "instagram_positions": ["story", 'reels'],
                },
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        adset.remote_create(params={"status": "PAUSED"})

        return adset['id']

    def create_ads(self, adset):
        static_ads = Static_ads()
        carousel_creation = Carosuel_creation()
        video_creation = Video_creation()
        story_creation = Story_creation()

        static_ads.create_Ads(adset)
        carousel_creation.creative_ads(adset)
        video_creation.creation_ad_creative(adset)
        story_creation.creation_ad_creative(adset)

if __name__ == '__main__':
    access_token = App_data.access_token
    all = AllinOne(access_token)
    adset = all.creative_camapignandadset()
    adset = all.creative_camapignandadset()
    all.create_ads(adset)
