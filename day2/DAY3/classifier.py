def check_odd_even(n):
    if n % 2==0:
         print ("is even")
    else :
        print("is odd")





numbers  = [4,5,6,7]
total_even = 0
total_odd=0
for num in numbers:
    result = check_odd_even(num)
    print(f"{num} is {result}")
    if result == "even": total_even+=1
    else:total_odd += 1


print("total_even",total_even)
print("total_odd",total_odd)