from abc import ABC, abstractmethod


class SocialMediaClient(ABC):

    @abstractmethod
    def _get(self, endpoint='', params={}):
        pass
    
    @abstractmethod
    def get_feed(self):
        pass
