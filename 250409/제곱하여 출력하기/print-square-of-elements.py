n = int(input())
a = list(map(int, input().split()))
r = [i **2 for i in a]

print(*r)