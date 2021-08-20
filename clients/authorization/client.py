from commons.env import Env
from clients.authorization.config import AuthConfig
import requests


class AuthorizationClient:
    def __init__(self, env: Env) -> None:
        self._config = AuthConfig(env)

    def generate_auth_token(self) -> str:
        endpoint = "/token"
        full_path = self._config.get_base_url() + endpoint
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self._config.get_auth_credential().clientId,
            'client_secret': self._config.get_auth_credential().secret
        }
        resp = requests.post(full_path, data=payload)
        if resp.status_code == 200:
            return resp.json()["access_token"]
        else:
            print("Error talking to auth")
            return None
