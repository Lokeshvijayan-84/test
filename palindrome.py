num=int(input("plz enter the number: "))
temp=num
rev=0
while num>=1:
    dig=num%10
    rev=rev*10+dig
    num//=10
if temp==rev:
    print("givwn num is palindrome")
else:
    print("given num is not a palindrome")
        
