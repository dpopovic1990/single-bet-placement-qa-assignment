import pytest

from utils.api_client import ApiClient


@pytest.mark.api
def test_place_bet_without_user_id_returns_401():
    """
    Chosen as the API automation test because it validates
    a high-risk authentication and authorization rule
    protecting the betting endpoint from unauthorized access.
    """

    api_client = ApiClient()

    payload = {
        "matchId": "premier-league-manutd-chelsea",
        "selection": "HOME",
        "stake": 5,
    }

    response = api_client.place_bet_without_user_id(
        payload
    )

    response_body = response.json()

    assert response.status_code == 401
    assert response_body["error"] == "missing_user_id"