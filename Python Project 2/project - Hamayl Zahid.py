import random
import time


class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.inventory = []
        self.score = 0

    def show_status(self):
        print(f"\n--- {self.name} ---")
        print("Inventory: ")
        for item in self.inventory:
            print(f"- {item}")
        print(f"Score: {self.score}")
        time.sleep(2)


def intro():
    """
    Prints the game introduction.
    """
    print("\nWelcome to Space Explorer!")
    time.sleep(2)
    print("You are a lone space traveler, venturing into the unknown depths of the cosmos.")
    time.sleep(1)
    print("Your mission: to explore the galaxy and discover its wonders.")
    print("--------------------------------------------------")


def choose_destination():
    """
    Lets the player choose their next destination.
    """
    print("\nContinue Exploring Space")
    time.sleep(1)
    print("Where do you want to travel?")
    time.sleep(1)
    print("1. Nebula Cluster")
    time.sleep(1)
    print("2. Alien Planet")
    time.sleep(1)

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        nebula_cluster()
        player.score += 5
    elif choice == '2':
        player.score += 5
        alien_planet()
    else:
        print("Invalid choice. Please enter 1 or 2: ")
        choose_destination()


def nebula_cluster():
    """
    Handles the encounter with the nebula cluster.
    """
    print("\nYou've entered a colorful nebula cluster.")
    time.sleep(1)
    print(" It's a breathtaking sight, but also eerily silent.")
    time.sleep(3)

    print("You encounter a peaceful alien species. They offer you valuable information.")
    time.sleep(2)
    print('''you have 2 options
                  1.Gain secrets of advanced technology, scientific discoveries and lost history
                  2.Leave them and follow a bright purple light ''')

    ch = input("Enter 1 or 2: ")

    if ch == "1":

        print(" You gain some secrets ... 15 points for you.")
        time.sleep(2)
        player.score += 15
        '''
        random library is used to have different encounters everytime you make a choice
        '''

        post_secret_event = random.randint(1, 4)

        if post_secret_event == 1:

            print("As you leave, a small alien child gives you a strange device. ")
            time.sleep(2)
            print("It seems to be a universal translator.")
            time.sleep(2)

            player.inventory.append("Universal Translator")
            print("Universal Translator added to inventory!")
            time.sleep(1)
            print("Continue Exploring Space ")

            # Future Events

        elif post_secret_event == 2:

            print("Suddenly, a rival alien faction arrives, demanding the secrets you were given! \nThey attack!")
            time.sleep(2)
            print("A quick battle ensues!")
            time.sleep(2)
            battle_outcome = random.randint(1, 2)

            if battle_outcome == 1:

                print("You manage to fight them off, but your ship sustains minor damage")
                time.sleep(1)
                print("you have to give 5 points to repair ship")
                player.score -= 5
                time.sleep(1)
                print("ship is repaired .Continue exploring Space")
            else:

                print("You are overwhelmed and they steal some of your supplies!\n -10 score")
                time.sleep(1)
                player.score -= 10
                if "Nebula Ore Sample" in player.inventory:
                    player.inventory.remove("Nebula Ore Sample")
                    print("They stole your Nebula Ore Sample!")
        elif post_secret_event == 3:

            print("The aliens offer you a rare artifact as a sign of goodwill.")
            time.sleep(1)
            artifact_type = random.choice(["Ancient Map", "Energy Core", "Data Chip"])
            player.inventory.append(artifact_type)
            print(f"You received an {artifact_type}!")
            time.sleep(1)
            print("Continue Exploring Space")
            # Future event: The artifact has a special use later in the game.
        elif post_secret_event == 4:

            print("As you leave, you notice a hidden compartment in your ship.")
            time.sleep(1)
            print("The aliens must have placed something there.")
            time.sleep(1)
            print("You find a small cache of valuable resources! +10 score")
            player.score += 10
            player.inventory.append("Rare Minerals")
            time.sleep(1)
            print("Rare Minerals added to inventory")
            time.sleep(1)
            print("Continue Exploring Space")
    elif ch == "2":

        print("You decide to follow the bright purple light...")
        time.sleep(2)
        purple_light_event()  # Calling a new function
    else:
        print("incorrect input")


def purple_light_event():

    print("You follow the mesmerizing purple light deeper into the nebula...")
    time.sleep(2)
    '''
    random library is used to have different encounters everytime you make a choice
            '''

    event = random.randint(1, 3)  # Random event

    if event == 1:

        print("The light leads you to a field of rare energy crystals!\n +25 score")
        player.score += 25

    elif event == 2:

        print("You get lost in the nebula. You lose 5 points.")
        time.sleep(2)
        player.score -= 5
        print("Suddenly, your ship is caught in a gravitational anomaly!")
        time.sleep(2)
        print("1. Attempt to escape using emergency thrusters.")
        time.sleep(1)
        print("2. Analyze the anomaly for weaknesses.")
        time.sleep(2)
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("5 points")
            player.score += 5
            escape_attempt()

        elif choice == "2":
            print("5 points")
            player.score += 5
            analyze_anomaly()
    else:
        print("The light suddenly vanishes, leaving you disoriented.\n You lose some time. -5 score")
        player.score -= 5


def escape_attempt():
    """
        Handles the escape attempt.
        """
    print("Engines roar! You try to break free...")
    time.sleep(1)
    chance = random.randint(1, 20)
    ''' random library is used to have different encounters
        everytime you make a choice.'''

    if chance > 10:

        print("YES! You burst through the anomaly's grip!"
              "and continue your journey.")
        time.sleep(1)
        print('''You're safe. New course plotted 
        "+5 points''')
        time.sleep(2)

        print("Congrats!!")
        player.score += 5

    elif chance > 15:

        print("So close! Energy crackles around you!")
        time.sleep(1)
        print("You escape...but Your ship is severely damaged.....\n you lost 5 points")

        player.score -= 5
        time.sleep(1)
        end_game()

    else:

        print("NO! The anomaly pulls you back!")
        time.sleep(1)
        print("Systems failing! Escape impossible.")
        player.score -= 5
        end_game()


def analyze_anomaly():

    print("You analyze the anomaly and discover a weakness.")
    time.sleep(1)
    print("looking for a way through...")
    time.sleep(1)
    print("The energy is weird. Nothing like this before.")
    time.sleep(1.5)

    chance = random.randint(1, 10)   # random library

    if chance > 4:

        print("You find a weak spot! A way to get through!")
        time.sleep(1)
        print("You carefully fly through. You made it!")
        time.sleep(1.5)
        print("You're safe on the other side")
        player.score += 5

    elif chance > 2:

        print("You find something, but it's hard to see.")
        time.sleep(1)
        print("You try to follow it, but the anomaly moves.")
        time.sleep(1.5)
        print("You get through , but your ship gets a little banged up.")
        time.sleep(1)
        print("You successfully navigate through the anomaly and continue your journey.\n but you lost 2 points")
        player.score -= 2
        time.sleep(2)
        print('''You've successfully exited the nebula cluster
            you can again choose : ''')

    else:

        print("The energy is too messy. You can't see anything.")
        time.sleep(1)
        print("The anomaly gets stronger! Your ship gets hit!")
        time.sleep(1.5)
        print("You have to go back. Your ship is hurt.")
        player.score -= 5
        end_game()


def alien_planet():
    """Handles the encounter with the alien planet with more adventures."""

    print("\nYou've landed on an alien planet. The air is thick and the landscape alien.")
    time.sleep(1.5)

    encounter_type = random.randint(1, 2)  # More varied encounters

    if encounter_type == 1:  # Ancient ruins

        print("You stumble upon crumbling ruins, remnants of a long-lost civilization.")
        time.sleep(2)
        print('''Inside, you discover a powerful energy crystal. It hums with unknown energy.
        1.Get Energy Crystal
        2.leave it''')

        ch = input("Choose 1 or 2: ")

        if ch == "1":

            spirits_angered = random.randint(1, 2)
            if spirits_angered == 1:

                print("The spirits guarding the crystal are angered! You must choose:")
                time.sleep(1)
                print("1. Attempt to fight them.")
                print("2. Attempt to appease them with an offering.")

                while True:
                    fight_or_appease = input("Enter 1 or 2: ")
                    if fight_or_appease in ("1", "2"):
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")

                if fight_or_appease == "1":

                    battle_outcome = random.randint(1, 2)
                    if battle_outcome == 1:
                        print("You defeat the spirits, but the crystal shatters slightly.")
                        print("You still obtain a Fragmented Energy Crystal. +10 Score")

                        player.inventory.append("Fragmented Energy Crystal")
                        player.score += 10
                    else:
                        print("The spirits overwhelm you! You barely escape with -15 score.")
                        player.score -= 15
                elif fight_or_appease == "2":

                    if "Shiny Rock" in player.inventory:
                        print("You offer the shiny rock.")
                        time.sleep(2)
                        print("The spirits seem pleased and allow you to take the crystal unharmed")

                        player.inventory.remove("Shiny Rock")
                        player.inventory.append("Energy Crystal")
                        player.score += 20
                    else:
                        print("You have nothing to offer. The spirits attack! -10 score")
                        player.score -= 10

            elif spirits_angered == 2:  # No spirits

                print("You carefully take the Energy Crystal. It hums with power. +20 score")
                player.inventory.append("Energy Crystal")
                player.score += 20
                # Event: You discover a hidden message etched on the base where the crystal was.
                print("You discover a hidden message etched on the base where the crystal was.")
                player.inventory.append("Ancient Inscription")

        elif ch == 2:
            player.score += 20
            print("You find a unique ecosystem. Strange plants and small creatures surround you.")
            time.sleep(2)
            discovery = random.randint(1, 3)

            if discovery == 1:

                print("You discover a rare plant with medicinal properties. You collect a sample.")
                time.sleep(2)
                player.inventory.append("Medicinal Plant")
                print("Medicinal Plant added to inventory.")

            elif discovery == 2:

                print("A small, harmless creature approaches you. It seems curious.")
                time.sleep(2)
                print("It gives you a shiny rock")
                time.sleep(1)
                player.inventory.append("Shiny Rock")
                print("Shiny rock added to inventory")
                time.sleep(2)

            else:
                print("You find a strange fruit tree. You eat a fruit")
                time.sleep(2)
                print("It was delicious and gives you energy")
                time.sleep(1)
                player.score += 5
                print("+5 score")
    else:

        print("Suddenly, you're surrounded by strange, net-wielding aliens! They capture you!")
        time.sleep(2)
        print("You're taken to their camp. They seem interested in studying you.")
        time.sleep(1)
        print("You have a chance to escape:")
        time.sleep(2)
        escape_choice = input("Pay 5 points to bribe a guard (b) or attempt a risky escape (r)? (b/r): ")
        time.sleep(2)

        if escape_choice.lower() == 'b':

            if player.score >= 5:
                print("You bribe a guard, who discreetly opens a back exit.")
                time.sleep(2)
                print("You escaped !")
                time.sleep(1)
                print("-5 score")
                player.score -= 5

            else:
                print("You don't have enough points to bribe the guard.")
                time.sleep(1)
                player.score -= 5
                print("-5 score")
                print("The aliens take some of your supplies")
                time.sleep(1)

        elif escape_choice.lower() == 'r':
            escape_roll = random.randint(1, 7)

            if escape_roll > 4:
                print("You manage to overpower your guards and make a daring escape!")
                time.sleep(1)
                player.score += 5  # reward for successful escape
                print("+5 score")

            else:
                print(
                    "Your escape attempt fails, and the aliens become more wary. They take some of your supplies.")
                time.sleep(1)
                player.score -= 10
                print("-10 score")
        else:

            print("Invalid choice. You remain captive for now.")
            time.sleep(1)
            player.score -= 5
            print("-5 score")
            time.sleep(1)
            print("The aliens take some of your supplies")
    print(f"Inventory: {player.inventory}")


def end_game():
    """
    Prints the game over message.
    """
    print("--------------------------------------------------")
    print(f"Your final score: {player.score}")
    time.sleep(2)
    print("Game Over.")


if __name__ == "__main__":
    intro()
    player = Player()
    while True:
        player.show_status()
        choose_destination()
        if player.score <= 0:
            print('''your score is not enough to survive.
            You cannot Continue ...''')
            time.sleep(2)

            end_game()
            break
