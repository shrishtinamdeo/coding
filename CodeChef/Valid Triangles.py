# Problem Statement: https://www.codechef.com/problems/FLOW013

# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if A+B+C==180:
        print("YES")
    else:
        print("NO")