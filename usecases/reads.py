from commons.env import Env
from clients.authorization.client import AuthorizationClient
from clients.purchase.client import PurchaseClient


class Reads:
    def __init__(self, env: Env):
        self._env = env

    def get_purchase_as_admin(self, purchase_uuid: str) -> str:
        auth_client = AuthorizationClient(self._env)
        access_token = auth_client.generate_auth_token()
        if access_token is None:
            print("Failed getting access token.")
            return

        return PurchaseClient(self._env, access_token).get_purchase_as_admin(purchase_uuid)
