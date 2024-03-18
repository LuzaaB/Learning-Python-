nums = [0,1,0,3,12]
zero = []
n = len(nums)
for each in nums:
    if each == 0:
        zero.append(each)
nums = list(set(nums))
nums.remove(0)
nums = nums + zero
print(nums)