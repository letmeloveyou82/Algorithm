def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def quad(x, y, n):
        first = arr[x][y]
        
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != first:
                    n //= 2
                    quad(x, y, n)
                    quad(x, y+n, n)
                    quad(x+n, y, n)
                    quad(x+n, y+n, n)
                    return
        answer[first] += 1
    
    quad(0, 0, n)
    return answer