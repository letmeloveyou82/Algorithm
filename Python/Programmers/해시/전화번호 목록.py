def solution(phone_book):
    phone_book.sort()
    dict_phone_book = dict()
    for i in range(len(phone_book)):
        n = len(phone_book[i])
        for j in range(n):
            if dict_phone_book.get(phone_book[i][0:j+1]) != None:
                return False
        dict_phone_book[phone_book[i]] = 0
    return True