from game_data import data
from art import logo, vs
import random


game_on = True
print(logo)


def get_acc():
    return random.choice(data)


def check(a_followers, b_followers, guess):
    if a_followers["follower_count"] > b_followers["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def format_data(acc):
    name = acc["name"]
    des = acc["description"]
    country = acc["country"]
    return f"{name} , a {des} , from {country}"


game_ON = True

score = 0
A = get_acc()
B = get_acc()
while game_ON:
    print(f"Your Current Score is {score} ")
    print(f"Compare: A :-{format_data(A)}")
    print(vs)
    print(f"Compare: B :-{format_data(B)}")
    guess = input("which one have more followers? A or B ").lower()

    res = check(A, B, guess)

    if res:
        score += 1
        A = B
        B = get_acc()
    else:

        print(f"your score is {score}")
        game_ON = False
