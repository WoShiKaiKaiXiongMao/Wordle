from colorama import init, Fore, Back, Style
import json
import os
init(autoreset=True)

import random

print("Welcome to Wordle!")

WORDS4 = [
   "able", "ages", "also", "area", "army", "away", "baby", "back", "ball"
    ]
WORDS5 = [
   "apple", "angle", "about", "alone", "alarm", "adapt", "admit", "adopt", "after"
    ]
WORDS6 = [
   "absent", "accept", "access", "across", "acting", "action", "active", "actual", "admire"
    ]

STREAK_FILE = "streak.json"

# loading stats
def load_stats():
    if os.path.exists(STREAK_FILE):
        with open(STREAK_FILE, "r") as f:
            return json.load(f)
    return {"streak": 0, "best": 0, "played": 0, "won": 0}

# saving stats
def save_stats(stats):
    with open (STREAK_FILE, "w") as f:
        json.dump(stats, f)

# ask the player, answer is stored in variable "words"
words = input("How many letters in a word? Please type 4, 5, or 6.")

if words == "4":
    def get_random_word_4():
        return random.choice(WORDS4)

    # check if guess is correct
    def check_guess_4(guess, answer):
        result = []

        # determine whether ans is correct present or absent
        for i in range(4):
            if guess[i] == answer[i]:
                result.append("correct")

            elif guess[i] in answer:
                result.append("present")
            else:
                result.append("absent")

        return result

    # use colorama to colour the letters
    def colorize_guess_4(guess, result):
        colored = ""
        # if correct colour word light green, if present colour word yellow, if absent colour word light black
        for i in range(4):
            if result[i] == "correct":
                colored += Fore.LIGHTGREEN_EX + guess[i].upper() + Style.RESET_ALL
            elif result[i] == "present":
                colored += Fore.YELLOW + guess[i].upper() + Style.RESET_ALL
            else:
                colored += Fore.LIGHTBLACK_EX + guess[i].upper() + Style.RESET_ALL
        return colored

    def play_4():
        # playing the game
        stats = load_stats()
        answer = get_random_word_4()

        # 6 attempts, say if invalid
        for attempt in range(1, 7):
            guess = input(f"Guess {attempt}/6: ").strip().lower()
            if len(guess) != 4 or not guess.isalpha():
                print("Invalid! Must be FOUR (4) letters only. And you just wasted a guess.")
                continue

            # check and
            result = check_guess_4(guess, answer)
            print(colorize_guess_4(guess, result))

            if result == ["correct"] * 4:
                print("You guessed correctly:", answer.upper()), "in", attempt, "tries!"
                stats["won"] += 1
                stats["streak"] += 1
                stats["best"] = max(stats["best"], stats["streak"])
                save_stats(stats)
                print(f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")
                break
        else:
            print("The correct answer was:", answer.upper())
            stats["streak"] = 0
            stats["played"]+= 1
            save_stats(stats)
            print(f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")

    while True:
        play_4()
        again = input("Play again? (y/n) If you want to play the game with different number of letters, please press that green replay button on the top of the screen and restart.").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

elif words == "5":
    def get_random_word_5():
        return random.choice(WORDS5)


    def check_guess_5(guess, answer):
        result = []

        for i in range(5):
            if guess[i] == answer[i]:
                result.append("correct")

            elif guess[i] in answer:
                result.append("present")
            else:
                result.append("absent")

        return result


    def colorize_guess_5(guess, result):
        colored = ""
        for i in range(5):

            if result[i] == "correct":
                colored += Fore.LIGHTGREEN_EX + guess[i].upper() + Style.RESET_ALL
            elif result[i] == "present":
                colored += Fore.YELLOW + guess[i].upper() + Style.RESET_ALL
            else:
                colored += Fore.LIGHTBLACK_EX + guess[i].upper() + Style.RESET_ALL
        return colored


    def play_5():
        stats = load_stats()
        answer = get_random_word_5()

        for attempt in range(1, 7):
            guess = input(f"Guess {attempt}/6: ").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid! Must be FIVE (5) letters only. And you just wasted a guess.")
                continue

            result = check_guess_5(guess, answer)
            print(colorize_guess_5(guess, result))

            if result == ["correct"] * 5:
                print("You guessed correctly:", answer.upper()), "in", attempt, "tries!"
                stats["won"] += 1
                stats["streak"] += 1
                stats["best"] = max(stats["best"], stats["streak"])
                save_stats(stats)
                print(
                    f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")
                break
        else:
            print("The correct answer was:", answer.upper())
            stats["streak"] = 0
            stats["played"] += 1
            save_stats(stats)
            print(f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")


    while True:
        play_5()
        again = input(
            "Play again? (y/n) If you want to play the game with different number of letters, please press that green replay button on the top of the screen and restart.").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

elif words == "6":
    def get_random_word_6():
        return random.choice(WORDS6)

    def check_guess_6(guess, answer):
        result = []

        for i in range(6):
            if guess[i] == answer[i]:
                result.append("correct")

            elif guess[i] in answer:
                result.append("present")
            else:
                result.append("absent")

        return result


    def colorize_guess_6(guess, result):
        colored = ""
        for i in range(6):

            if result[i] == "correct":
                colored += Fore.LIGHTGREEN_EX + guess[i].upper() + Style.RESET_ALL
            elif result[i] == "present":
                colored += Fore.YELLOW + guess[i].upper() + Style.RESET_ALL
            else:
                colored += Fore.LIGHTBLACK_EX + guess[i].upper() + Style.RESET_ALL
        return colored


    def play_6():
        stats = load_stats()
        answer = get_random_word_6()

        for attempt in range(1, 7):
            guess = input(f"Guess {attempt}/6: ").strip().lower()
            if len(guess) != 6 or not guess.isalpha():
                print("Invalid! Must be SIX (6) letters only. And you just wasted a guess.")
                continue

            result = check_guess_6(guess, answer)
            print(colorize_guess_6(guess, result))

            if result == ["correct"] * 6:
                print("You guessed correctly:", answer.upper()), "in", attempt, "tries!"
                stats["won"] += 1
                stats["streak"] += 1
                stats["best"] = max(stats["best"], stats["streak"])
                save_stats(stats)
                print(
                    f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")
                break
        else:
            print("The correct answer was:", answer.upper())
            stats["streak"] = 0
            stats["played"] += 1
            save_stats(stats)
            print(f" Played: {stats["played"]}  Won: {stats["won"]}  Streak: {stats["streak"]}  Best: {stats["best"]} ")


    while True:
        play_6()
        again = input(
            "Play again? (y/n) If you want to play the game with different number of letters, please press that green replay button on the top of the screen and restart.").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

else:
    print("Invalid input! Please type 4, 5, or 6! Anyway, please restart the game by pressing that green play button on the top of the screen.")