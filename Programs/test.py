nums = [1,2,3,4,5,6,7,8,9]
n = len(nums)
num_dict = {}
def f(li):
    for each in li:
        if each in num_dict:
            num_dict[each] += 1
        else:
            num_dict[each] = 1        
    for key, val in num_dict.items():
        # print (type(val))
        if val > 1:
            return True
    return False

result = f(nums)