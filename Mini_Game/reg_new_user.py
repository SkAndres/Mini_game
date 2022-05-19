from conect import reg_new_user, check_log, user_data

# registration new user


# first name user
def first_name():
    name = input("Write your first name: ")
    check = len(name)
    if check >= 20:
        print("First name is too long! (MAXIMUM IS 20 CHARACTERS)")
        return first_name()
    
    elif check <= 20:
        name = name.split()
        print(f"Your name is {name[0]} ")
        return name


def nickname():
    user_name = input("Write your nickname: ")
    check = len(user_name)
    if check >= 20:
        print("First name is too long! (MAXIMUM IS 20 CHARACTERS)")
        return nickname()
    elif user_name in check_log():
        print("The same nickname already exists")
        return nickname()
    user_name = user_name.split()
    return user_name


def special_word():
    password_1 = input("Write your password: ")
    password_2 = input("Confirm your password: ")
    check = len(password_1)
    if check < 5:
        print("Repeat password.\n"
              "Your password is too short.\n"
              "Your password must contain at least 5 characters\n")
        return special_word()
    elif password_1 != password_2:
        print("passwords do not match please try again")
        return special_word()
    password_1 = password_1.split()
    print(password_1)
    return password_1


# Use a secret question(sec_que) for changing the password
# if the secret question is True pass would be changed
def secret_que():
    print("1) What is your mother's maiden name?\n"
          "2) What was your first pet?\n"
          "3) What was the model of your first car?\n"
          "4) In what city were you born?\n"
          "5) What was your father's middle name?\n"
          "6) What was your childhood nickname?\n")

    choose_que = input("Choose a secret question: ")
    if choose_que == "1":
        first_que = input("In what city were you born?\n"
                          "Your answer: ").split()
        id_que = "1".split()
        data_que = id_que + first_que
        return data_que

    elif choose_que == "2":
        sec_que = input("What was your first pet?\n"
                        "Your answer: ").split()
        id_que = "2".split()
        data_que = id_que + sec_que
        return data_que

    elif choose_que == "3":
        thi_que = input("What was the model of your first car?\n"
                        "Your answer: ").split()
        id_que = "3".split()
        data_que = id_que + thi_que
        return data_que

    elif choose_que == "4":
        fourth_que = input("In what city were you born?\n"
                           "Your answer: ").split()
        id_que = "4".split()
        data_que = id_que + fourth_que
        return data_que

    elif choose_que == "5":
        fifth_que = input("hat was your father's middle name?\n"
                          "Your answer: ").split()
        id_que = "5".split()
        data_que = id_que + fifth_que
        return data_que

    elif choose_que == "6":
        sixth_que = input("What was your childhood nickname?\n"
                          "Your answer: ").split()
        id_que = "6".split()
        data_que = id_que + sixth_que
        return data_que


def registration():
    name = first_name()
    user_name = nickname()
    password = special_word()
    secret_question = secret_que()
    values = name + user_name + password + secret_question
    reg_new_user(values=values)
    user_data(user_d=user_name)
