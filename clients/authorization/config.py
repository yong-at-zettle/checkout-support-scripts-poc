from dataclasses import dataclass
from commons.env import Env


@dataclass
class AuthCredential:
    clientId: str
    secret: str


class AuthConfig:
    def __init__(self, env: Env) -> None:
        self._env = env

    def get_auth_credential(self) -> AuthCredential:
        if self._env == Env.TEST:
            return AuthCredential("110e4853-fc6c-4837-9df3-9bb310671ebc", "IZSEC2fec8911-81e7-4634-9c36-56795099bfd5")
        elif self._env == Env.PROD:
            return AuthCredential("your-prod-admin-client-id", "your-prod-admin-client-id") # <== replace me
        else:
            return None

    def get_base_url(self) -> str:
        if self._env == Env.TEST:
            return "https://oauth.izettletest.com"
        elif self._env == Env.PROD:
            return "https://oauth.izettle.com"
        else:
            return None
