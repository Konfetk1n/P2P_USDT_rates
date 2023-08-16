import requests


class API:
    def __init__(self):
        pass

    def request(self):
        pass

    def get(self):
        ...

    def post(self, url: str, headers=None, json=None, params=None):
        try:
            response = requests.post(url=url, headers=headers, json=json, params=params)
        except ConnectionError as e:
            print("Connection error", e)
        else:
            if response.status_code == 200:
                return response
            else:
                print("Status code:", response.status_code, response.text, response.json())

