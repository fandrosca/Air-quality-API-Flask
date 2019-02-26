import requests

categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

my_latitude = '51.52369'
my_longitude = '-0.0395857'
my_date = '2018-11'

resp = requests.get(categories_url_template.format(date = my_date))
crimes = resp.json()

if resp.ok:
    categories_json = resp.json()
else:
    print(resp.reason)

categories = {categ["url"]:categ["name"] for categ in categories_json}

crime_category_stats = dict.fromkeys(categories.keys(), 0)
crime_category_stats.pop("all-crime")


for crime in crimes:

    crime_category_stats[crime["category"]] += 1

print(crime_category_stats)
