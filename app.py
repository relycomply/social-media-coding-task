from flask import Flask

from resources.socials import get_social_network_activity

app = Flask(__name__)

@app.route("/")
def social_network_activity():
    # TODO: your code here
    json_response = get_social_network_activity()
    return json_response
