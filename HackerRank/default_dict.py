from collections import defaultdict
n , m = map(int, input().split())
N = defaultdict(list)
for i in range(1,n+1):
    word = input()
    N[word].append(i)
for _ in range(m):
    char = input()
    if char in N:
        print(*N[char])        
    else: 
        print(-1)

 