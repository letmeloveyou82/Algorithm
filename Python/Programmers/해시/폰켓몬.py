from collections import defaultdict
def solution(nums):
    ponkemon = defaultdict(int)
    for i in nums:
        ponkemon[i] += 1
    if  len(ponkemon) <= len(nums)/2:
        return len(ponkemon)
    else:
        return int(len(nums)/2)