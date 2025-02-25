import MetaTrader5 as mt5
from datetime import datetime


class MT5Client:
    @staticmethod
    def connect(account, password, server):
        try:
            path = "C:/Program Files/MetaTrader 5/terminal64.exe"
            if not mt5.initialize(path=path, login=int(account), password=password, server=server, portable=True):
                error_code = mt5.last_error()
                print("initialize() failed, error code =", error_code)
                mt5.shutdown()
                return {"status": False, "error_code": str(error_code)}

            authorized = mt5.login(int(account), password=password, server=server)
            if authorized:
                account_info = mt5.account_info()
                return {"status": True, "account_info": account_info}
            else:
                error_code = mt5.last_error()
                print(
                    "failed to connect at account #{}, error code: {}".format(
                        account, error_code
                    )
                )
                return {"status": False, "error_code": str(error_code)}
        except Exception as e:
            print("Error connecting to MT5: ", e)
            return {"status": False, "error_code": str(e)}

    @staticmethod
    def get_orders(symbol=None, date_from=None, date_to=None, group="GROUP"):
        try:
            if symbol:
                orders = mt5.orders_get(symbol=symbol)
            elif group:
                orders = mt5.orders_get(group=group)
            else:
                orders = mt5.orders_get(symbol="SYMBOL")

            orders_dict = [order._asdict() for order in orders] if orders else []
            if date_from and date_to:
                date_from = datetime.strptime(date_from, "%Y-%m-%d")
                date_to = datetime.strptime(date_to, "%Y-%m-%d")
                if group is None:
                    orders = mt5.history_deals_get(date_from, date_to)
                else:
                    orders = mt5.history_deals_get(date_from, date_to, group=group)
            else:
                date_from = datetime.strptime("2000-01-01", "%Y-%m-%d")
                date_to = datetime.today()
                if group is None:
                    orders = mt5.history_deals_get(date_from, date_to)
                else:
                    orders = mt5.history_deals_get(date_from, date_to, group=group)
            history_dict = [order._asdict() for order in orders] if orders else []
            merged_orders = orders_dict + history_dict
            return merged_orders
        except Exception as e:
            print("Error getting orders: ", e)
            return []

    @staticmethod
    def shutdown():
        mt5.shutdown()
