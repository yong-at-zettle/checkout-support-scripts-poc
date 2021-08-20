from commons.env import Env


class CheckoutConfig:
    def __init__(self, env: Env) -> None:
        self._env = env

    def get_base_url(self) -> str:
        if self._env == Env.TEST:
            return "https://checkout.izettletest.com"
        elif self._env == Env.PROD:
            return "https://checkout.izettle.com"
        else:
            return None
