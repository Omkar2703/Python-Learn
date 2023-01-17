n = int(input("Enter the number: "))
ans = 0
while n!=0:
    ans = ans*10+n%10
    n//=10 #can also written as n =int(n/10)
print("Reverse of the given number is ", str(ans))
