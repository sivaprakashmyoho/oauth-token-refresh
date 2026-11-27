
# OAuth 2.0 Client Credentials and Token Refresh

## Project Overview

This project demonstrates OAuth 2.0 Client Credentials authentication using Python and FastAPI.

It implements a mock authentication server that generates access tokens valid for 30 seconds.

The client automatically refreshes expired tokens when it receives HTTP 401 and retries the API request once.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Requests

## Features

- Client Credentials authentication
- Access token generation
- 30-second token expiration
- Protected GET /data endpoint
- Automatic token refresh
- HTTP 401 error handling
- Retry API request once
- Masked token printing

## Project Structure

oauth-token-refresh/
- auth_server.py
- client.py
- requirements.txt
- README.md
- .gitignore

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Start authentication server

uvicorn auth_server:app --reload

### 3. Run client

python client.py

## Expected Output

Token acquired: c945****
GET /data -> 200

GET /data -> 200

GET /data -> 401, refreshing token
Token acquired: c111****
GET /data -> 200

GET /data -> 200

## Concepts Covered

- OAuth 2.0 Client Credentials Flow
- Token Expiration
- HTTP Authentication
- 401 Unauthorized
- Automatic Token Refresh
- API Retry Mechanism
