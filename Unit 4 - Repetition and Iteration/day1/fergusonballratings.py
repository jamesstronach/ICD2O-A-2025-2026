N = int(input())

numStarsPlayers = 0

for i in range(N):
    P = int(input())
    F = int(input())

    if P*5-F*3 >= 40:
        numStarsPlayers+=1

gold = ""
if N == numStarsPlayers:
    gold = "+"
print(f"{numStarsPlayers}{'+' if N == numStarsPlayers else ''}")