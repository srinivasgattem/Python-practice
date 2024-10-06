MOD=10**9+7
def count_vowel_permutation(n):
    a_count=e_count=i_count=o_count=u_count=1
    for _ in range(1,n):
        new_a_count=(e_count+i_count+u_count)%MOD
        new_e_count=(a_count+i_count)%MOD
        new_i_count=(e_count+o_count)%MOD
        new_o_count=i_count%MOD
        new_u_count=(i_count+o_count)%MOD
    
        a_count=new_a_count
        e_count=new_e_count
        i_count=new_i_count
        o_count=new_o_count
        u_count=new_u_count
    return(a_count+e_count+i_count+o_count+u_count)%MOD
n=int(input("enter the length of the string "))
print(count_vowel_permutation(n))    
          