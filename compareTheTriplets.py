alice = list(map(int, input().split()))
bob = list(map(int, input().split()))
countA = 0
countB = 0
if len(alice) != 3 or len(bob) != 3:
    print('Error')
else:
    for i in range(3):
        if alice[i] > bob[i]:
            countA += 1
        elif alice[i] < bob[i]:
            countB += 1

print(str(countA)+" "+str(countB))
