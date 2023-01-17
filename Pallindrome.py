def Pallindrome():
    rev = string[::-1]
    if rev==string:
        print(string, " is a pallindrome.")
    else:
        print(string, " is not a pallindrome.")
string = input("Enter the string: ")
Pallindrome()
