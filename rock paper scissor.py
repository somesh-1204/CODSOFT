import random

game = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

user_score = 0
computer_score = 0

print("=" * 50)
print("🎮 WELCOME TO ROCK • PAPER • SCISSORS 🎮")
print("=" * 50)

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    options = {"1": "rock", "2": "paper", "3": "scissors"}

    if choice not in options:
        print("❌ Invalid choice!")
        continue

    user = options[choice]
    computer = random.choice(list(game.keys()))

    print("\n----------------------------")
    print(f"👤 You      : {user.capitalize()}")
    print(f"🤖 Computer : {computer.capitalize()}")
    print("----------------------------")

    if user == computer:
        print("🤝 Match Draw!")

    elif game[user] == computer:
        print("🎉 You Win This Round!")
        user_score += 1

    else:
        print("💻 Computer Wins This Round!")
        computer_score += 1

    print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

    again = input("\nPlay another round? (Y/N): ").strip().lower()

    if again != "y":
        break

print("\n" + "=" * 50)
print("🏁 FINAL RESULT")
print("=" * 50)

print(f"Your Score     : {user_score}")
print(f"Computer Score : {computer_score}")

if user_score > computer_score:
    print("\n🏆 Overall Winner: You!")
elif computer_score > user_score:
    print("\n🤖 Overall Winner: Computer!")
else:
    print("\n🤝 Overall Result: It's a Tie!")

print("\n✨ Thanks for Playing! ✨")