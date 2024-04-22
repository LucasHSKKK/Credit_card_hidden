credit_card = ["123345566788656"]


# this fuction receive the card's number
def credit():
    credit_card = input(f"which is your credit card number: ")
    credit_number = credit_card
    desired_length = 16
    check_string_length(credit_number, desired_length)


# this function check out if the number received has is enough.
def check_string_length(my_string, desired_length):
    if len(my_string) == desired_length:
        print("\nconfirm your card:")
        hidden()
        Validation()
    else:
        print("\nthat isn't a valid card. try again.")
        credit()


# this fuction is to valid if the person wants to save the card
def Validation():
    confirmation = input(f"\n do you want to save: ")
    if confirmation.lower() == "yes":
        print("\nCard saved.")
    elif confirmation.lower() == "no":
        print("\nCard deleted.")
        del credit_card[0]
    else:
        print(f"\n command invalid. Try it again.")
        print(f"it's only valid YES or NO")
        Validation()


# this function shows only the four last card's number
def hidden():
    last_four_numbers = credit_card[0][-4:]
    print(f"*****{str(last_four_numbers)}")


credit()
