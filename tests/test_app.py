from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_them_from_activity():
    activity_name = "Chess Club"
    email = "student@example.com"

    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    unregister_response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    assert email not in activities_response.json()[activity_name]["participants"]
