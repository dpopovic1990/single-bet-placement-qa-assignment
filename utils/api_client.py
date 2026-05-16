import requests

from utils.config import API_BASE_URL, USER_ID


class ApiClient:

    def place_bet_without_user_id(self, payload):
        return requests.post(
            f"{API_BASE_URL}/place-bet",
            json=payload,
        )

    def place_bet(self, payload):
        headers = {
            "x-user-id": USER_ID,
        }

        return requests.post(
            f"{API_BASE_URL}/place-bet",
            headers=headers,
            json=payload,
        )