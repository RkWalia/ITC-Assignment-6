#Ques2

def f(x):
    if x==x[::-1]:
        return "Given string is a Palindrome."
    else:
        return "Given string is not a Palindrome."


string=input("Enter a srting= ")
print(f(string))