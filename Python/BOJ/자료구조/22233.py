import sys
input = sys.stdin.readline
n, m = map(int, input().split()) 
keyword = set()
for _ in range(n):
    keyword.add(input().rstrip())

for _ in range(m):
    new_post = set(input().rstrip().split(','))
    keyword-=new_post
    print(len(keyword))