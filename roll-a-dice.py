import random

response = input("Enter y to start")
response = "y"

while response == "y":
    no = random.randint(1, 6)
    
    if(no==1) :
        print("[-----]")
        print("O")
        print("[-----]")

    if(no==2) :
        print("[-----]")
        print("O  O")
        print("[-----]")

    if(no==3) :
        print("[-----]")
        print(" O ")
        print("O O")
        print("[-----]")

    if(no==4) :
        print("[-----]")
        print("O O")
        print("O O")
        print("[-----]")

    if(no==5) :
        print("[-----]")
        print("O O O")
        print("O O")
        print("[-----]")

    if(no==6) :
        print("[-----]")
        print("O O O")
        print("O O O")
        print("[-----]")

response = input("Press y to continue, or press n to exit")
print("\n")

