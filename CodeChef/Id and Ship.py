# Problem Statement : https://www.codechef.com/problems/FLOW010

# cook your dish here
T=int(input())
for i in range(T):
    ClassID=input()
    if ClassID=="B" or ClassID=="b":
        print("BattleShip")
    elif ClassID=="C" or ClassID=="c":
        print("Cruiser")
    elif ClassID=="D" or ClassID=="d":
        print("Destroyer")
    else:
        print("Frigate")