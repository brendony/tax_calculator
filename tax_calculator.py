import locale
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select, Input, Button, Label
from textual.containers import HorizontalGroup

from controller.tax_system import TaxSystem
from model.tax_rates import getSupportedFinancialYears


class TaxCalculator(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(
            "Please select the financial year and enter your income for that year."
        )
        yield Select(
            id="fy",
            options=[(fy, fy) for fy in getSupportedFinancialYears()],
            prompt="Select FY",
        )
        with HorizontalGroup():
            yield Label("$")
            yield Input(placeholder="Enter your income", type="integer", id="income")
        yield Button("Calculate tax", id="calculate", disabled=True)
        yield Label("", id="tax")

    @on(Select.Changed)
    def on_select(self, event: Select.Changed) -> None:
        self.query_one("#tax", Label).update("")
        if event.value and self.query_one("#income", Input).value:
            self.query_one("#calculate", Button).disabled = False
        else:
            self.query_one("#calculate", Button).disabled = True

    @on(Input.Changed)
    def on_text_changed(self, event: Input.Changed) -> None:
        self.query_one("#tax", Label).update("")
        if event.value and self.query_one("#fy", Select).value != Select.BLANK:
            self.query_one("#calculate", Button).disabled = False
        else:
            self.query_one("#calculate", Button).disabled = True

    def on_button_pressed(self, event: Button.Pressed) -> None:
        fy = self.query_one(Select).value
        income = int(self.query_one(Input).value)
        tax = TaxSystem.calculate_tax(fy, income)
        self.query_one("#tax", Label).update(
            f"The estimated tax on your taxable income is: {locale.currency(tax, grouping=True)}"
        )


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "en_AU.UTF-8")
    app = TaxCalculator()
    app.run()
