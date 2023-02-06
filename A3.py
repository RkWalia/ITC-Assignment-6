#Ques6


def PascalTriangle(n):
    row=[1]
    y=[0]
    for i in range(max(n,0)):
        print(row)
        row=[l+x for l,x in zip(y+row,row+y)]
    return n>=1


ROWS=int(input("Enter number of rows= "))
PascalTriangle(ROWS)