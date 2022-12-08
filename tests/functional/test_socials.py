from tests.functional import client
import mock

"""
    TODO: Mock api requests
"""

values = [{'key': 'value'}]

@mock.patch('resources.socials.fb_client.get_feed', return_value=values)
@mock.patch('resources.socials.insta_client.get_feed', return_value=values)
@mock.patch('resources.socials.ttw_client.get_feed', return_value=values)
def test_social_network_activity(social_client1, social_client2, social_client3, client):
    social_activity = client.get('/')
    assert social_activity.status_code == 200
    activities = social_activity.json

    for activity in activities:
        assert activities[activity] == 1

