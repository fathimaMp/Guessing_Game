import random
import os
import time
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Women's Day Theme: List of Inspirational Women and Their Hints
women_leaders = {
    "Marie Curie": ["First woman to win a Nobel Prize", "Pioneer in radioactivity"],
    "Malala Yousafzai": ["Advocate for girls' education", "Youngest Nobel Prize laureate"],
    "Kalpana Chawla": ["First Indian woman in space", "NASA astronaut"],
    "Indira Gandhi": ["First female Prime Minister of India", "Led during major wars"],
}

# Function to Display Stylish Text
def display_message(message, color=Fore.MAGENTA, delay=0.05):
    for char in message:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print("\n")

# Function to Play the Game
def play_game():
    score = 0
    play_again = "yes"

    display_message("\n🎉 Welcome to the Women's Day Guessing Game! 🎉\n", Fore.GREEN)
    
    while play_again.lower() == "yes":
        # Pick a random woman from the list
        woman, hints = random.choice(list(women_leaders.items()))

        display_message(f"🌟 Who am I? 🌟", Fore.YELLOW)
        time.sleep(1)

        # Provide hints one by one
        for index, hint in enumerate(hints, start=1):
            display_message(f"Hint {index}: {hint}", Fore.CYAN)
            time.sleep(1)

        # Get the user's guess
        user_guess = input(Fore.LIGHTGREEN_EX + "\n🔍 Your guess: " + Style.RESET_ALL).strip()

        # Check the answer
        if user_guess.lower() == woman.lower():
            display_message("🎉 Correct! You got it right! 🎉", Fore.GREEN)
            score += 1
        else:
            display_message(f"❌ Oops! The correct answer was: {Fore.RED}{woman}", Fore.RED)

        # Ask if the user wants to play again
        play_again = input(Fore.LIGHTBLUE_EX + "\nDo you want to play again? (yes/no): " + Style.RESET_ALL).strip().lower()

    # Final Score
    clear_screen()
    display_message(f"\n🏆 Your final score: {score} points! 🏆\n", Fore.YELLOW)
    display_message("💖 Happy Women's Day! Keep Learning and Inspiring!💖\n\n🌸 A Woman is the Full Circle. Within Her is the Power to Create, Nurture, and Transform. 🌸\n\n💖 She is Clothed in Strength & Dignity, and She Laughs Without Fear of the Future. 💖\n\n🚀 Here's to Strong Women: May We Know Them, May We Be Them, May We Raise Them! 🚀\n\n🎉 Happy International Women's Day! Keep Inspiring the World! 💃 ", Fore.GREEN)

# Run the game
if __name__ == "__main__":
    play_game()



  