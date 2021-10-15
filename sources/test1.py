"""import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.nordstrom.com/api/style/6290742"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
headers["Accept"] = "application/vnd.nord.pdp.v1+json"
headers["Accept-Language"] = "en-US"
headers["cardmember"] = "Non-CardMember"
headers["clientname"] = "d2a00906-5d3f-495b-84be-43d5b44f38c3"
headers["consumer-id"] = "product-page"
headers["content-type"] = "application/json"
headers["countrycode"] = "US"
headers["currency-code"] = "USD"
headers["customerauthstate"] = "anonymous"
headers["device"] = "Display on Desktop"
headers["experiments"] = '{"experiments":[],"optimizely":{"experiments":[{"n":"filter_sorting","v":"filtersorting","p":"FULL_LINE_DESKTOP"},{"n":"hp_stylist_creative","v":"SV2","p":"FULL_LINE_DESKTOP"},{"n":"checkout_pref_store","v":"pref_store","p":"FULL_LINE_DESKTOP"},{"n":"pdp_brand_ingress","v":"Brand_ingress","p":"FULL_LINE_DESKTOP"},{"n":"sbn-account_flyout_update","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"urgency_messaging_order_of_display_with_pick_up","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"reco-3996_ncom_recs_quickview","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"sbn-sr-spa","v":"variation_2","p":"FULL_LINE_DESKTOP"},{"n":"nr_token_migration","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"pdp_enhanced_about_the_brand","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"cam-recognized-user","v":"recognized-user","p":"FULL_LINE_DESKTOP"},{"n":"subheadlines_desktop_mow","v":"B","p":"FULL_LINE_DESKTOP"},{"n":"pdp_fulfillment_choosestore","v":"variation_2","p":"FULL_LINE_DESKTOP"},{"n":"hp_signin_v2_a","v":"signV2A","p":"FULL_LINE_DESKTOP"},{"n":"sbn-sponsoredads","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"checkout_beauty_sample_selection","v":"sample_selection","p":"FULL_LINE_DESKTOP"},{"n":"sbn-campaign_landing_pages__pt1_","v":"product_tray","p":"FULL_LINE_DESKTOP"},{"n":"checkout_shoesthatfit_giving","v":"stf_giving","p":"FULL_LINE_DESKTOP"},{"n":"sbn-availablenearby","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"checkout_paypal_guest","v":"paypal_guest","p":"FULL_LINE_DESKTOP"},{"n":"checkout_reg_paypal_v2","v":"paypal_regv2","p":"FULL_LINE_DESKTOP"},{"n":"pas_size_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"pas_categories_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"nsearch_bm25_weights","v":"Default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"pas_brands_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"}],"id":"c3dbaf83-88c9-4213-bbd2-5f60e820ce11"},"user_id":"c3dbaf83-88c9-4213-bbd2-5f60e820ce11"}'
headers["identified-bot"] = "False"
headers["is-anniversary"] = "false"
headers["is-anniversarycaeaqualified"] = "false"
headers["is-anniversaryea"] = "false"
headers["is-anniversaryeaqualified"] = "false"
headers["is-anniversarystaggeredea1qualified"] = "false"
headers["is-anniversarystaggeredea2qualified"] = "false"
headers["is-anniversarystaggeredea3qualified"] = "false"
headers["is-mobile"] = "false"
headers["is-mwp"] = "true"
headers["is-sizeprefexp"] = "true"
headers["loyaltylevel"] = "non-member"
headers["newrelic"] = "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzMDUxMjEiLCJhcCI6IjMwMjQ2MTM4NiIsImlkIjoiMGYwNTc3YWQ4MTM5MzZiMiIsInRyIjoiMzc2Zjc0Nzc3MjY3Y2Q4NDQzYjQ2MDNiY2JjNmJkODAiLCJ0aSI6MTYzNDExOTg3MjA4OCwidGsiOiIyMjkxMTU0In19"
headers["nord-channel-brand"] = "NORDSTROM"
headers["nord-country-code"] = "US"
headers["nord-customer-qualifications"] = '{"loyaltylevel":"","rewardsmember":false,"cardmember":false,"employee":false,"tenderMember":false}'
headers["nord-postalcode"] = "21301"
headers["shopper-id"] = "a75770cc96f1492c97310524c7bd116b"
headers["tracecontext"] = "defbba2a-28a0-4abd-944d-957d31e0dd6d"
headers["traceparent"] = "00-376f74777267cd8443b4603bcbc6bd80-0f0577ad813936b2-01"
headers["tracestate"] = "2291154@nr=0-1-2305121-302461386-0f0577ad813936b2----1634119872088"
headers["visitorstatus"] = "Repeat Customer"
headers["x-v2-router"] = "v2"
headers["X-y8S6k3DB-f"] = "A3gS-Hh8AQAAYbj4aSx9vfl_fnnRWPBntMspnGndmrpFV9ztrMQht3n4qaM1AcV1oh2cuPlowH8AADQwAAAAAA=="
headers["X-y8S6k3DB-b"] = "fvbah"
headers["X-y8S6k3DB-c"] = "AIA-4Xh8AQAAouVxbw1W4Fa2cjgu84T04HZuS7iX_4Cj1fTW5fPhc9svGZK5"
headers["X-y8S6k3DB-d"] = "AAaihIjBDKGNgUGASZAQhISy1WLz4XPbLxmSuf_____CrffjABL05R8U3QojlUVlSW5DVWc"
headers["X-y8S6k3DB-z"] = "q"
headers["X-y8S6k3DB-a"] = "fhZMY6VPaplkZS9KgguRJi2W2Q41QJqlgD1-g6hVn_NVJKcPiM3GheCK7YarhtRFrqPu2mop_lqGoPHwMoWJ8TghvmmqggWUd3g21=--WYXIYq-2uyWyC2sauzdKS5QdtL2TGa4ZiShQV4eWuTQJVUYB1fZX-ZSmwyknHCsMDaP8QDoqaWEfnCYzmTspA5D6z7lz5eR7GNHcyUh6mvWyOXTprsaE-euo-djYwhzJxbjvgFaiUIGJxWL1eCidZYh66I4IZIQ66ygLUNEELtdRMY3MUI7aH6fL_stGst71B9dm_nzmT5wY-3fN9qx-pMeR_2z1ACx9QcpgdpYys8tstBV2JgxkMn4oTA6e7qM1AxfPHFNuHM8kC2lxp9L6LQ2apqJmUhGWtztOE446bHTIXXtrCEkswpdu61zYtb3p6TlnzzbvN5KyGvLdvzGbGmGI6GNDCBmt6QB7-i1FwPmDrsWkVr5ds85EPVxSGWUE6mDTWZHRuCCuHv_EfNqqXcUWaY2ZRY8e5osmFjjMa_43BncjUahJPFWN8kd5p4rKLUk2nvIdK9NfaqqtoYswL_VSJqDxk6yrFLt=aqqIfpo9HgKn-nGPHNSPUCHR5BwZuoAy8oo=X6OnZqzm65tBWPGZvUAJTKqjS7Iythm7WjMbAN7vP=pBtxgIst_sZBd3W-_x1hLGDI8x6g1h81_fVY--8mo=ArWx4jHkT-QUlWkNcKtkBR9uIR4sfQ4cNlEMOQ69wXCBZB=GD_ugPJCowQFgzmLEt2t61GuDT=RLhGji=GV8CkT9P5HzD4xfVSO-jtNXYQnMMYsE6vFaNguxsNeH3aF9cPaPmYlmuXxuqlVNlD7mQs9KaXn1H=ArGHcAc3a9b6Wg6MsOYyZ-cWJYrhPwWOEnleXgODV3wyom_iT2rtmVsIuK=YJTYvVN2k=np1LiHIEQekk=hi2lbvj25CSbRBfQSpa-qPVccjXYM8NFsxZiF3fcSPdaj3S_FkUnW=y2NH6swJk5RRY=RNs7TBuO-H1N41mgmeUottfn2iavqvfdrlk3Pf=U3mo1tla=hviyh6e-9qrpJf9FWda2Ii4KWUjIVrRYYO5iqQy8dWxi1KqQ381L9u7RaYi2eH96fsHOkmSRZ1CR=nrZs5iySZuduRlDPlNcJ9I2gl2LzQn9MIRmkCazSZ_A7USliGJloU__C9F=OJAA2ayv7xch4leZbExfClEh7i44b=ZUviNEofJfpKGlvY52S1-snDxggkcvDbERPLi3I6bhnUIuaxvDPDNWkRWukGdlQ3NA8JbgToAHPEUo3cHH1AWEOKWK8Ew5NFGy22SCljs-43dj5hnWAeOV-=EbGcOSvbn5ff8dTS11jq2iyGftGSzvrZkGjLaDBqTpmVWNWtReTGFcgMf8KppjhdoAuGmG6_IQXPdl2vDYtwUPBXZsHcUeItAEj6V_-uprMoRQVh3ILIJmUeV3zHlF3G4vJswfVw8lRyXzzlLNbF5Qr-fstqEN-jQ18VHImJ5Pjm5ZBonFVxVh4Z_f4hn97ZBOeMG95hCf4iW3PvsDzQx6Z4sXhAzijxi8-8sCAgutGJbKFvawvpERXdm_CBiZeICE=uKlSjtR9_CfMzmJ1WUGZA94LWiZjekJkz-ch=bXpZ1m_oGFGsrOXjXDmzMMLOAMs48=FViRjxEewCFZ3_cNN-eiNDcqEeeiPNplz5dr7XJhwnPJf9sD517LQAheH5TiYvT=JKxtkKMKWcigUD7LD8sGyNlVbjXKYghEkDpwpWGLLII-uaRJGgU8DmBv_mY=Hm9irk7J2zTo3OEdoRyHV4abhXYQTd3tOyEchaO4P=VMUe=Uceb5JpMf-6zHMkCLqlP=2rLqGx_kEIG4E5idUoIjFLUzJKIVVtNoDcnf1vx3TFGitjW11cl1UJgntlDf2iWANukvdFOduxtZaoqi=kyYgSC=WhPAuQlkS-opOMKnw3nnQihuOrMZgPaSt=WXopiA2BeEuWavkvXvO_U2akLGSjOqrT1sGt2UY=6WloVcz69RybwMKU8ELDld15t=hjW62tOOL7jk4S2A8te_49pqEXY4qbonjjTD7k_RqjwrkhyMpVnqooXtpkIQn3aKW5mlmiirB7EDfBXropD==IlEfPEE3gFSjclZUAqv_7aeGPr2-NNfCADXe=1VcleJUe6dS5fBpj_uYzW3niwsfSxUSsxjm8FUOgCP_EclEeI2O6G8yQwcZcW9LWQPb3pabn_g2K=gY24pVwrP_-I8RHMaiypv3pMk2hvSn6LkPb7ROJoKLmKuGvmLB4GvqahGrE-82Jfzm8h1zBPQ8dRZrAJUjd9_TaCWz-xVBqd6v-Uzkxob_v6E8_Dkd22d_75DWcQzaTs8ymLI73L-AhsRBttMVwl=jIWBePHmLmM2IF_MQCaTrBbtKeZqV44j5hN1ESX9rQVbI_z-Wcxgl6FX_-b4ZEls6HxucCkf3cpcWEpEwoQaeWp1o7fa1LmHDGdzR5R_I_gpP_OpEREd43-pSSz4OtJboZs7SPjLhg4vrmwseE3fv1dgHjrN_XO3tEUyAI1QOeWx2jimmFKUkaEBjzrlTbes=ntAoex6NreV=FNZmBRhKMe8K=4P1Ez1hgRmNHHmbXMWlQQxMKFe3Dhp5LQPWm_YGO1KNLvTSx6uKmoOqGj8nCNPL1=5BwYuRnEGi6VM1cN9RQVERDyRS22sGzWtRaD_8vw98R2YDQjlqJViWM=pZrthDZzZTeNz5ak2FldzlaiQHAH-2uHIODyWwmfD87WGRsUUZXPYJn7g=s-WF1-L8JYBIHNkKdDapBta_APfBvkFW7=lwH3RWJvjkB8gBe7HLRvV5z389Gt8U_pva18HHTw_oGaatb8W4kPy6PtN65-eaYRDbWmsvW-MyLKcA8uO-JiDxOOQo6O1gpOvIKHlLoK3i9WlrR_gn2Trj_K7BvUw1V8r9xN-jBx2D_ZezT9EgVvhohyJfLzHU9vrjYS79PeQi-dcnl8IE_-T_FQ1nGyG=TMlzDZlMt1k4Yt6oivei17kMpqcpZ2a6ywuaJj6AKqc31=AzAtSFK3kE1jiLZw3fsGaFooAeRui=owidIDlxOQ9yIxkl7zgNYcp_1f7med6iz=BtQwMsBnp8tzCyj=ZWn8IrhbtB=O3gTJD28w-uqGjpJ91F6s8KRx1NK6faLIpqG=r3P7UXD3=vxS9gyDcXKvLobCLyxmKp9KzQLqs9U5h-_4Zerx2J1KMQ-yGv8VhW4d_hDstgNAHcEla4xxvL-8S7L61EBfPVIyipU56QZqKQ_a_f1hWoX4UW_c5YsPJFVgOtZrr5Iho-zP56r5cTgGNjG5f15AM8Ym5YV4UssrySNOiRHW2pkJ-AZFHuk6Nl2Qq91DiqrguOfSpfsVGs1GBsJWqw3TRToJwVsnBk7BkL-F5TNvyNK-ZnmI8WO2RkAcP=qqabC3ETVEvhQtTy=o-xjfHo76U3cM7=DBW1whH3r74cgtAXl5Zi87=c=FBqgLWVu=16UWoO=aJRNBC4ouJZ4ICNJazKBpup8gNoT_L9feO3Om2xeUi=nQVBfBwaMJ27hBPVUGvPTGuhJf6VVSRrYi7Uy_6qzwkjq9dznctTpuKS7laYNrZV5iQu1NpGFUGS24thE6-nJFVm1jWjTFFXZ1Xf_LPbpeMmmP4XSZsULfFSveXpYP-FcXBc-zdu_syyUR4ErNcK4DNRQs2rgII_RMZKx8eFpdonnAjJwZNgMMbc2PwWC=hNphIZ6MHCvpUB6QsU3IvHJlaoL9kbxzqa8z3EbKMv5SG_msohsUBTs9E-6bklLFbTL=9N1xVV1ECrwlXQqP9Oz_Uk9=w8srBKLmydUcHZElP5hkQJPcQtUMHYsNc22pNRYWCbbnYgcct1zv9gwc2xxRynPU6LWKINqbz=mzcnWzne_EpGOcd6ZlujForbD9v_4sw2KWBTA7cJBmZICALt5=7BvhdA9H3yn24Yh6Zf=h3gvt7_fXj54Tr8Kytd5gzks8-ZHQ7O=UKTIOqoUeveUWDyoCGEP56"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["Referer"] = "https://www.nordstrom.com/s/levis-wedgie-icon-fit-high-waist-straight-leg-jeans-these-dreams/6290742?origin=category-personalizedsort&breadcrumb=Home%2FWomen%2FClothing&color=420"
headers["Connection"] = "keep-alive"
headers["Cookie"] = "Ad34bsY56=AFqXuVF8AQAA7YgFtsCjJHsAxseCKMQALnY7FPiEc7L5dMMAL43UshQ8Y3wS|1|1|4b4cfbc99ec7e552156c46280fa90b9740f8ad4c; internationalshippref=preferredcountry=US&preferredcurrency=USD&preferredcountryname=United%20States; no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=a75770cc96f1492c97310524c7bd116b&USERNAME=; nui=firstVisit=2021-10-05T18%3A31%3A31.521Z&geoLocation=&isModified=false&lme=false; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhNzU3NzBjYzk2ZjE0OTJjOTczMTA1MjRjN2JkMTE2YiIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5NDg5OTE0OTEsInJlZnJlc2giOjE2MzM0NzMwOTEsImp0aSI6Ijg2YzA5ZGQ3LWNjY2EtNGE3MC04N2Q0LWZlODVhMDQyN2JmMiIsImlhdCI6MTYzMzQ1ODY5MX0.HXJc945CkPaT_aYv64AGXKK_gi_RUxZ8IQGkhfFUk9Fygy1agea_arS-t6nXYvT5XJROGuhA2SnfKjtEBWdFoEQ_tpuKgbb832vdE0Buiq5SXP6DwvbEQm_1Jcp81jaTKAmCz_pCdjT3W5g4CR-hJKss7TSl6_m32JguxUrIEG4MzDOBxp_-cdFh6hSOVd7gonUzJE7uv8ituIE_FhVEe9rQrQ2mSvJRXioIEGy2AmuxAQ10qS_r1umwp-FkWMDa5BiDYpcLyiNVqcDYalA8Pyf7WTrt97texWNAYD_YoQLJw8aoH3SulU3h7jKqgwM-lMxpkfMjK6u1Y-8QJAGQQQ; experiments=ExperimentId=c3dbaf83-88c9-4213-bbd2-5f60e820ce11; Bd34bsY56=AN8xInl8AQAAwn6BsPO14DaY4TessYGHkcJBywkwA746YXRK6aHTCZ5MsujB; forterToken=8d87d40cc711483f8d181f8fbca70836_1634117095421__UDF43_6; _gcl_au=1.1.886446307.1633458711; storemode=version=4&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; storeprefs=|100|||2021-10-13T09:25:02.503Z; _ga_XWLT9WQ1YB=GS1.1.1634119833.5.1.1634119873.20; _ga=GA1.2.160709569.1633458715; _imp_apg_r_=%7B%22c%22%3A%22VXlpTThMMVY5a3FrRHdqbA%3D%3DOuknDwnIUaZYQU_GDWKIWoA8T_vbgbKXBDffXD2hWEgaZYhViGoZVaLNVjlhrCFXbefAx6-_VI7qu9WGAXJNDp7dXunUlw%3D%3D%22%2C%22dc%22%3A1%2C%22mf%22%3A0%2C%22_fr%22%3A20000%2C%22fr%22%3A%226KIOBlWmYoXBFTOcxS-kMQ%3D%3DWt741Dvp4uYiEc3kK9ylqVjZlVkTrErSQN7R5Qu5Sezh2BctJ_YtgJOp2TCT1-N7F-hLSs5SW_6-DcqFZQ%3D%3D%22%7D; ftr_ncd=6; rkglsid=h-b28156d49e8add029fe1010017c51b9f_t-1634119854; _pin_unauth=dWlkPVltUTVNekEzWmpndFl6RmpOQzAwTkRRMkxUZ3dPR1l0TlRobU1UY3lZakJoWlRjeQ; _fbp=fb.1.1633458722311.522931396; rfx-forex-rate=currencyCode=USD&exchangeRate=1&quoteId=0; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0&; usersession=CookieDomain=nordstrom.com&SessionId=c044e30a-e023-4c33-b24c-572857dcbc44; _gid=GA1.2.477122038.1634117100; _4c_mc_=a7de90bf-1fa8-4294-b345-b42705ab019f; _gat_UA-107105548-1=1; _uetsid=6fc6a6502c0711ec98f8afca42b24d62; _uetvid=84ad9a60260a11ecb9d71bab6bf0bf68"
headers["TE"] = "trailers"


resp = requests.get(url, headers=headers)

print(resp.status_code)

"""




from seleniumwire import webdriver  # Import from seleniumwire
import time
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
print(driver.execute_script("return navigator.userAgent;"))
#driver = webdriver.Chrome(options =options)

# Go to the Google home page
driver.get('https://www.nordstrom.com/browse/women/clothing?breadcrumb=Home%2FWomen%2FClothing&origin=topnav')
time.sleep(10)
# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if "api/browse/browse/women/clothing" in request.url:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
