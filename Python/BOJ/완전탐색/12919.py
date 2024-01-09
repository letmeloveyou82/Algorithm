S = input()
T = input()

def make(str):
    if str == S:
        print(1)
        exit(0)
    if len(str) == 0:
        return 0
    if str[-1] == 'A':
        make(str[:-1])
    if str[0] == 'B':
        make(str[1:][::-1])

make(T)
print(0)