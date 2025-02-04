import MetaTrader5 as mt5

class MT5Client:
    def connect(self, account, password, server):
        if not mt5.initialize():
            return False
        return mt5.login(account, password, server)
    
    def get_trades(self):
        return mt5.positions_get()