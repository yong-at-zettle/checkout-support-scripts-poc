from commons.env import Env
from clients.purchase.config import PurchaseConfig
import requests


class PurchaseClient:
    def __init__(self, env: Env, access_token: str) -> None:
        self._config = PurchaseConfig(env)
        self._access_token = access_token

    def get_purchase_as_admin(self, purchase_uuid: str):
        endpoint = "/purchase/v2/" + purchase_uuid + "/system"
        full_path = self._config.get_base_url() + endpoint
        headers = {'Authorization': 'Bearer ' + self._access_token}

        resp = requests.get(full_path, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            print("Error talking to purchase with response code:", resp.status_code)
            return None
