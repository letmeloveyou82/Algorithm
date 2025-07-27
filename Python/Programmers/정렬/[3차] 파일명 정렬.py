def solution(files):
    new_files = []
    for file in files:
        head = 0
        number = 0
        tail = len(file) # 없을 수도 있어서 초기값 file 길이로 해줘야 함
        for i in range(len(file)):
            if file[i].isdecimal() and number == 0:
                number = i
            elif not file[i].isdecimal() and number != 0:
                tail = i
                break

        new_files.append([file[head:number], file[number:tail], file[tail:]])

    new_files = sorted(new_files, key=lambda x : (x[0].lower(), int(x[1])))

    for i in range(len(new_files)):
        h, n, t = new_files[i]
        new_files[i] = h+n+t
    
    return new_files