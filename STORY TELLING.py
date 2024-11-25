import time
import random

# Define Sci-Fi stories
def tell_sci_fi_story_1():
    """
    Tells the first Sci-Fi story.
    """
    print("In the year 2200, humanity has spread across the stars, encountering new alien species and challenges...")

def tell_sci_fi_story_2():
    """
    Tells the second Sci-Fi story.
    """
    print("On a distant planet, a team of explorers discovers an ancient civilization's technology that could change the fate of the galaxy...")

# Define Adventure stories
def tell_adventure_story_1():
    """
    Tells the first Adventure story.
    """
    print("In the dense jungles of the Amazon, an adventurer searches for a lost city rumored to hold unimaginable treasures...")

def tell_adventure_story_2():
    """
    Tells the second Adventure story.
    """
    print("A brave knight embarks on a perilous quest to rescue a princess from a fearsome dragon...")

# Define Mystery stories
def tell_mystery_story_1():
    """
    Tells the first Mystery story.
    """
    print("In a quiet English village, a detective must solve the mystery of a missing heirloom with a dark past...")

def tell_mystery_story_2():
    """
    Tells the second Mystery story.
    """
    print("A group of friends gather for a dinner party, but the evening takes a sinister turn when one of them is found dead...")

# Main function
def main():
    """ 
    Main function to start the storytelling adventure. Continuously prompts the user to select a 
    story genre and tells a random story from the selected genre. 
    """
    while True:
        print("Welcome to the Storytelling Adventure!")
        print("1. Sci-Fi")
        print("2. Adventure")
        print("3. Mystery")
        choice = input("Enter your choice (1/2/3): ")
        
        # Select and tell a random story based on user choice
        if choice == "1":
            random.choice([tell_sci_fi_story_1, tell_sci_fi_story_2])()
        elif choice == "2":
            random.choice([tell_adventure_story_1, tell_adventure_story_2])()
        elif choice == "3":
            random.choice([tell_mystery_story_1, tell_mystery_story_2])()
        else:
            print("Invalid choice. Please choose a number from 1 to 3.")
        
        # Ask user if they want to hear another story
        cont = input("\nDo you want to hear another story? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for joining the Storytelling Adventure. Goodbye!")
            break

if _name_ == "_main_":
    main()