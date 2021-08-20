from commons.env import Env


class PurchaseConfig:
    def __init__(self, env: Env) -> None:
        self._env = env

    def get_base_url(self) -> str:
        if self._env == Env.TEST:
            return "https://purchase.izettletest.com"
        elif self._env == Env.PROD:
            return "https://purchase.izettle.com"
        else:
            return None