from usecases.reads import Reads
from commons.env import Env
from commons.io_helper import IoHelper


def run_example():
    print("Run me to try out calls")
    purchase = Reads(Env.TEST).get_purchase_as_admin(
        "3899d056-01bd-11ec-b407-03c0c1cf3ebd")
    IoHelper.print_pretty_json(purchase)


if __name__ == "__main__":
    run_example()
