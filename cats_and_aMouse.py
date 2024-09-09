q = int(input())
for i in range(q):
    pos = list(map(int, input().split()))
    if abs(pos[0]-pos[2]) > abs(pos[1]-pos[2]):
        print("Cat B")
    elif abs(pos[0]-pos[2]) < abs(pos[1]-pos[2]):
        print("Cat A")
    else:
        print("Mouse C")