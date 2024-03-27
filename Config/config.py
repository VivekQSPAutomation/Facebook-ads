import os
from datetime import date


class TestData:
    # influencers credentials
    Base_URL = "https://staging-staging-platform.social.quotient.com/signup"
    TITLE = "Quotient Social "
    # Stage_LOGIN_EMAIL = "menimaco@clip.lat"
    Stage_LOGIN_EMAIL = "qsptestmail@rediffmail.com"
    Prod_LOGIN_EMAIL = "digoface@closetab.email"
    LOGIN_PASSWORD = "vivek@123"
    NEWPASS = "vivek@1234"
    CONFIRMPASS = "vivek@1234"
    Confirmation_msg = (
        "If you have an account with us you will receive an email to reset your password. If you do "
        "not receive an email, please contact support."
    )
    DRAFT_MSG = "SUCCESS. YOUR DRAFTS HAVE BEEN SENT TO QUOTIENT. WE WILL REVIEW THEM AND GET BACK TO YOU"
    EDIT_MSG = "Success. Your Edits have been sent to Testing"
    SOCIAL_EMIAL = "vivektestmeli@gmail.com"
    SOCIAL_PASS = "vivek@123"
    PIN_EMAIL = "vivektestmel@gmail.com"
    PIN_PASS = "vivek@1234"
    # Facebook_Socail_Email = "quovivek@rediffmail.com"
    Facebook_Socail_Email = "facebookchecksmailbox@rediffmail.com"
    Facebook_SOCIAL_PASS = "vivek@123"

    ## Filter dashboard
    filter_dash = "Your campaign has been saved."
    Filtername = "Testing_filter"
    mediaBudget = "10"
    imp_count = "100"

    USER_INFORM = "Information has been saved!"
    FACEBOOK_MSG = "FACEBOOK HAS BEEN AUTHENTICATED, THANK YOU!"
    PINTEREST_MSG = "PINTEREST HAS BEEN AUTHENTICATED, THANK YOU!"
    INSTAGRAM_MSG = "INSTAGRAM HAS BEEN AUTHENTICATED, THANK YOU!"

    # Ahalogist Credentials
    # Base_URL = f"{TestData.env_setup(self)}/signup"
    Aha_login_email = "evan@ahalogy.com"
    Aha_login_password = "Testmuse123"

    Campaign_msg = (
        "Your campaign and SF opportunity were created and connected successfully."
    )
    Applicaiton_msg = "Application emails for Short Form Video are sending to 1 partners. You can leave the page."
    Onboarded_MSG = "SUCCESS! EMAIL SENT TO THIS INFLUENCER"
    Draft_saved = "SUCCESS. YOUR DRAFT HAS BEEN SAVED"
    Add_to_queue_msg = "SUCCESS! THIS INFLUENCER WAS SUCCESFULLY ADDED TO THE QUEUE."
    remove_msg = (
        f"TestingTesting has been successfully removed from Testing_QA_{date.today()}"
    )

    Sign_brief_msg = "YOU HAVE ACCEPTED THE PROJECT BRIEF FOR TEST - COUPONS TE_Q279425_QMP CAMPAIGN."

    Gittoken = "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"

    smtp_host = "smtp.gmail.com"
    smtp_port = 465
    smtp_email_id = "aairflow_dev@quotient.com"
    smtp_password = "sopbdbybapmztpqp"

    Campaign_prod_name = "Q203537"
    Campaign_performance_name = "OB570X8TL"
    Campaign_name = "OS3OY4NTL"
    Add_opp = ["OB570X8TL"]
    camp_price = ["OJQPW4NTL", "OB570X8TL", "OPPF386TL", "OLUOM5QTL-1947-1"]
    # Campaign_name = "OPPF386TL"
    # Campaign_name = "Q263199"

    #####Facebook and instagram Ads Config ####

    ad_account_id = "act_7044521622279409"
    access_token = "EAAOmtky97ZA0BO0Xxk3SjhPU7yTrNL36G2eAZAk78D4HvgyZCctUSEwMmEfICbsWm6ZAwmZCeFKZCSw1kmWOISGTzxrZCAkKbvA7WMhuImzVXDK1pyZBdPhqVgDmb8tPJInXy7dioZComHZCyGGZAysxr93wriY1u5PrS5kU7AKqSBKDhpTGfyrfECYIcmM78vw2srb"
    # access_token = "AAOmtky97ZA0BO3RGjtoB3JGvuLgQQCDySLdrYsWDgPwnPUnDGrXxgRWYWqdNMVSZCNrqSfTad7sNg2eEdmvf4HK0lad7u60ZBqp5a9KB0x2mcGXiQ7fK332hXL0RJF62aeSYkIe2XKI9FC7HCBAqoAZBFKEjSH3weWWGZA9leyZBid8xI9gjMuS9ZCENzEYTqw"
    app_secret = "cfbcca04aa930c2b26d4926495a62d09"
    app_id = "1027726831906205"
    page_id = "139571262574677"
    instagram_account_id = "6437798096331313"
    page_access_token = "EAAOmtky97ZA0BOxqrJTKp0k8V4jqrZAprrR2wHKhTaFHOku8UflcKwL7aFlLOc4lZA1qJdafjOQsp4UFSHlBFre2aHpULiG0hwqRZB6SoY5KrLCC0Gf8rNL7OOmz5UZA7mGpeilSas5ERVwzz3sWYiZCiGk9bnXPGOBkYZBro9ZCB8Jl1CMVAAz92M1ed55MO3tZC"

    def env_setup(self):
        if os.environ.get("Env") == "Prod":
            return "https://platform.social.quotient.com"
        else:
            return "https://staging-platform.social.quotient.com"
