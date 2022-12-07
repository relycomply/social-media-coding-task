from clients import SocialMediaClient
import requests

class FacebookClient(SocialMediaClient):

    def __init__(self):
        self.base_url = "https://takehome.io/facebook"
        self.headers = {"Content-Type": "application/json;"}

    def _get(self, endpoint='', params={}):
        try:
            url = f"{self.base_url}{endpoint}"
            res = requests.get(url,
                    params=params,
                    headers=self.headers)
            return res.json()
        except requests.exceptions.JSONDecodeError:
            return []
        
    def get_feed(self):
        return self._get()


client = FacebookClient()
