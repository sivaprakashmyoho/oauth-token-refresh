
from fastapi import FastAPI, HTTPException, Header
from datetime import datetime, timedelta, timezone
import secrets

app = FastAPI()

# Client credentials
CLIENT_ID = "my-client-id"
CLIENT_SECRET = "my-client-secret"

# Store generated tokens
tokens = {}


@app.post("/token")
def generate_token(client_id: str, client_secret: str):

    # Verify client credentials
    if client_id != CLIENT_ID or client_secret != CLIENT_SECRET:
        raise HTTPException(
            status_code=401,
            detail="Invalid client credentials"
        )

    # Generate access token
    access_token = secrets.token_hex(16)

    # Token expires after 30 seconds
    expiry_time = datetime.now(timezone.utc) + timedelta(seconds=30)

    tokens[access_token] = expiry_time

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 30
    }


@app.get("/data")
def get_data(authorization: str = Header(None)):

    # Check authorization header
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Missing or invalid token"
        )

    access_token = authorization.split(" ", 1)[1]

    # Check whether token exists
    if access_token not in tokens:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    # Check token expiry
    if datetime.now(timezone.utc) >= tokens[access_token]:
        del tokens[access_token]

        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    return {
        "message": "API access successful",
        "data": [
            {"id": 1, "name": "Python"},
            {"id": 2, "name": "SQL"},
            {"id": 3, "name": "FastAPI"}
        ]
    }
