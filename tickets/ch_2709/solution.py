from commons.io_helper import IoHelper
from commons.env import Env
from usecases.finalization import Finalization
import time


def solve():
    finalization = Finalization(Env.PROD)
    checkout_uuids = IoHelper.get_raw_lines("checkout_uuids_from_replica.txt")

    delta_uuids = []
    i = 0
    for checkout_uuid in checkout_uuids:
        if i != 0 and i % 50 == 0:
            print("Processing record upto:", i)
            finalization.finalize_fully_funded_as_admin(delta_uuids)
            delta_uuids = []
            time.sleep(5)

        delta_uuids.append(checkout_uuid)
        i += 1

    if len(delta_uuids) != 0:
        finalization.finalize_fully_funded_as_admin(delta_uuids)


if __name__ == "__main__":
    solve()
