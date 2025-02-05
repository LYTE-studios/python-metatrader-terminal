import MetaTrader5 as mt5


class MT5Client:
    # def __init__(self):

    @staticmethod
    def connect(account, password, server):
        # if not mt5.initialize(path="C:/Program Files/MetaTrader 5/terminal64.exe"):
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            return False

        authorized = mt5.login(account, password=password, server=server)
        if authorized:
            # display trading account data 'as is'
            print(mt5.account_info())
        else:
            print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
            return False
        return True

    @staticmethod
    def get_orders(symbol=None, group=None):
        try:
            if symbol:
                orders = mt5.orders_get(symbol=symbol)
            elif group:
                orders = mt5.orders_get(group=group)
            else:
                orders = mt5.orders_get()

            return orders
        except Exception as e:
            print("Error getting orders: ", e)
            return

    @staticmethod
    def shutdown():
        mt5.shutdown()
