def min_char_to_make_palin(n,s):
    def is_palindrome(st):
        return st==st[::-1]
        if is_palindrome(s):
            print("NULL")
            return
        for i in range(n):
            if is_palindrome(s[i:]):
                to_append=s[:i][::-1]
                print(to_append)
                return
n=int(input())            
s=input()