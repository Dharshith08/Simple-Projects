import random
a = random.randint(0 , 100)
c = 3
while c > 0:
    print("You have",c,"Lives left")
    b = int(input("Guess a number from (0 to 100):"))
    print("The numbwe you entered is \"CORRECT\"") if a == b else None
    if a != b:
        c -= 1
        print("The number you entered is \"WRONG\" Try again",c,"Tries remaining")
    if c == 0:
        print("The lives ended try again and by the way",a,"this is the answer.")