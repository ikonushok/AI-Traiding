# Библиоетки backtesting
from backtesting import Backtest, Strategy

class Long_Strategy(Strategy):
    
    def init(self):
      self.signal = self.I(lambda x: x, self.data.Signal, name='Signal') 
        
    def next(self):
      # торгуем по крайней цене закрытия
      price = self.data.Close[-1]

      if (self.position.is_long and
          self.signal == -1):
        self.position.close()

      if (self.position.size == 0 and
          self.signal == 1):
          self.buy()
          #self.buy(sl=0.8 * price)
          self.position.entry_price = price
