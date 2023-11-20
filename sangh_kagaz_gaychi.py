import random

def get_user_choice():
    print("انتخاب کنید:")
    print("1. سنگ")
    print("2. کاغذ")
    print("3. قیچی")
    choice = input("عدد مربوط به انتخاب خود را وارد کنید: ")
    return choice

def get_computer_choice():
    return random.choice(["سنگ", "کاغذ", "قیچی"])

def determine_winner(user_choice, computer_choice):
    print(f"شما: {user_choice}")
    print(f"کامپیوتر: {computer_choice}")

    if user_choice == computer_choice:
        return "مساوی!"
    elif (
        (user_choice == "1" and computer_choice == "3") or
        (user_choice == "2" and computer_choice == "1") or
        (user_choice == "3" and computer_choice == "2")
    ):
        return "شما برنده شدید!"
    else:
        return "کامپیوتر برنده شد."

def play_game():
    print("بازی سنگ، کاغذ، قیچی!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
