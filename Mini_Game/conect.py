import mysql.connector as mysql

db = mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="$$$$",
    database="db_mini_game"
)
cursor = db.cursor()


# use the function to register a new user
def reg_new_user(values):
    query = "INSERT INTO users(name, user_name, password, question_id, answer_quest, time_reg) " \
            "VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    db.commit()


# use for insert in user data information about user_name
def user_data(user_d):
    query = "INSERT INTO user_data(user_name, best_score) VALUES(%s, 0)"
    cursor.execute(query, user_d)
    db.commit()


# use check_log to check if the nickname has already been registered
def check_log():
    query = "SELECT user_name from users ORDER BY user_name"
    cursor.execute(query)
    usernames = cursor.fetchall()
    return str(tuple(usernames))


# use for getting info from the database for login
def get_data():
    query = "SELECT user_name, password from users ORDER BY user_name"
    cursor.execute(query)
    # fetching all usernames from the 'cursor' object
    usernames = cursor.fetchall()
    # Showing the data
    return dict(usernames)


# use for inserting score in db
def gm_score(score, nickname):
    query = "UPDATE user_data SET best_score=%s WHERE user_name=%s"
    cursor.execute(query, [score, nickname])
    db.commit()


# use to check if the best score is more than the actual result
def check_bs_sc(nickname):
    query = "SELECT best_score from user_data WHERE user_name=%s"
    cursor.execute(query, [nickname])
    best_score = cursor.fetchall()
    return best_score


# use for changing password
def change_pw(nickname, password):
    query = "UPDATE users SET password=%s WHERE user_name=%s"
    cursor.execute(query, [password, nickname])
    db.commit()


# use to get information about the secret question
def get_que_id(user_name):
    query = "SELECT question_id from users WHERE user_name=%s"
    cursor.execute(query, [user_name])
    info_q = cursor.fetchall()
    return info_q


# use to get information about the answer to the secret question
def ans_check(user_name):
    query = "SELECT answer_quest from users WHERE user_name=%s"
    cursor.execute(query, [user_name])
    ans_q = cursor.fetchall()
    return ans_q
