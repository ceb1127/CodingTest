def solution(s):
    answer = ''
    text = s.split(' ')
    for i in range(len(text)):
        text[i] = text[i].capitalize()
        answer = ' '.join(text)
    return answer