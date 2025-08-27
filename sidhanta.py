
print("!.....WEL_COME TO THE NUMBER GUSSING ......!");

import random
count=0
while True:
    
    system=random.randint(1,100)
    print(system)

    user=int(input("Enter the number: "))

    if(system==user):
        print("you won..!")
        count+=1
    elif(user==0):
        print("!...THANK'S FOR PLAYING THIS GAME..!")
        break
    else:
        print("you loss.!")
        count-=1
    print(count)
