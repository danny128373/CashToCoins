dollarAmount = 11.16

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
piggyBank["quarters"] = int(dollarAmount / 0.25)
piggyBank["dimes"] = int((dollarAmount - piggyBank["quarters"] * .25) / .10)
piggyBank["nickels"] = int(round((dollarAmount -
                                  (piggyBank["quarters"] * .25 + piggyBank["dimes"] * .10)) * 100)/5)
piggyBank["pennies"] = int(round((dollarAmount - (piggyBank["quarters"] * .25 +
                                                  piggyBank["dimes"] * .10 + piggyBank["nickels"] * .05)) * 100))
print(piggyBank)
