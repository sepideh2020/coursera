import requests


def requestURL(baseurl, params={}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method='GET', url=baseurl, params=params)
    prepped = req.prepare()
    return prepped.url

# print(requestURL(some_base_url, some_params_dictionary))
# import requests
# dest_url = <some expr>
# d = <some dictionary>
# resp = requests.get(dest_url, params = d)
# print(resp.url)
# print(resp.text[:200])


test=requests.get("https://www.google.com/search",params={"tbm":"isch","q": "violins and guitars"})
print(test)
#
# d = {'q': '"violins and guitars"', 'tbm': 'isch'}
# results = requests.get("https://google.com/search", params=d)
# print(results.url)

print(requestURL("https://www.google.com/search",params={"tbm":"isch","q": "violins and guitars"}))