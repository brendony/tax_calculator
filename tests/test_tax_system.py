import unittest
from hypothesis import given, strategies

from controller.tax_system import TaxSystem


# I'm using hypothesis for Property Based testing
# so that library will generate lots of cases every time I run it
# which will help find corner cases etc.
class TestTaxSystem(unittest.TestCase):
    known_fy_values = ['2020-2021', '2021-2022']

    def test_known_fy(self):
        for fy in TestTaxSystem.known_fy_values:
            self.assertEqual(len(TaxSystem.get_brackets_for_year(fy)), 5)

    @given(strategies.text())
    def test_fy(self, fy):
        if fy not in TestTaxSystem.known_fy_values:
            self.assertEqual(len(TaxSystem.get_brackets_for_year(fy)), 0)

    def test_coding_exercise_example(self):
        self.assertEqual(TaxSystem.calculate_tax('2020-2021', 96200), 21732)

    def test_unknown_year(self):
        with self.assertRaises(Exception):
            TaxSystem.calculate_tax('bloop', 45000)

    @given(strategies.integers(),
           strategies.one_of(
               strategies.just('2020-2021'),
               strategies.just('2021-2022')
           ))
    def test_values(self, income, fy):
        # Apologies, I'm just going to reimplement things here, which is obviously not ideal
        expectedValue = 0 if income < 18200 else \
            0.19 * (income - 18200) if income < 45000 else \
                5092 + 0.3 * (income - 45000) if income < 120000 else \
                    29467 + 0.37 * (income - 120000) if income < 180000 else \
                        51667 + 0.45 * (income - 180000)

        self.assertEqual(
            TaxSystem.calculate_tax(fy, income),
            expectedValue
        )


if __name__ == '__main__':
    unittest.main()
