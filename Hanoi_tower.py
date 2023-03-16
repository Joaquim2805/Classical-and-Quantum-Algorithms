

def hanoi(A,B,C,n):
    if n !=0:
        if n == 1:
            print("Moove disk of",A,"on",C)
        else:
            hanoi(A,C,B,n-1)
            print("Moove disk of",A,"on",C)
            hanoi(B,A,C,n-1)


hanoi("A","B","C",2)