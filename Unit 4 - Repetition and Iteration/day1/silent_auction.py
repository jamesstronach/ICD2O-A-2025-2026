N = int(input())

nameBiggest = input()
bidBiggest = int(input())

for i in range(N-1):
    name = input()
    bid = int(input())
    if bid > bidBiggest:
        bidBiggest = bid
        nameBiggest = name

print(nameBiggest)