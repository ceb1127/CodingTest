def solution(phone_number):
    tel_back = list(map(str,phone_number))[-4:]

    tel_front = [ '*' for i in range(len(phone_number[:-4]))]
    answer = ''.join(tel_front +  tel_back)
            
    return answer