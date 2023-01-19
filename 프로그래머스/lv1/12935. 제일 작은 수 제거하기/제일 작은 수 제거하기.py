def solution(arr):
    if len(arr) == 1 : return [-1] 
    else : 
        minX = sorted(arr).pop(0)
        arr.remove(minX)
        return arr
        