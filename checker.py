def checker(password):
    dgts = False
    upper_case = False
    lower_case = False

    while len(password) < 5 or len(password) > 10:
        if len(password) > 10: print("Your password is too long!")
        elif len(password) < 5: print("Your password is too short!")

    for x in range(0, len(password)):
        if ord(password[x]) in range(48, 59):
            dgts = True
        if ord(password[x]) in range(97, 124):
            lower_case = True
        if ord(password[x]) in range(65, 92):
            upper_case = True

    if "_" in password or "-" in password:
        print("You cannot have '_' or '-' in your password!")

    elif dgts and upper_case and lower_case:
        print("You sir, have a very strong password.")
    else:
        print("You sir, do not have a very strong password.")

check = checker("Your password here")