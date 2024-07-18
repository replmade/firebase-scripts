import firebase_admin
from firebase_admin import credentials, auth
import requests


class Auth:

    def __init__(self):  
        self.base_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    def set_api_key(self, api_key):
        self.api_key = api_key
        self.auth_url = f"{self.base_url}?key={self.api_key}"

    def authenticate_user(self, email, password):
        if not self.api_key:
            raise ValueError("API Key is not set.")

        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        response = requests.post(self.auth_url, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            id_token = response_data.get("idToken")
            print("ID Token: ", id_token)
            self.id_token = id_token
            return id_token
        else:
            error_message = response_data.get("error", {}).get("message", "Unknown error occurred")
            print(f"Failed to authenticate. Error: {error_message}")
            return None
        
    def get_session_cookie(self, expires_in = 60 * 60 * 24 * 7):
        if not self.id_token:
            raise ValueError("ID Token is not set.")
        try:
            session_cookie = auth.create_session_cookie(self.id_token, expires_in=expires_in)
            print("Session Cookie: ", session_cookie)
            self.session_cookie = session_cookie
            return session_cookie
        except Exception as e:
            print(f"Failed to create session cookie. Error: {str(e)}")
            return None
        
    def auth_user(self):
        if not self.session_cookie:
            raise ValueError("Session Cookie is not set.")
        try:
            decoded_token = auth.verify_id_token(self.id_token)
            self.decoded_token = decoded_token
            return decoded_token
        except Exception as e:
            print(f"Failed to verify token. Error: {str(e)}")
            return None
    
    def get_user_by_uid(self, uid):
        try:
            user_record = auth.get_user(uid)
            return user_record
        except firebase_admin.auth.UserNotFoundError:
            print("User not found.")
        except Exception as e:
            print(f"Failed to get user. Error: {str(e)}")
            return None
        
    def create_custom_token(self, uid):
        try:
            custom_token = auth.create_custom_token(uid)
            self.custom_token = custom_token
            return custom_token
        except Exception as e:
            print(f"Failed to create custom token. Error: {str(e)}")
            return None