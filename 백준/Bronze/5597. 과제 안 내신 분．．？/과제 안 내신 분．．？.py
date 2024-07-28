student = [i for i in range(1, 30+1)]
for i in range(28):
    n = int(input())
    
    if n in student:
        student.remove(n)
    
print(min(student))
print(max(student))