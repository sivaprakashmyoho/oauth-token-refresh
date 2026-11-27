
import requests
import time

# API server URL
BASE_URL = "http://127.0.0.1:8000"

# Client credentials
CLIENT_ID = "my-client-id"
CLIENT_SECRET = "my-client-secret"

# Store access token
access_token = None


def get_token():
    global access_token

    response = requests.post(
        f"{BASE_URL}/token",
        params={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
    )

    response.raise_for_status()

    access_token = response.json()["access_token"]

    # Never print the complete token
    masked_token = access_token[:4] + "****"

    print(f"Token acquired: {masked_token}")

    return access_token


def call_api(url):
    global access_token

    # Get token if not available
    if access_token is None:
        get_token()

    # First API request
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # If token expired, refresh and retry once
    if response.status_code == 401:

        print("GET /data -> 401, refreshing token")

        get_token()

        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {access_token}"}
        )

    print(f"GET /data -> {response.status_code}")

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    # Run API calls for more than 30 seconds
    for i in range(4):

        print(f"\nAPI Request {i + 1}")

        data = call_api(f"{BASE_URL}/data")

        print("Response:", data)

        if i < 3:
            print("Waiting 15 seconds...")
            time.sleep(15)
