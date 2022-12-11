import random
import string

def passwd_gen():
    password = ""
    password_strength = input("How strong do you want the password to be? Strong (S) Medium (M) or Weak (W)")

    if password_strength.lower() == "s":
        for num in range(0,10+1):
            rando_character = random.choice(string.punctuation)
            rando_letter = random.choice(string.ascii_letters)
            rando_num = random.randint(0, 10)
            password+= str(random.choice([rando_character,rando_letter,rando_num]))

    elif password_strength.lower() == "m":
        for num in range(0,6+1):
            rando_letter = random.choice(string.ascii_letters)
            rando_num = random.randint(0,10)
            password += str(random.choice([rando_letter,rando_num]))

    elif password_strength.lower() == "w":
        for num in range(0,5+1):
            rando_letter = random.choice(string.ascii_letters)
            password += str(rando_letter)

    return password
    
