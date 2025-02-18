import MetaTrader5 as mt5


class MT5Client:
    @staticmethod
    def connect(account, password, server):
        if not mt5.initialize():
            error_code = mt5.last_error()
            print("initialize() failed, error code =", error_code)
            return {"status": False, "error_code": str(error_code)}

        authorized = mt5.login(int(account), password=password, server=server)
        if authorized:
            account_info = mt5.account_info()
            print(account_info)
            return {"status": True, "account_info": account_info}
        else:
            error_code = mt5.last_error()
            print("failed to connect at account #{}, error code: {}".format(account, error_code))
            return {"status": False, "error_code": str(error_code)}

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
