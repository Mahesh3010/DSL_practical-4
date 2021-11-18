total = 0
while True:
    A = input()
    if A == "":
     break   
    else:
        A = A.split(" ")
        if A[0] == "D":
            total = total + int(A[1])
        elif A[0] == "W":
            total = total - int(A[1])
            if total<=0:
               print("your balance isnot sufficient",total)
   
print(total)