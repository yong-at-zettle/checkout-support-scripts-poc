from commons.env import Env
from clients.authorization.client import AuthorizationClient
from clients.checkout.client import CheckoutClient


class Finalization:
    def __init__(self, env: Env):
        self._env = env

    def finalize_fully_funded_as_admin(self, checkout_uuids: list[str]):
        auth_client = AuthorizationClient(self._env)
        access_token = auth_client.generate_auth_token()
        if access_token is None:
            print("Failed finalizing  access token.")
            return

        resp = CheckoutClient(
            self._env, access_token).finalize_fully_funded_as_admin(checkout_uuids)
        if len(resp.failed) != 0:
            print("Failed finalizing checkouts count:", len(
                resp.failed), ", they are:", resp.failed)

        return resp
