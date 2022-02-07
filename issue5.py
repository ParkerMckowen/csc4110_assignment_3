import random

if __name__ == "__main__":
    bank_balance = 250
    player_balance = 250
    while bank_balance >= 0 and player_balance >= 0:
        print(f"Your balance: {player_balance}")
        wager = int(input("Your wager: "))
        bet = input("Choose (-) for 0-0.5 or (+) for 0.5-1: ")
        rand_val = random.uniform(0, 1)
        if rand_val == 0.5:
            continue
        elif rand_val < 0.5 and bet == "-":
            player_balance += wager
            bank_balance -= wager
            print("You win!!")

        elif rand_val > 0.5 and bet == "-":
            player_balance -= wager
            bank_balance += wager
            print("You LOSE!!")

        elif rand_val > 0.5 and bet == "+":
            player_balance += wager
            bank_balance -= wager
            print("You win!!")

        elif rand_val > 0.5 and bet == "-":
            player_balance -= wager
            bank_balance += wager
            print("You LOSE!!")
