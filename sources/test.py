import json



from benedict import benedict
data=test['results']['filterCates']['children']
for cat in data:
    cat_id = cat['cat_id']
d = benedict(data)
cats =d.search('cat_id', in_keys=True, exact=True, case_sensitive=False)
print (cats)




"""from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
import json
# Go to the Google home page
driver.get('https://www.shein.com/MOTF-PREMIUM-VISCOSE-MIDI-SHIRT-DRESS-p-2912954-cat-1727.html?scici=navbar_WomenHomePage~~tab01navbar04~~4~~webLink~~~~0')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        try :
            data= json.loads(request.response.body)
            if "more_goods_imgs" in data.keys():

                print(
                request.url

                )
        except Exception:
            pass"""