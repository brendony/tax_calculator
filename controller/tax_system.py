import math

from model.tax_rates import TaxBracket, historical_tax_rates, getSupportedFinancialYears


class TaxSystem:

    @staticmethod
    def calculate_tax(fy: str, income: int) -> float:
        if income < 0:
            return 0
        brackets = TaxSystem.get_brackets_for_year(fy)
        if len(brackets) == 0:
            raise Exception(f'Unknown FY {fy}, must be one of {getSupportedFinancialYears()}')
        bracket = next(bracket for bracket in brackets
                       if bracket.min_income <= income <= (bracket.max_income or math.inf))
        return bracket.base_amount + bracket.cents_per_dollar / 100.0 * (int(income) - bracket.over_amount)

    @staticmethod
    def get_brackets_for_year(fy: str) -> list[TaxBracket]:
        return historical_tax_rates.get(fy, [])
