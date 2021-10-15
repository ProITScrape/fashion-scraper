import requests
import json
from requests.structures import CaseInsensitiveDict
s= requests.Session()
url = "https://www.nordstrom.com/api/cupcake/"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
headers["Accept"] = "*/*"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["Content-Type"] = "application/vnd.nordstrom.cake.v1+json"
headers["appid"] = "APP01196"
headers["eventtime"] = "1634136029518"
headers["geolocation"] = "undefined"
headers["identified-bot"] = "False"
headers["newrelic"] = "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzMDUxMjEiLCJhcCI6IjMwMjQ2MTM4NiIsImlkIjoiOWYwMzU3YzkxYmQyMTEwZSIsInRyIjoiMDdiNzI4MDdlYjNmMzY2ZDc2ZWJhY2EzNDhmOWY4NzAiLCJ0aSI6MTYzNDEzNjAyOTUxOSwidGsiOiIyMjkxMTU0In19"
headers["nord-channel-brand"] = "NORDSTROM"
headers["nord-client-id"] = "mwp"
headers["nord-request-id"] = "a1ac55ae-de89-46c5-85e3-cec44e892e68"
headers["systemtime"] = "1634136029519"
headers["traceparent"] = "00-07b72807eb3f366d76ebaca348f9f870-9f0357c91bd2110e-01"
headers["tracestate"] = "2291154@nr=0-1-2305121-302461386-9f0357c91bd2110e----1634136029519"
headers["Origin"] = "https://www.nordstrom.com"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["Referer"] = "https://www.nordstrom.com/browse/women/clothing?breadcrumb=Home%2FWomen%2FClothing&origin=topnav&page=5"
headers["Connection"] = "keep-alive"
headers["Cookie"] = "Ad34bsY56=AFqXuVF8AQAA7YgFtsCjJHsAxseCKMQALnY7FPiEc7L5dMMAL43UshQ8Y3wS|1|1|4b4cfbc99ec7e552156c46280fa90b9740f8ad4c; internationalshippref=preferredcountry=US&preferredcurrency=USD&preferredcountryname=United%20States; no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=a75770cc96f1492c97310524c7bd116b&USERNAME=; nui=firstVisit=2021-10-05T18%3A31%3A31.521Z&geoLocation=&isModified=false&lme=false; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhNzU3NzBjYzk2ZjE0OTJjOTczMTA1MjRjN2JkMTE2YiIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5NDg5OTE0OTEsInJlZnJlc2giOjE2MzM0NzMwOTEsImp0aSI6Ijg2YzA5ZGQ3LWNjY2EtNGE3MC04N2Q0LWZlODVhMDQyN2JmMiIsImlhdCI6MTYzMzQ1ODY5MX0.HXJc945CkPaT_aYv64AGXKK_gi_RUxZ8IQGkhfFUk9Fygy1agea_arS-t6nXYvT5XJROGuhA2SnfKjtEBWdFoEQ_tpuKgbb832vdE0Buiq5SXP6DwvbEQm_1Jcp81jaTKAmCz_pCdjT3W5g4CR-hJKss7TSl6_m32JguxUrIEG4MzDOBxp_-cdFh6hSOVd7gonUzJE7uv8ituIE_FhVEe9rQrQ2mSvJRXioIEGy2AmuxAQ10qS_r1umwp-FkWMDa5BiDYpcLyiNVqcDYalA8Pyf7WTrt97texWNAYD_YoQLJw8aoH3SulU3h7jKqgwM-lMxpkfMjK6u1Y-8QJAGQQQ; experiments=ExperimentId=c3dbaf83-88c9-4213-bbd2-5f60e820ce11; Bd34bsY56=AOxLGHp8AQAAm9pSPS-mD4DXyLmknQ-0RwgVWWxw12XYa-uw0hJAI3P-ZjDA; forterToken=8d87d40cc711483f8d181f8fbca70836_1634135614653__UDF43_6; _gcl_au=1.1.886446307.1633458711; storemode=version=4&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; storeprefs=|100|||2021-10-13T14:33:40.957Z; _ga_XWLT9WQ1YB=GS1.1.1634135239.8.1.1634135977.6; _ga=GA1.2.160709569.1633458715; _imp_apg_r_=%7B%22c%22%3A%22VEZtVG1zQlp0Y2tJWHJBSQ%3D%3D5tLQfH7up7FavOe2XQSvIcclqiSRLOm3yGcyZsmjXmOUAN9MbDrSBzif-jvtDo3mS2w-f_TZmxt0jvbBE4yKZqAXAOGydQ%3D%3D%22%2C%22dc%22%3A1%2C%22mf%22%3A0%2C%22_fr%22%3A20000%2C%22fr%22%3A%22rnqcZAStgBO6VMy1bD-8Pw%3D%3DhI_uIxBwFD4RAkQOTWDQcFiZHakSE4j1NCUWb6_9a8WTHEFzkCfobbR0o25YURTPIUr-IDjQJuXvJ7yonQ%3D%3D%22%7D; ftr_ncd=6; rkglsid=h-b28156d49e8add029fe1010017c51b9f_t-1634135981; _pin_unauth=dWlkPVltUTVNekEzWmpndFl6RmpOQzAwTkRRMkxUZ3dPR1l0TlRobU1UY3lZakJoWlRjeQ; _fbp=fb.1.1633458722311.522931396; _gid=GA1.2.477122038.1634117100; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0&; usersession=CookieDomain=nordstrom.com&SessionId=c044e30a-e023-4c33-b24c-572857dcbc44; _4c_mc_=a7de90bf-1fa8-4294-b345-b42705ab019f; rfx-forex-rate=currencyCode=USD&exchangeRate=1&quoteId=0; __ts_xfdF3__=296609933; _uetsid=6fc6a6502c0711ec98f8afca42b24d62; _uetvid=84ad9a60260a11ecb9d71bab6bf0bf68; _gat_UA-107105548-1=1"
headers["TE"] = "trailers"

data = '[{"type":"com.nordstrom.event.customer.Engaged","data":{"action":"CLICK","context":{"id":"6ba5b440-6b34-4d33-938b-50674829bc3c","pageInstanceId":"4cf1c4a3-02c4-42a6-8cb7-88ae13b317da","pageType":"CATEGORY_RESULTS","digitalContents":[]},"customer":{"idType":"SHOPPER_ID","id":"a75770cc96f1492c97310524c7bd116b"},"element":{"id":"ProductResults/ProductGallery/Pagination","type":"HYPERLINK","value":"Next"},"eventTime":1634136029518,"source":{"channel":"FULL_LINE","channelCountry":"US","platform":"WEB","feature":"ProductResults"}}}]'


resp = s.post(url, headers=headers, data=data)

print(resp.status_code)
import time
i=0
while i <1000:
    
    #time.sleep(2)
    #print(i)
    url = "https://www.nordstrom.com/api/browse/browse/women/clothing?offset=%s"%(str(i))
    import requests
    from requests.structures import CaseInsensitiveDict


    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["cardmember"] = "Non-CardMember"
    headers["content-type"] = "application/json"
    headers["country-code"] = "US"
    headers["currency-code"] = "USD"
    headers["customerauthstate"] = "anonymous"
    headers["experimentid"] = "c3dbaf83-88c9-4213-bbd2-5f60e820ce11"
    headers["experiments"] = '{"experiments":[],"optimizely":{"experiments":[{"n":"checkout_paypal_guest","v":"paypal_guest","p":"FULL_LINE_DESKTOP"},{"n":"reco-3996_ncom_recs_quickview","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"subheadlines_desktop_mow","v":"B","p":"FULL_LINE_DESKTOP"},{"n":"hp_stylist_creative","v":"SV2","p":"FULL_LINE_DESKTOP"},{"n":"cam-recognized-user","v":"recognized-user","p":"FULL_LINE_DESKTOP"},{"n":"sbn-campaign_landing_pages__pt1_","v":"product_tray","p":"FULL_LINE_DESKTOP"},{"n":"filter_sorting","v":"filtersorting","p":"FULL_LINE_DESKTOP"},{"n":"checkout_beauty_sample_selection","v":"sample_selection","p":"FULL_LINE_DESKTOP"},{"n":"pdp_enhanced_about_the_brand","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"pdp_fulfillment_choosestore","v":"variation_2","p":"FULL_LINE_DESKTOP"},{"n":"checkout_shoesthatfit_giving","v":"stf_giving","p":"FULL_LINE_DESKTOP"},{"n":"sbn-sponsoredads","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"urgency_messaging_order_of_display_with_pick_up","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"sbn-availablenearby","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"sbn-account_flyout_update","v":"variation_1","p":"FULL_LINE_DESKTOP"},{"n":"sbn-sr-spa","v":"variation_2","p":"FULL_LINE_DESKTOP"},{"n":"pdp_brand_ingress","v":"Brand_ingress","p":"FULL_LINE_DESKTOP"},{"n":"checkout_pref_store","v":"pref_store","p":"FULL_LINE_DESKTOP"},{"n":"nr_token_migration","v":"Default","p":"FULL_LINE_DESKTOP"},{"n":"hp_signin_v2_a","v":"signV2A","p":"FULL_LINE_DESKTOP"},{"n":"checkout_reg_paypal_v2","v":"paypal_regv2","p":"FULL_LINE_DESKTOP"},{"n":"pas_brands_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"pas_size_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"pas_categories_profile_page_on_desktop_mow","v":"default","p":"FULL_LINE_BACKEND_SERVICE"},{"n":"nsearch_bm25_weights","v":"Default","p":"FULL_LINE_BACKEND_SERVICE"}],"id":"c3dbaf83-88c9-4213-bbd2-5f60e820ce11"},"user_id":"c3dbaf83-88c9-4213-bbd2-5f60e820ce11"}'
    headers["feature-flags"] = "issponsoredadsforbrowseactive"
    headers["identified-bot"] = "False"
    headers["includecontent"] = "false"
    headers["ismobile"] = "false"
    headers["isusereventqualified"] = "false"
    headers["loyaltylevel"] = "non-member"
    headers["newrelic"] = "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzMDUxMjEiLCJhcCI6IjMwMjQ2MTM4NiIsImlkIjoiZGYyZDk2M2M2MWVkOTRmZSIsInRyIjoiMDg3YTAyZTE4N2YxNjZhYTZmMzg5YTZlYjUwZmQ4OTAiLCJ0aSI6MTYzNDEzNjAzMDI1OCwidGsiOiIyMjkxMTU0In19"
    headers["nord-channel-brand"] = "NORDSTROM"
    headers["nord-context-id"] = "6ba5b440-6b34-4d33-938b-50674829bc3c"
    headers["nord-country-code"] = "US"
    headers["nord-postalcode"] = "21301"
    headers["nord-request-id"] = "d5ece2f0-1403-4e9d-87e6-277b6d414c3b"
    headers["nord-searchapi-version"] = "1"
    headers["nordapiversion"] = "1.0"
    headers["tracecontext"] = "eb18e20f-8d24-46c2-b40a-9d0630b10f38"
    headers["traceparent"] = "00-087a02e187f166aa6f389a6eb50fd890-df2d963c61ed94fe-01"
    headers["tracestate"] = "2291154@nr=0-1-2305121-302461386-df2d963c61ed94fe----1634136030258"
    headers["userauthentication"] = "Anonymous"
    headers["userid"] = "a75770cc96f1492c97310524c7bd116b"
    headers["userqualificationtype"] = "-1"
    headers["visitorstatus"] = "Repeat Customer"
    headers["X-y8S6k3DB-f"] = "A5egEnp8AQAAMiTnGqaxlVhSpjIyRPGcM4nAej9Ml3s54DbgcEvufzcVMeTkAcV1oh2cuPlowH8AADQwAAAAAA=="
    headers["X-y8S6k3DB-b"] = "-h5xar8"
    headers["X-y8S6k3DB-c"] = "AEBeD3p8AQAAC1FYeE9IZIWwxm9DGh6qPKrT2vbsHe0uePiR4aIlokIvSpgN"
    headers["X-y8S6k3DB-d"] = "AAaihIjBDKGNgUGASZAQhISy1WKiJaJCL0qYDf_____CrffjAD1r_xaeiuH8Yy3CgafwXi8"
    headers["X-y8S6k3DB-z"] = "q"
    headers["X-y8S6k3DB-a"] = "zXL1Ejj=w1MvULw2fZUlKRiR8BQTIdUtThKiY8w_9-gt3wnw6m7wwfPZfJkITnZ5cBUIdNNVOgAi=nY_G_A=-q=24aF8w9VPzW8aO9_fTodB3jz-9Y435RngUvZ6D9e6E7GBN_2YO6IUEJj2UTgPynw_2kIXziZjWSX9oHeLMe=OVyT6LCX5fyhfzImkUHC4UeefLy9p=7ZU3nrB744QB9W5I-yGZ22cr3jXN-3b46heX-PM-1kKBqEbUWtEeREJkKtxkmPu_Bl2shYeKC3w5NOK2JvLzBYwqHDIpKH6-4-oqstjY7-_wAkTTu334EK6fFnNFbTBo8sZHNQ=WH6U6hFzJhsB_94Kn3gHX75q5jTAUWdvnBM5QDXXvOeFqIok_=pCSmDR6Ish78aTviNH5jhpl2cobDuGtVRsEdajmFofYKiER2h1tCUuCXG9h-OXsMrQzDzclEwAioEwjX7kTGywAsJ-nD5zApQ9HGr9LpRYLIUzD52DYCXFGDRIni1=uvcRD=2LMG67MUgKw=1S1DWOe9BT4N7ZF-DxLHSj-__nnK_=ACw=K=6KW-OrpknqcPFLstffIFC6L95ZnX=dGLk=WbgL8-faeiLZUmWfjmFgO8Te-Um-uWE837xgAkbFV-uo4lOtr7xF5nAwUzE9D_qFdKSS6nqP1uxTGlb25JGcnvn16Zub9-ufXkjuYK62_ToRtCZ22zPwCZCvTTkAcNO58Qr2nVNHrvv1BkOLoUH-Tgp9Q5cv-yJPnFxVlELhiz1c-FOykziuXIFX-t2PZPUa4FS2Iz3VAv1VEsQiCr5R17yGkq7ul4h5iZlQpelj9xQTLtvCdLlqeL78az52=WHMslXaju7crs3hwpQK32a2OJqrqWYCHdsrlyHgMLnQBgHCsb=acdX_-wpPNQySpEvAqBFyii7ilnYExkeZtLIJ9VFYJIjh_D9__BTekjpLCTv2F43_eUGLWSj9E-iNIIE1s5FnwkTnrqzQ8lfiwTyXG4l7bl=xLQaet56wmFX9-h4ihEWCM=ojPqnRM6mMju55f9siQ_NNkiHAHjsfshHHqGWqlOmuNP6OcEDuwXNVg8vHtcpBM-Jj5TC2CErokIVnONM9mHtffvCevFox_3dw5hZ4NIqyooU=NkFBv5=qa5uVkSR34ufvzrTSw9AAt_kfMEmQbXSe9J8qTCGokRsHn4lHBXno-1u-qXZLGsEWfHwQGnQUB99LBWp=qV7Zj_AwbScyr4TQxbSkEU8TjgVD7r85MQfgu6ujxKdZa5prkVwz-Vt6axgK4RkgPv93F9D82Ua81kdEPsMmoY58iF6iLsgZXmmBjxsmqzJ-kD6enbJeOFsIr-tjRwBj5h9X2yaHEiZ9rbgopq=FHvilOvA=_Z2d_KY6V42z52dESw_=somK1cjXJIi-FAvYHaqifgTpM1Rb7r8HGB_5QBP2NPAr7iX8k28lfaIzA-e8SLLBblqiQSrq8AAWIXs7S64DiW2tqstlEWLjWKnutgAGxtXFXq_KpWqSEQCg2=xkYl5xKfdgxYQbDAxhsP5D_ehFurOq=JnCC9QUZJY8uCuZbXJb2UN1xWq5-7=4_w5zKnCC=ufbDV5wdEZCQaP-rWZgyFJ6twm-qniwslUM6O-QHy7YRnf6OnyXr-3_yZmWqSO7j5q2HRFVS-dMS-lnQg2YKZTObvplCEM4HwR6zjSS4lHPZ5HYDb1almJDWFR1m6taNdzCojTzxD3ZcQ19GLTZnSEX-EOYwQ5NpbiXOckH5B4u9EGV3VHHgHqsp-rpTP39fSSzBQ9AbEVoSOJ=6gzg47Xxn2EjGCOMSqcJGa-VoTEHjKmLhPNzM7owOO2wPYGaXv_8_hjS1FBvAnJaxc3agnbzP8Hmju4wv28JFLrDIC5=9W5M7YyNMqgCBm3bJ3e_vjU4_jj6cpzwjAGIWCe9iMcN2st5IRaLsN7GkyalJixG7qhZNP_ful1tARTJfy=KH46j47=UDLiV-cfUOW4YteBh1xwtYJcJ1lDJG3wtmGFgPQQvGzDB2kZKBl7-i3NuOG5t5A8RfGEa6NgWycb1cH57tapVAR_gR624SYs-8_KOVp-6BaoMjN=OULEZgaar1wfEDBlkkboaENz4evMtD21T6KVUdcPdhsDAOmpRV7gH-ujiT96kQxYS37jkXawgOEgt8=gZO67swMnQoFfyKaJavy3LSDo_wFyhfINV24lO5kRTkL8rvJGSDLAnDDClA9=K2zVOboiCC8htkOoSfNhE2Na4KOb5XPFqPWvKPugbysi=TMdBnHugSalbYwrugqSTTo7fxcdNzJ7O23QexOREw9QaXmmxNRasqXSHtFBQH8DTbKluI9ZotP4cAO9fK4IE_gq_aFyH3xjzNR4z7ofzKP359mxdPo91c-43qls19w1NhjkOC=g4LIEcA4kOTyN_x9CZ6j-AgvYH4qBBVdZuZBFdIfAPHkRTvGUtHQkmrehJIbfJ63dFJcVoIQDioUREwjoD_vIQp_83AIQCE59XUTmgaDHNMKPnUFV4AIHcM_t9BsUC-7cWaSUuhDxu5g_QNkxON3kLIB5H94-DlGHiSe7SQ2QwCLuNdUeDo-M_VkBIzfUULESXxXOGCkEiovc5gs_4MEm3t6=fBgwWM3wZhnCkmqGOJ2-QrqX1GUKbbZsNPlLZ9bR6lJW8l3NSrEEVE2ZsYss9n-Pm=vtw5LCVQYAuIcESu7dESN-5zY1Ou_tEpepOr9A9tglsIcUjQRrvxsZ28suRNT6Dpe_f9_Ho3TyMtSjgoT5O3LHbsdrxoyLUPzrqMpALbjxvmjr2xi=66SbfNy6dBu65pFCDhh1u=H53sA1r-CY3Mr5SOisx_gJhBGg=CYCJXofOYplk7a7mWBmmLfnxdZ2MI_ypxbkShlMIMzMPN1O7M1Mnkb-tAmu5KtCNa-c7yhwgQjcFd2G7zG96Z-6uD2qvVDeURh6mawdxJqb9_Hns9_DrQv4fn1_j49SnL4o5-Hr14S9ksdK4xjfpMZusw3kzB5G5C1U4rctSREFupxbdm1lKxpzZvhVMEUf4kh6yJMuyBaz5tIiTqGo76SYl6sEtDqc96aeqrlv9zj9pIvE9igR4m-yYBKmznCrm2=SFlRCRlNE9Fu7Rf44x8-SXURy7=eDE24OvVY=Sz=tPL8oERSfjMZ1kqK-mpo3sqaMjrlnYouTEsuDf_q1xsfyRTxlyswvrEsgy55IkfjZK3W3n1Fdxc5mFuIUcruTFnBv12_pjcmMxNaLGk7e1LCVb7QszFJ3YMgqTE8CbbHNXA=kxOE9tvEmRvnCgJbXNDVxcFFMzW7x5DhyLqoo5PkvfsSipA7-yFojnjuvOxq7ty=hFPf5OexCYFP9DQsaZEE5Ie1DjtY8MTKWoZO5IGqwUx5HFaPw629k2ByimpGW2OzqCGVf7IHDdlFQ92qY7Lcslp77qfyScqbdP_iaiKaQ5pVEvGbxN8HpVCk3_i6JLHNVkzKL98lTxpGP63EVyHgPTvGsD3bnjSoogOfjonjp7OozEuo1fo5COncbRi1THkedPyBqkRG2hEBG2cd4=gR2-KOqIlzLmw=yBPfppXNSCedCQECNOfQmsvdRVJ-Vrtatd99ModI44t5lxG4U6mv=lalete5cRxZfnNNv76A8uCMwxn1KJb1E=RVtSW8XFhV72o=nreK48Ku99SPP8VM6rxujp4QLRM3MjEDR9SzElA725wxoIRI-Xw1Cla32p-QK3-UoSzRHgPRjHYLDakHYRmn7HfzlU"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Referer"] = "https://www.nordstrom.com/browse/women/clothing?breadcrumb=Home%2FWomen%2FClothing&origin=topnav&page=6"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "Ad34bsY56=AFqXuVF8AQAA7YgFtsCjJHsAxseCKMQALnY7FPiEc7L5dMMAL43UshQ8Y3wS|1|1|4b4cfbc99ec7e552156c46280fa90b9740f8ad4c; internationalshippref=preferredcountry=US&preferredcurrency=USD&preferredcountryname=United%20States; no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=a75770cc96f1492c97310524c7bd116b&USERNAME=; nui=firstVisit=2021-10-05T18%3A31%3A31.521Z&geoLocation=&isModified=false&lme=false; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhNzU3NzBjYzk2ZjE0OTJjOTczMTA1MjRjN2JkMTE2YiIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5NDg5OTE0OTEsInJlZnJlc2giOjE2MzM0NzMwOTEsImp0aSI6Ijg2YzA5ZGQ3LWNjY2EtNGE3MC04N2Q0LWZlODVhMDQyN2JmMiIsImlhdCI6MTYzMzQ1ODY5MX0.HXJc945CkPaT_aYv64AGXKK_gi_RUxZ8IQGkhfFUk9Fygy1agea_arS-t6nXYvT5XJROGuhA2SnfKjtEBWdFoEQ_tpuKgbb832vdE0Buiq5SXP6DwvbEQm_1Jcp81jaTKAmCz_pCdjT3W5g4CR-hJKss7TSl6_m32JguxUrIEG4MzDOBxp_-cdFh6hSOVd7gonUzJE7uv8ituIE_FhVEe9rQrQ2mSvJRXioIEGy2AmuxAQ10qS_r1umwp-FkWMDa5BiDYpcLyiNVqcDYalA8Pyf7WTrt97texWNAYD_YoQLJw8aoH3SulU3h7jKqgwM-lMxpkfMjK6u1Y-8QJAGQQQ; experiments=ExperimentId=c3dbaf83-88c9-4213-bbd2-5f60e820ce11; Bd34bsY56=AOxLGHp8AQAAm9pSPS-mD4DXyLmknQ-0RwgVWWxw12XYa-uw0hJAI3P-ZjDA; forterToken=8d87d40cc711483f8d181f8fbca70836_1634135614653__UDF43_6; _gcl_au=1.1.886446307.1633458711; storemode=version=4&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; storeprefs=|100|||2021-10-13T14:33:40.957Z; _ga_XWLT9WQ1YB=GS1.1.1634135239.8.1.1634135977.6; _ga=GA1.2.160709569.1633458715; _imp_apg_r_=%7B%22c%22%3A%22VEZtVG1zQlp0Y2tJWHJBSQ%3D%3D5tLQfH7up7FavOe2XQSvIcclqiSRLOm3yGcyZsmjXmOUAN9MbDrSBzif-jvtDo3mS2w-f_TZmxt0jvbBE4yKZqAXAOGydQ%3D%3D%22%2C%22dc%22%3A1%2C%22mf%22%3A0%2C%22_fr%22%3A20000%2C%22fr%22%3A%22rnqcZAStgBO6VMy1bD-8Pw%3D%3DhI_uIxBwFD4RAkQOTWDQcFiZHakSE4j1NCUWb6_9a8WTHEFzkCfobbR0o25YURTPIUr-IDjQJuXvJ7yonQ%3D%3D%22%7D; ftr_ncd=6; rkglsid=h-b28156d49e8add029fe1010017c51b9f_t-1634135981; _pin_unauth=dWlkPVltUTVNekEzWmpndFl6RmpOQzAwTkRRMkxUZ3dPR1l0TlRobU1UY3lZakJoWlRjeQ; _fbp=fb.1.1633458722311.522931396; _gid=GA1.2.477122038.1634117100; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0&; usersession=CookieDomain=nordstrom.com&SessionId=c044e30a-e023-4c33-b24c-572857dcbc44; _4c_mc_=a7de90bf-1fa8-4294-b345-b42705ab019f; rfx-forex-rate=currencyCode=USD&exchangeRate=1&quoteId=0; __ts_xfdF3__=296609933; _uetsid=6fc6a6502c0711ec98f8afca42b24d62; _uetvid=84ad9a60260a11ecb9d71bab6bf0bf68; _gat_UA-107105548-1=1"
    headers["TE"] = "trailers"


    resp = s.get(url, headers=headers)

    
    if resp.status_code == 403:
        i=i-1
    else:
        print(resp.status_code)
        i=i+1
