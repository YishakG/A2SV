A = set(map(int, input().split()))
n = int(input())
sets = []
for _ in range(n):
    B = set(map(int, input().split()))
    sets.append(B)
for num in sets:
    if not num < A:
        print(False)
        break
else:
     print(True)
# This is a specific feature in Python that 
# allows you to run a block of code after 
# the loop finishes only if the loop wasn't 
# prematurely exited by a break statement.