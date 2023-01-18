def solution(x):
    answer = True
    arr = list(map(int, str(x)))
    int_arr = int(''.join(map(str,arr)))
    sum_arr = sum(arr[i] for i in range(len(arr)))
    if (int_arr % sum_arr ) == 0 :
        return answer
    else: 
        return False 