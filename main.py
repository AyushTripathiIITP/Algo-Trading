from AlgorithmImports import *
from alpha import PriceActionAlpha

# BTCUSD Long Only Dual Thrust Algorithm 
class DualThrustAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2022, 1, 31)
        self.SetCash(100000)
        self.SetBrokerageModel(BrokerageName.GDAX, AccountType.Cash)

        symbol = self.AddCrypto("BTCUSD", Resolution.Minute).Symbol

        self.AddAlpha(PriceActionAlpha(self, symbol))
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel(lambda time: None))
        self.SetExecution(ImmediateExecutionModel())