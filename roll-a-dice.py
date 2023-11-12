import random


response = input("Press 'y' to roll dice, or 'n' to exit the program... ")

def give_result(resp):

    roll = random.randint(1, 6)
    
    if (resp == "y"):
        if (roll == 1):
            print("[   ]")
            print("[ * ]")
            print("[   ]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        elif (roll == 2):
            print("[   ]")
            print("[* *]")
            print("[   ]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        elif (roll == 3):
            print("[   ]")
            print("[***]")
            print("[   ]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        elif (roll == 4):
            print("[* *]")
            print("[   ]")
            print("[* *]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        elif (roll == 5):
            print("[* *]")
            print("[ * ]")
            print("[* *]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        elif (roll == 6):
            print("[* *]")
            print("[* *]")
            print("[* *]")
            response = input("Press 'y' to roll dice or press 'n' to exit... ")
            give_result(response)
        else:
            print("There's glitch...")
    else:
        print("Code exited...")

give_result(response)
