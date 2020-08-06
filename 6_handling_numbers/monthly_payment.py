#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

def calculate_monthly_payment(loan_amount, yearly_interest_rate, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate monthly payment
    monthly_payment = loan_amount * monthly_interest_rate / \
                      (1 - 1 / (1 + monthly_interest_rate) ** months)
    
    return monthly_payment

def main():
    print("Monthly Payment Calculator")
    print()
    
    choice = "y"
    while choice.lower() == "y":
        print("DATA ENTRY")
        loan_amount = Decimal(input("Loan amount:          "))
        interest_rate = Decimal(input("Yearly interest rate: "))
        years = int(input("Years:                "))
        print()

        # quantize the entries
        loan_amount = loan_amount.quantize(Decimal("1.12"))
        interest_rate = interest_rate.quantize(Decimal("1.1"))

        # calculate and quantize the results
        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, years)
        monthly_payment = monthly_payment.quantize(Decimal("1.12"))

        print("FORMATTED RESULTS")
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:22} {:>16}"
        print(line.format("Loan amount:",
            lc.currency(loan_amount, grouping=True)))
        print(line.format("Yearly interest rate:",
            str(interest_rate) + "%"))
        print(line.format("Number of years:",
            str(years)))
        print(line.format("Monthly payment:",
            lc.currency(monthly_payment, grouping=True)), "\n")

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
