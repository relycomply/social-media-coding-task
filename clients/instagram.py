from clients import SocialMediaClient
import requests


class InstagramClient(SocialMediaClient):

    def __init__(self):
        self.base_url = "https://takehome.io/instagram"
        self.headers = {}

    def _get(self, endpoint='', params={}):
        try:
            url = f"{self.base_url}{endpoint}"
            res = requests.get(url,
                    params=params,
                    headers=self.headers)
            return res.json()
        except requests.exceptions.JSONDecodeError:
            return [{ 'post': res.text }] if res.text else []
        
    def get_feed(self):
        return self._get()


client = InstagramClient()
