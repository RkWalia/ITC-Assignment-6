#Ques4

def f(x):
    Pangrams="abcdefghijklmnopqrstuvwxyz"
    for char in Pangrams:
        if char not in x:
            return False
        else:
            return True


string=input("Enter a string: ")

if f(string)==True:
    print("Given string is a Pangram.")
else:
    print("a string is not a Pangram.")