def main():
    # ask user to enter amount for meal in$##
    dollars = dollars_to_float(
        input("How much was the meal? "))

    # ask user to enter amount for tip in ##%
    percent = percent_to_float(
        input("What % would you like to tip? "))
    # do the math
    tip = float(dollars) * float(percent)/(100)

    dollars = float(dollars)

    percent = float(percent)

    print(f"meal  {dollars:.2f}")
    print(f"tip   {percent}")
    print(f"Leave ${tip:.2f}")


# def dollars_to_float
# remove $ sign
def dollars_to_float(d):
    return d.strip("$")


# percent_to_float
# remove percentage
def percent_to_float(p):
    return p.strip("%")


# def main():
main()
