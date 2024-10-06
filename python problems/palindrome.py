def ispalindrome(num):
    palindrome=num
    reverse=0
    while palindrome!=0:
        rem=palindrome%10
        reverse=reverse*10+rem
        palindrome=palindrome//10
    return num==reverse
if __name__=='__main__':
    number=int(input("enter a number:"))    
if ispalindrome(number):
    print("yes the number is palindrome")
else:
    print("the number is not palindrome")    