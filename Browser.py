import requests

url = 'https://www.nlb.gov.sg/'
r = requests.get(url)
# This will get the full page
print(r.text)

print("Status code:")
print("\t *", r.status_code)
if r.status_code == 200:
    print("OK")

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("************************************************")

headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
