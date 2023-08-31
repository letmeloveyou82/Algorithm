import sys
input = sys.stdin.readline
n = int(input())
st = input().strip()

result = []

temp = st.rstrip('R')
result.append(temp.count('R'))

temp = st.rstrip('B')
result.append(temp.count('B'))

temp = st.lstrip('R')
result.append(temp.count('R'))

temp = st.lstrip('B')
result.append(temp.count('B'))

print(min(result))