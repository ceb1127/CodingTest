def solution(s):
    s = list(map(str, str(s).lower()))

    if s.count('p') == s.count('y') :
        return True
    else : 
        return False
