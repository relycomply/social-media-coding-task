from flask import Flask
import requests
import json
from threading import Thread

def get_social_media_activity():
    # TODO: your code here
    instagram_response = requests.get("https://takehome.io/instagram")
    facebook_response = requests.get("https://takehome.io/facebook")
    twitter_response = requests.get("https://takehome.io/twitter")

    instagram_data = json.loads(instagram_response.text)
    facebook_data = json.loads(facebook_response.text)
    twitter_data = json.loads(twitter_response.text)

    json_response = {"instagram": instagram_data, "facebook": facebook_data, "twitter": twitter_data}

    return json_response

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/")
    def social_network_activity():
        # TODO: your code here
        json_response = get_social_media_activity()
        return json_response

    app.run()
