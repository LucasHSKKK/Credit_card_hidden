credit_card = ["123345566788656"]


def credit():
    credit_card = input(f"which is your credit card number: ")
    credit_number = credit_card
    desired_length = 16
    check_string_length(credit_number, desired_length)


def check_string_length(my_string, desired_length):
    if len(my_string) == desired_length:
        print("\nconfirm your card")
        hidden()

    else:
        print("that isn't a valid card. try again.")
        credit()


def hidden():
    last_four_numbers = credit_card[0][-4:]
    print(f"*****{str(last_four_numbers)}")


credit()
