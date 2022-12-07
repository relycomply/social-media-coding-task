import threading
from typing import Any
from clients import SocialMediaClient

from clients.facebook import client as fb_client
from clients.instagram import client as insta_client
from clients.twitter import client as ttw_client


class GetSocialNetworkActivity:

    post_count = {}

    @classmethod
    def add_posts(cls, social_client: SocialMediaClient, name:str):
        cls.post_count[name] = len(social_client.get_feed())

    def __call__(self, *args: Any, **kwds: Any) -> Any:

        threads = [threading.Thread(target=self.add_posts, args=(fb_client, "facebook")),
                    threading.Thread(target=self.add_posts, args=(insta_client, "instagram")),
                    threading.Thread(target=self.add_posts, args=(ttw_client, "twitter"))]

        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        

        return self.post_count


get_social_network_activity = GetSocialNetworkActivity()
