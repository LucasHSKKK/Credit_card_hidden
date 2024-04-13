credit_card = []


def credit():
    credit_number = credit_card
    desired_length = 16
    credit_card = input(f"which is your credit card number: ")
    check_string_length(credit_number, desired_length)


def check_string_length(my_string, desired_length):
    if len(my_string) == desired_length:
        print("\ncard saved")
    else:
        print("that isn't a valid card. try again.")
        credit()


def hidden():
    credit_card


credit()
