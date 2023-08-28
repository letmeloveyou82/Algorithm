vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()
    if password == "end":
        break
    else:
        include_vowel = False
        result = True
        # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        for i in range(len(password)):
            if password[i] in vowel:
                include_vowel = True
                break
        if not include_vowel:
            print(f"<{password}> is not acceptable.")
            continue
        # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        for i in range(len(password)-2):
            if password[i] in vowel and password[i+1] in vowel and password[i+2] in vowel:
                result = False
                break
            elif password[i] not in vowel and password[i+1] not in vowel and password[i+2] not in vowel:
                result = False
                break
        if not result:
            print(f"<{password}> is not acceptable.")
            continue
        # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        for i in range(len(password)-1):
            if password[i] == password[i+1] and password[i] != 'e' and password[i] != 'o':
                result = False
                break
        if not result:
            print(f"<{password}> is not acceptable.")
        else:
            print(f"<{password}> is acceptable.")