def reverse_and_print_positions(arr):
    reversed_arr=arr[::-1]
    even_positions=[str(reversed_arr[i]) for i in range(1,len(reversed_arr),2)]
    odd_positions=[str(reversed_arr[i])for i in range(0,len(reversed_arr),2)]
 
    even_str=" ".join(even_positions)
    odd_str=" ".join(odd_positions)
    print(f"odd positions:{odd_str}")
    print(f"even positions:{even_str}") 
arr=[8,3,4,1,6,2]
reverse_and_print_positions(arr)    