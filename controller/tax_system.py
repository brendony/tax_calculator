import math

from model.tax_rates import TaxBracket, historical_tax_rates


class TaxSystem:

    @staticmethod
    def calculate_tax(fy: str, income: int) -> float:
        # We should store these in decreasing order, but:
        # Because there are only 5 or six brackets per year, I'm going to sort them
        # to make sure things are correct
        brackets = sorted(TaxSystem.get_brackets_for_year(fy), key=lambda x: x.max_income or math.inf)
        if len(brackets) == 0:
            raise Exception(f'Unknown FY {fy}, must be one of {historical_tax_rates.keys()}')
        bracket = [bracket for bracket in brackets
                   if income < (bracket.max_income or math.inf)][0]
        return bracket.base_amount + bracket.cents_per_dollar / 100.0 * (int(income) - bracket.over_amount)

    @staticmethod
    def get_brackets_for_year(fy: str) -> list[TaxBracket]:
        return historical_tax_rates.get(fy, [])
