from Washing_mode import WashingMode
from Resources import Resources
from Check_payment import CheckPayment

wash = WashingMode()
resource = Resources()
money = CheckPayment()

with_drying = False
on = True

while on:
    user_input = input(f"Washing machine is ready. Please, choose mode {wash.get_mode()}: ")
    if user_input == "off":
        on = False
    elif user_input in wash.get_mode():
        if resource.check_resources(user_input):
            drying = input("If you need drying? Enter 'yes' or 'not': ")
            if drying == "yes":
                with_drying = True
            wash.with_drying(with_drying, user_input)

            print("If it correct, please enter money.")
            deposit = float(input("How much money did you deposit?: "))
            if money.check_money(deposit, with_drying, user_input):
                print("Washing machine is working. Please wait...")
                resource.wash_process(user_input, with_drying)
                resource.waiting_process(user_input)
            else:
                print("Not enough money")
        else:
            print("Sorry, this washing machine mode does not available now. "
                  "Please choose another mode or another machine.")

    elif user_input == "report":
        resource.report()

    else:
        print("Please, enter correct mode.")
