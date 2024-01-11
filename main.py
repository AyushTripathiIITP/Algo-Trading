from AlgorithmImports import *
from alpha import PriceActionAlpha
from Risk.MaximumDrawdownPercentPerSecurity import MaximumDrawdownPercentPerSecurity

# BTCUSD
class DualThrustAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 1, 1)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)
        self.SetBrokerageModel(BrokerageName.GDAX, AccountType.Cash)

        symbol = self.AddCrypto("BTCUSD", Resolution.Minute).Symbol

        self.AddAlpha(PriceActionAlpha(self, symbol))
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel(lambda time: None))
        self.SetExecution(ImmediateExecutionModel())
        #Add the Maximum Portfolio Drawdown Model with a 8% maximum drawdown and a trailing mode
        self.AddRiskManagement(MaximumDrawdownPercentPerSecurity(0.08))