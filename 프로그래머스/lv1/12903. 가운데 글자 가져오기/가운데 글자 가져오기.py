def solution(s):
    s = list(s)
    lenX = len(s)//2
    if len(s)%2 != 0 :
        return s[lenX]
    else : 
        answer = ''.join(s[lenX-1:lenX+1])
        return answer
    
'''
4 -> 1,2 0 12 3 -> 2-1:2
6 -> 2,3 01 23 45 -> 3-1:3
8- > 3,4 012 34 567 -> 4-1: 4
'''