import datetime
import os
from datetime import date



class TestData:
    # influencers credentials
    Base_URL = "https://staging-staging-platform.social.quotient.com/signup"
    TITLE = "Quotient Social "
    # LOGIN_EMAIL = "vunopi@tutuapp.bid"
    LOGIN_EMAIL = "sharad@ubimo.com"
    LOGIN_PASSWORD = "aA111111"

    IO_name = f"Testing_vivek_{datetime.date.today()}"
    Creative_string ="""<script src='mraid.js'></script> <img src="data:image/gif;base64,TlND" onerror="{if(typeof_caf==='undefined')_caf=[];var m=Math,t=this,i=t.id+'-'+m.floor(m.random()*99),c=_caf,f,s;c[i]={};f=c[i].pp={};f.h='https:';f.cs=f.h+'//cdn2.crispadvertising.com/CDNbanners/DEFAULT/';f.cp=t.id.split(/-[A-Za-z0-9]/)[1].replace(/[^0-9]/g,'/')+'/';f.vu='%VEW%';f.cu='{REPORT{U0}{CLICK}}';f.au='{REPORT{U0}{MINOR}{}{}}';f.eu='{REPORT{U0}{INTERACTION}}';f.xp='lparam=channel:UBIMO;auction_id:{BID_ID};DSP_ADV:{ADVERTISER_ID};DSP_ORDER:{IO_ID};DSP_LINE:{PLACEMENT_ID};DSP_CID:{CAMP_ID};DSP_CRID:{CRT_ID};exchange:{EXCHANGE_ID};APPID:{APP_ID};SITE:{BUNDLE_ID};user_ip:{IP};zip:{ZIP_CODE};geo:{LATITUDE},{LONGITUDE};did:{UCDID};didtyp:{CDID_TYPE};LMT:{LMT};SIZE:{WIDTH}x{HEIGHT}';t.id=i;s=document.createElement('script');s.setAttribute('type','text/javascript');s.setAttribute('src',f.cs+f.cp+'pgc.js');t.appendChild(s)}(this)" width="5" height="5" style="display:none" onload="this.onerror();" alt="." id="crisp-a237p4776z110368"/>
"""

    Creative_name = f"Creative_promo_{datetime.date.today()}"

    Promoname = "Promo_amp"
    Pro ="1"
    imp = "10"
    cpm ="2.09"
    Week = "1"
    cta = "https://gic.com"
    audi ="Beverages"

    Line_name = f"Line_items{datetime.date.today()}"
    Target = "10"
    product ="1"
    Retailer_id = "12"
    banner_code = "12345"
    offer_price = ".09"

    Tactics_name = f"Tactics_name{datetime.date.today()}"
    Tactics_imp = "10"

    def env_setup(self):
        if os.environ.get('Env') =="Prod":
          return  "https://media.quotient.com"
        else:
           return  "https://qa.media.quotient.com"