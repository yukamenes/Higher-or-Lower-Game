from game_data import data
from random import choice
from art import logo, vs
from os import system, name


def clear_screen():
    system("cls" if name == "nt" else "clear")

def get_random_options():
    if len(data) < 2:
        raise ValueError("Not enough data to play (at least 2 items required).")
    optionA = choice(data)
    optionB = choice(data)
    while optionA == optionB:
        optionB = choice(data)
    return optionA, optionB

def display_comparison(optionA, optionB):
    print(f"Compare A: {optionA["name"]}, a {optionA["description"]}, from {optionA["country"]}")
    print(vs)
    print(f"Against B: {optionB["name"]}, a {optionB["description"]}, from {optionB["country"]}")


def has_more_followers(optionA, optionB):
    if optionA["follower_count"] > optionB["follower_count"]:
        return True
    else:
        return False

def get_user_answer():
    while True:
        answer = input("Who has more followers? Type 'A' or 'B':").lower()
        if answer in ["a", "b"]:
            return answer
        print("You supposed to write 'a' or 'b'. Try again!")

def play_game():
    print(logo)
    score = 0
    option_a, option_b = get_random_options()

    while True:
        display_comparison(option_a, option_b)
        user_answer = get_user_answer()

        if (has_more_followers(option_a, option_b) and user_answer == 'a') or \
           (has_more_followers(option_b, option_a) and user_answer == 'b'):
            score += 1
            clear_screen()
            print(f"You're right! Your score: {score}")
            option_a = option_b  
            option_b = choice(data)
            while option_a == option_b: 
                option_b = choice(data)
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
    while True:
        if play_again not in ["yes", "no"]:
            print("You supposed to write 'yes' or 'no'. Try again!")
            play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        else:
            break
    if play_again == 'yes':
        clear_screen()
        play_game()

play_game()