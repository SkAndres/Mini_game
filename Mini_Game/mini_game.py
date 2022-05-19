import random


class Games:

    def __init__(self):
        self.chest = random.randint(1, 10)
        self.score = 0
        self.attempt = 3
        self.select = []


class Start(Games):

    def rand_number(self):
        self.chest = random.randint(1, 10)

    def greeting(self):
        print(f"Hi, and welcome to pygame, you have {self.attempt} attempts in order to guess number\n")
        print("======================================10=1===========\n"
              "If you select = 'multiply' or '1' '\n"
              "The number will be multiplied by 2\n"
              "if you use the hint you will earn + 2 score\n"
              "==================================================\n"
              "If you select = 'divisible' or '2' \n"
              "The number will be divisible by 2\n"
              "if you use the hint you will earn + 4 score\n"
              "==================================================\n"
              "If you select = 'easy hint' or '3' \n"
              "the hint allows to reduce the search range\n"
              "if you use the hint you will earn + 6 score\n"
              "=================================================\n")

    def hint(self):
        select = input("choose hint > ")
        # below we give user a hint
        if select == "multiply".lower() or select == "1":
            print("Number is equal:", self.chest * 2)
        elif select == "divisible".lower() or select == "2":
            print("Number is equal:", float(self.chest / 2))
        elif select == "easy hint".lower() or select == "3":
            if self.chest < 5:
                print("The number is less than 5")
            elif self.chest > 5:
                print("The number is more than 5")
        self.select.append(select)
        return self.select

    def random(self):
        choose = int(input("Guess the number> "))
        # first hint
        if self.select[0] == '1':
            if choose == self.chest:
                self.score += 2
                print("Congratulations! You won, your score is ", self.score)
            elif choose != self.chest and self.attempt != 1:
                self.attempt -= 1
                print(f"You have only {self.attempt} attempt")
            elif self.attempt == 1:
                print("You lose😥")
        # second hint
        elif self.select[0] == '2':
            if choose == self.chest:
                self.score += 4
                print("Congratulations! You won, your score is", self.score)
            elif choose != self.chest and self.attempt != 1:
                self.attempt -= 1
                print(f"You have only {self.attempt} attempt")
            elif self.attempt == 1:
                print("You lose😥")
        # third hint
        elif self.select[0] == '3':
            if choose == self.chest:
                self.score += 6
                print("Congratulations! You win ", self.score)
            elif choose != self.chest and self.attempt != 1:
                self.attempt -= 1
                print(f"You have only {self.attempt} attempt")
            elif self.attempt == 1:
                print("You lose😥")

    def call(self):
        self.greeting()
        self.hint()
        self.random()
        self.rand_number()
        self.select.pop(0)
