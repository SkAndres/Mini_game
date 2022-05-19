from mini_game import Start
from reg_new_user import registration
from conect import check_log, gm_score, check_bs_sc, get_que_id, ans_check, change_pw


def authorization():
    print("If you have already registered pick: 1\n"
          "If you haven't registered pick: 2\n")
    auth = input("Write your choice: ")
    if auth == "1":
        nickname = input("Your nickname: ")
        password = input("password: ")
        # use check_log to check if the nickname has already been registered
        if nickname not in check_log():
            print("Fail, check the correct username")
            return authorization()
        elif (nickname, password) not in check_log().items():
            print("Check password and nickname "
                  "pick 1 to try again or pick 2 to change the password")
            change_pas = input(">")
            # use for a new try
            if change_pas == "1":
                return authorization()
            # use 2 for changing the password
            elif change_pas == "2":
                # looking for id in database
                for quest_id in get_que_id(nickname):
                    quest_id = int(quest_id[0])
                    # looking for id equal quest_id
                    if quest_id == "1":
                        print("What is your mother's maiden name?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer
                    elif quest_id == "2":
                        print("What was your first pet?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer
                    elif quest_id == "3":
                        print("What was the model of your first car?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer
                    elif quest_id == "4":
                        print("In what city were you born?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer
                    elif quest_id == "5":
                        print("What was your father's middle name?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer
                    elif quest_id == "6":
                        print("What was your childhood nickname?")
                        answer = input("> ")
                        # looking for an answer in database if the answer is the TRUE user can change his password-
                        for ans_q in ans_check(nickname):
                            ans_q = str(ans_q)
                            if answer in ans_q:
                                # checking correctness the new password
                                new_pass1 = input("New password: ")
                                new_pass2 = input("Repeat password: ")
                                if new_pass1 == new_pass2:
                                    change_pw(nickname=nickname, password=new_pass1)
                                    print("A new password was successfully changed")
                            elif answer not in ans_q:
                                print("incorrect answer, try again")
                                return answer

        elif (nickname, password) in check_log().items():
            print(nickname)
            print("SUCCESSFULLY")
            start = Start()
            choice = 1
            while choice == 1:
                start.call()
                choice = int(input("\nIf you want to play one more round pick 1 or pick 2 to finish the game: "))
                if choice == 2:
                    for score in check_bs_sc(nickname):
                        score = int(score[0])
                        if score <= start.score:
                            gm_score(start.score, nickname)
                        elif score >= start.score:
                            pass
                if choice != 1 and choice != 2:
                    print("Fail, try again")
                    choice = int(input("\nIf you want to play 1 round pick 1 or pick 2 to finish the game: "))
    elif auth == "2":
        registration()
        return authorization()
    else:
        print("incorrect request")
        return authorization()


def start_pr():
    try:
        start_the_game = int(input("> "))
        if start_the_game == 1:
            authorization()
        elif start_the_game == 2:
            print("Goodbye, thank you for visiting")
    except ValueError:
        print("incorrect request")
        return start_pr()
