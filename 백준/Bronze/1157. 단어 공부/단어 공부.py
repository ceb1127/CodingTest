S = input().upper()
s_list = list(set(S))
s_count = []

for i in s_list :
    s_count.append(S.count(i))    
    
if s_count.count(max(s_count)) >= 2:
    print("?")
else:
    print(s_list[(s_count.index(max(s_count)))])

