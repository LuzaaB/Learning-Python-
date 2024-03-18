class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
                
        # nums = set(nums)
        # all_nums = set()
        # for i in range(n):
        #     all_nums.add(i)
        # print("all_nums content :",all_nums)
        # diff = all_nums - nums
        # number = 0
        # for each in diff:
        #     number = each
        # print(number)
        # return number
    
c = Solution()
li = c.missingNumber([9,6,4,2,3,5,7,0,1])