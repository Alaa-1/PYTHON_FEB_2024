# * Functions
# what is a function ?
# ? a set of instructions
# ? could take in parameters
#! All functions always return something

# print(print("hello"))


def greeting():
    return "hello"


# * To invoke a function we need to call its name
# print(greeting())
# result = greeting()
# print(greeting())


# * Parameters
def say_hello(name):
    return f"good afternoon {name}"


# print(say_hello("Joe"))


def say_hello_mutiple_times(times, name):

    for i in range(times):
        print(f"Good morning {name}")


# say_hello_mutiple_times(name="Louis", times=52)


#! default parameter
def default_greeting(times=None, name="Anonymous"):

    if times == None:
        print("Something went wrong")
    else:
        for i in range(times):
            print(f"Good morning {name}")


# default_greeting()
# default_greeting(12)


# def sum(num1, num2):
#     print(num1 + num2)


# sum(5, 6)


def sum_infinite(*args):
    print(args)
    sum = 0
    for number in args:
        sum += number
    print(sum)


# sum_infinite(3, 8, 101, 4, 7, 8, 22, 33)


user = {"first_name": "Marcus", "last_name": "smith", "email": "a@a.com"}


def display_info(user_dict):

    # print(f"my name is {user_dict["first_name"]} {user_dict["last_name"]} and my email is {user_dict["email"]}")
    first_name = user_dict["first_name"]
    last_name = user_dict["last_name"]
    email = user_dict["email"]

    # TODO destructuring for Dict
    # first_name, last_name, email = user_dict
    print(first_name, last_name, email)


# display_info(user)

# * multiple keyword args / named args
# def print_dict(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# # print_dict(first_name = "Jake", last_name="Smith", email= "jake@icloud.com")


# nba_player = {"name": "Lebron", "team": "Lakers", "shirt_number": 23}

# # nba_player_modified = {"name": "Lebron", "team": "Lakers", "shirt_number":23, "middle_name":"King"}

# nba_player_modified = {**nba_player, "middle_name": "King"}

# # print(nba_player_modified)

# # nba_player_transfer = {"team":"Clevlends", **nba_player}

# print(nba_player)
# print("=" * 36)
# print(nba_player_modified)


# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies": ["rock climbing", "knitting"],
}

users_list = [
    {"username": "joe", "email": "joe@joe.joe"},  # index 0
    {"username": "kayne", "email": "kayne@kayne.kayne"},  # index 1
    {"username": "jane", "email": "jane@jane.jane"},  # index 2
]

# print(resume_data["skills"][1])

# for key in resume_data:
#     for item in resume_data[key]:
#         print(item)


def print_users_info(all_users_list):

    for user in all_users_list:
        # {'username': 'joe', 'email': 'joe@joe.joe'}
        print(f"username -> {user["username"]} | email -> {user["email"]}")


print_users_info(users_list)
# username -> "joe" | email -> "joe@joe.joe"
