from colorama import init, Fore, Back, Style
import json
import os
init(autoreset=True)

import random

print("Welcome to Wordle!")

WORDS4 = [
   "able", "ages", "also", "area", "army", "away", "baby", "back", "ball",
   "band", "bank", "base", "bear", "beat", "been", "beer", "bell", "belt",
   "best", "bird", "blow", "blue", "boat", "body", "bold", "bone", "book",
   "boom", "boot", "born", "both", "bowl", "burn", "bury", "bush", "busy",
   "calm", "camp", "card", "care", "case", "cash", "cast", "chat", "chip",
   "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool",
   "copy", "core", "cost", "crew", "dark", "data", "date", "dawn", "days",
   "dead", "deal", "dear", "debt", "deep", "deny", "desk", "diet", "dish",
   "does", "done", "door", "dose", "down", "draw", "drew", "drop", "duck",
   "dust", "duty", "each", "earn", "ease", "east", "easy", "edge", "else",
   "even", "ever", "evil", "face", "fact", "fail", "fair", "fall", "farm",
   "fast", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill",
   "film", "find", "fine", "fire", "fish", "five", "flat", "flow", "food",
   "foot", "form", "four", "free", "from", "fuel", "full", "fund", "gain",
   "game", "gate", "gave", "gear", "gift", "girl", "give", "glad", "goal",
   "goes", "gold", "gone", "good", "grab", "grey", "grow", "hair", "half",
   "hall", "hand", "hang", "hard", "harm", "hate", "have", "head", "hear",
   "held", "help", "here", "hide", "high", "hill", "hire", "hold", "hole",
   "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt", "idea",
   "into", "item", "join", "jump", "just", "keen", "keep", "kept", "kick",
   "kill", "kind", "king", "knee", "knew", "know", "lady", "laid", "lake",
   "land", "last", "late", "lead", "left", "less", "life", "lift", "like",
   "line", "link", "list", "live", "loan", "lock", "long", "look", "lord",
   "lose", "lost", "love", "luck", "made", "mail", "main", "make", "male",
   "many", "mark", "mass", "meal", "mean", "meat", "meet", "menu", "mess",
   "milk", "mind", "mine", "miss", "mood", "moon", "more", "most", "move",
   "much", "must", "name", "near", "need", "news", "next", "nice", "nine",
   "none", "nose", "note", "once", "only", "onto", "open", "over", "pace",
   "pack", "page", "paid", "pain", "pair", "park", "part", "pass", "path",
   "pick", "pipe", "plan", "play", "plot", "plug", "plus", "poem", "poet",
   "poll", "poor", "port", "post", "pull", "pure", "push", "race", "rail",
   "rain", "rank", "rare", "rate", "read", "real", "rear", "rely", "rest",
   "rice", "rich", "ride", "ring", "rise", "risk", "road", "role", "roll",
   "roof", "room", "rose", "rule", "rush", "safe", "sail", "sale", "salt",
   "same", "sand", "save", "seat", "seed", "seek", "seem", "seen", "sell",
   "send", "shop", "show", "sick", "side", "sign", "site", "size", "skin",
   "slip", "slow", "snow", "soft", "soil", "sold", "some", "song", "soon",
   "soul", "spot", "star", "stay", "step", "stop", "such", "suit", "sure",
   "take", "talk", "team", "test", "than", "that", "them", "then", "they",
   "thin", "this", "time", "tiny", "told", "tone", "took", "tool", "tour",
   "town", "tree", "trip", "true", "turn", "twin", "type", "unit", "upon",
   "urge", "used", "user", "vast", "very", "view", "vote", "wait", "wake",
   "walk", "wall", "want", "warm", "wash", "weak", "wear", "week", "well",
   "went", "were", "west", "what", "when", "wide", "wife", "wild", "will",
   "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "wore",
   "work", "yard", "yarn", "yawn", "year", "yell", "your", "zero", "zone"
]

WORDS5 = [
   "apple", "angle", "about", "alone", "alarm", "adapt", "admit", "adopt", "after", "again",
   "agent", "agree", "ahead", "allow", "along", "alter", "amaze", "amber", "amend", "among",
   "anger", "angry", "apart", "apply", "arena", "argue", "arise", "array", "arrow", "ashes",
   "aside", "audio", "avoid", "awake", "award", "aware", "badly", "baker", "barks", "beach",
   "beard", "beast", "begin", "being", "below", "bench", "birth", "black", "blade", "blame",
   "blank", "blast", "blend", "block", "blood", "board", "boost", "booth", "bound", "brain",
   "brake", "brand", "brave", "bread", "break", "brick", "bring", "broad", "brown", "build",
   "built", "burnt", "buyer", "cable", "carry", "catch", "cause", "chain", "chair", "chase",
   "cheap", "check", "chest", "chief", "child", "claim", "class", "clean", "clear", "climb",
   "clock", "close", "cloud", "coach", "coast", "count", "court", "cover", "craft", "crash",
   "cream", "crime", "cross", "crowd", "cycle", "daily", "dance", "death", "delay", "depth",
   "digit", "dirty", "doubt", "draft", "drama", "dream", "dress", "drink", "drive", "earth",
   "enemy", "enrol", "entry", "error", "event", "every", "faith", "fault", "field", "fight",
   "final", "first", "focus", "force", "frame", "fresh", "front", "fruit", "giant", "glass",
   "grant", "grape", "great", "green", "gross", "group", "guide", "happy", "harsh", "heart",
   "heavy", "horse", "hotel", "house", "human", "ideal", "image", "index", "input", "issue",
   "judge", "juice", "knock", "knife", "label", "large", "laser", "later", "laugh", "layer",
   "learn", "lease", "leave", "legal", "light", "limit", "local", "logic", "lucky", "lunch",
   "magic", "major", "maker", "march", "match", "maybe", "media", "metal", "minor", "model",
   "money", "month", "motor", "mount", "music", "nasty", "night", "noise", "north", "novel",
   "nurse", "occur", "ocean", "offer", "often", "order", "other", "owner", "panel", "party",
   "phase", "phone", "photo", "piano", "piece", "pilot", "pitch", "place", "plain", "plane",
   "plant", "plate", "point", "power", "press", "price", "pride", "print", "prior", "prize",
   "proof", "prove", "proud", "queen", "quick", "quiet", "quite", "quote", "reach", "react",
   "ready", "refer", "right", "rival", "river", "rough", "round", "route", "royal", "rural",
   "scale", "scene", "scope", "score", "sense", "serve", "setup", "shade", "shake", "shall",
   "shape", "share", "sharp", "sheet", "shelf", "shift", "shine", "shirt", "shock", "shoot",
   "short", "shown", "sight", "since", "skill", "sleep", "small", "smart", "smile", "smoke",
   "solid", "solve", "sound", "south", "space", "spare", "speak", "speed", "spend", "spine",
   "sport", "staff", "stage", "stand", "start", "state", "steam", "steel", "stick", "still",
   "stock", "stone", "store", "storm", "story", "strip", "study", "stuff", "style", "sugar",
   "super", "sweet", "table", "taste", "teach", "thank", "theme", "there", "thing", "think",
   "third", "throw", "tight", "title", "today", "topic", "total", "touch", "tower", "track",
   "trade", "train", "trend", "trial", "trust", "truth", "under", "union", "unity", "value",
   "video", "visit", "voice", "waste", "watch", "water", "weigh", "wheel", "where", "which",
   "while", "white", "whole", "woman", "world", "worry", "worth", "write", "yacht", "young"
]

WORDS6 = [
   "absent", "accept", "access", "across", "acting", "action", "active", "actual", "admire", "advice",
   "advise", "affair", "affect", "afraid", "agency", "almost", "always", "amount", "animal",
   "annual", "answer", "appeal", "appear", "around", "arrive", "artist", "aspect", "assist", "assume",
   "attack", "attend", "author", "autumn", "backed", "barely", "battle", "beauty", "become", "before",
   "behalf", "behind", "belief", "belong", "better", "beyond", "bishop", "border", "bottle", "bottom",
   "branch", "breath", "bridge", "bright", "broken", "budget", "burden", "bureau", "button", "camera",
   "cannot", "carbon", "career", "castle", "casual", "caught", "centre", "chance", "change", "charge",
   "choice", "choose", "church", "circle", "client", "closed", "closer", "coffee", "column", "combat",
   "coming", "common", "couple", "course", "covers", "create", "credit", "crisis", "custom",
   "damage", "danger", "dealer", "debate", "decade", "decide", "defeat", "defend", "degree", "delete",
   "demand", "depend", "desert", "design", "desire", "detail", "detect", "device", "differ",
   "dinner", "direct", "doctor", "dollar", "domain", "double", "driven", "driver", "during", "easily",
   "eating", "editor", "effect", "effort", "eighth", "either", "eleven", "emerge", "empire", "employ",
   "enable", "ending", "energy", "engage", "engine", "enough", "ensure", "entire",
   "escape", "estate", "exceed", "except", "excess", "expand", "expect", "expert", "export",
   "extend", "extent", "fabric", "facing", "factor", "failed", "fairly", "fallen", "family", "famous",
   "father", "fellow", "female", "figure", "filing", "finger", "finish", "flight", "flower",
   "follow", "forest", "forget", "formal", "format", "former", "foster", "fought", "fourth", "freely",
   "friend", "future", "garden", "gather", "giving", "global", "golden", "ground", "growth",
   "guilty", "handed", "handle", "happen", "hardly", "headed", "health", "height", "hidden", "holder",
   "honest", "impact", "import", "income", "indeed", "injury", "inside", "intend", "invest",
   "island", "itself", "junior", "keeper", "labour", "latest", "launch",
   "lawyer", "leader", "league", "leaves", "legacy", "length", "lesson", "letter", "lights", "likely",
   "linked", "liquid", "listen", "little", "living", "locate", "locked", "lonely", "longer", "looked",
   "lovely", "mainly", "making", "manage", "manual", "marine", "marked", "market", "master",
   "matter", "medium", "member", "memory", "mental", "merely", "merger", "method", "middle", "minute",
   "mirror", "mobile", "modern", "modest", "moment", "mostly", "mother", "motion", "moving",
   "museum", "myself", "nation", "native", "nature", "nearby", "nearly", "nobody", "normal",
   "notice", "number", "object", "obtain", "office", "online", "option", "orange", "origin",
   "output", "packed", "palace", "parent", "partly", "people", "period", "permit", "person", "picked",
   "planet", "player", "please", "plenty", "pocket", "prefer", "pretty", "prince", "prison",
   "profit", "proper", "proven", "public", "pursue", "raised", "random", "rarely", "rather", "rating",
   "reader", "really", "reason", "recall", "recent", "record", "reduce", "regard", "region",
   "relate", "relief", "remain", "remote", "remove", "repair", "repeat", "report", "rescue", "resort",
   "result", "retain", "return", "reveal", "salary", "saving", "singer", "soccer", "spirit", "spoken",
   "spring", "stream", "street", "supply", "target", "thanks", "theory", "thirty", "thread",
   "thrive", "ticket", "timely", "toward", "valley", "vendor", "versus", "vision", "visual",
   "volume", "walker", "wealth", "weekly", "weight", "window", "winner", "winter", "worthy", "yellow"
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
