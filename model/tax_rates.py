# The tax rate information might come as a data file (json, csv, even excel) but for now I'm just going to use
# python to simplify things for myself.

from typing import Optional

from attr import dataclass


@dataclass
class TaxBracket:
    # A tax bracket can look like this:
    # For taxable income in the range
    # $45,001 – $120,000
    # The tax rate is defined as
    # $5,092 plus 32.5c for each $1 over $45,000
    #
    # In this case:
    # - maxIncome is 120000 (we won't worry about min of the range, that will be taken
    # by a lower bracket
    # - baseAmount is 5092
    # - centsPerDollar is 32.5
    # - overAmount is 45000

    max_income: Optional[int]
    base_amount: float
    cents_per_dollar: float
    over_amount: int


historical_tax_rates: dict[str, list[TaxBracket]] = {
    '2020-2021': [
        TaxBracket(max_income=18200, base_amount=0, cents_per_dollar=0.0, over_amount=0),
        TaxBracket(max_income=45000, base_amount=0, cents_per_dollar=19, over_amount=18200),
        TaxBracket(max_income=120000, base_amount=5092, cents_per_dollar=32.5, over_amount=45000),
        TaxBracket(max_income=180000, base_amount=29467, cents_per_dollar=37, over_amount=120000),
        TaxBracket(max_income=None, base_amount=51667, cents_per_dollar=45, over_amount=180000)
    ],
    '2021-2022': [  # NB: this is the same as 2020-2021, but I'm leaving them here as it is explicit
        TaxBracket(max_income=18200, base_amount=0, cents_per_dollar=0.0, over_amount=0),
        TaxBracket(max_income=45000, base_amount=0, cents_per_dollar=19, over_amount=18200),
        TaxBracket(max_income=120000, base_amount=5092, cents_per_dollar=32.5, over_amount=45000),
        TaxBracket(max_income=180000, base_amount=29467, cents_per_dollar=37, over_amount=120000),
        TaxBracket(max_income=None, base_amount=51667, cents_per_dollar=45, over_amount=180000)
    ]
}
