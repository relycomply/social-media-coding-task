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
    #Return All Posts From All End Points
    @app.route("/")
    def social_network_activity():
        json_response = get_social_media_activity()
        return json_response
    
    @app.route("/api")
    def numeric_social_network_activity():
        # get the data
        json_response = get_social_media_activity()
        # return the number of posts for each network
        return {"instagram": len(json_response["instagram"]), "facebook": len(json_response["facebook"]), "twitter": len(json_response["twitter"])}

    app.run()
