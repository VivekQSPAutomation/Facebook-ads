import requests

ad_account_id = "832621328338450"
access_token = "EAAOmtky97ZA0BO7DEcBt2g09tVDdVEL0CNPZCmwPs4EXK2gZBQVIEomXXwc7egmq7ZAoch8sZALp20gtTA3pWXC77qpLbBB61Haj6X356623Cqg9obAzRZCwcAol4rI7PJZBrwiKMjKkrsYMzCrZAeFBDhgvOLZBqFwMBFNG7aT1joQShian62Ambm3QWpWDF6lWO"
campaign_endpoint = f"https://graph.facebook.com/v18.0/act_{ad_account_id}/campaigns"
adsets_endpoint = f"https://graph.facebook.com/v18.0/act_{ad_account_id}/adsets"
ads_endpoint = f"https://graph.facebook.com/v18.0/act_{ad_account_id}/ads"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(campaign_endpoint, headers=headers)
campaigns_data = response.json()


for campaign in campaigns_data['data']:
    campaign_id = campaign['id']
    if not campaign_id:
        continue

    adsets_response = requests.get(
        f"{adsets_endpoint}?filtering=[{{'field':'campaign.id','operator':'IN','value':['{campaign_id}']}}]",
        headers=headers)
    adsets_data = adsets_response.json()


    for adset in adsets_data['data']:

        adset_id = adset['id']

        if not adset_id:
            continue

        ads_response = requests.get(
            f"{ads_endpoint}?filtering=[{{'field':'adset.id','operator':'IN','value':['{adset_id}']}}]",
            headers=headers)
        ads_data = ads_response.json()

        for ad in ads_data['data']:
            ad_id = ad['id']

            if not ad_id:
                continue

            print(f"    Campaign ID: {campaign_id}")
            print(f"    AdSet ID: {adset_id}")
            print(f"    Ad ID: {ad_id}")

            print("\n")

    print("\n" + "=" * 30 + "\n")
