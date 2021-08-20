from commons.env import Env
from clients.checkout.config import CheckoutConfig
from dataclasses import dataclass
import requests


@dataclass
class AdminFinalizationResp:
    finalized: list[str]
    failed: list[str]


class CheckoutClient:
    def __init__(self, env: Env, access_token: str) -> None:
        self._config = CheckoutConfig(env)
        self._access_token = access_token

    def finalize_fully_funded_as_admin(self, checkout_uuids: list[str]) -> AdminFinalizationResp:
        endpoint = "/admin/checkouts/finalize"
        full_path = self._config.get_base_url() + endpoint
        headers = {'Authorization': 'Bearer ' + self._access_token}

        resp = requests.post(full_path, json=checkout_uuids, headers=headers)
        if resp.status_code == 200:
            r = resp.json()
            return AdminFinalizationResp(r['finalized'], r['failed'])
        else:
            print("Error talking to checkout!")
            return None
