class Solution:
    def isUgly(self, n: int) -> bool:
        factors = []
        if n == 1:
            return True

        for i in range(2,n):
            if n % i == 0:
                factors.append(i)

        factors = set(factors)
        prime_factors = []
        count = 0
        for each in factors:
            # [a, b)
            for i in range(2,each+1):
                if each%i == 0:
                    count += 1
            if count == 1:
                prime_factors.append(each)

            count = 0
        
        f_len = len(prime_factors)    
        if f_len <= 3:

            # DRY - dont repeat yourself

            if prime_factors == [2]:
                return True
            elif prime_factors == [3]:
                return True
            elif prime_factors == [5]:
                return True
            elif prime_factors == [2,3]:
                return True
            elif prime_factors == [2,5]:
                return True
            elif prime_factors == [2,3,5]:
                return True
            elif prime_factors == [3,5]:
                return True
            
        return False

s = Solution()
print(s.isUgly(8))