import copy
nums = [5 , 10 , 15 , 20 , 25]

total = sum(nums)
bigger = max(nums)

reversed_nums = copy.deepcopy(nums)
reversed_nums.reverse()

print(f"The sum of the numbers : {total}")
print(f"The max number in the numbers : {bigger}")
print(f"The reversed version of the numbers : \n{reversed_nums}")