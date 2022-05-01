import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'a6d4ae1ffa20ba431683e262fc0ece2f'
redirect_uri = 'https://example.com/oauth' # APP에서 등록한 redirect_url
authorize_code = 'J4T8eXprWZ591ygd-BNEaDc7lP-cvGjJAT2MPOYgU45KoCskHfjsukuxgPrtLxEajUAZIgopcSEAAAGAWKCc2A' 
 
data = {
        'grant_type':'authorization_code',
        'client_id':rest_api_key,
        'redirect_uri':redirect_uri,
        'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens["access_token"])