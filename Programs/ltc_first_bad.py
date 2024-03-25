# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import random

A = 1
B = 10

bad_map = {}
bad_found = False
for num in range(A, B+1):
    if not bad_found:
        bad_found = random.randint(1,2) == 1
    
    if bad_found:
        bad_map[num] = True
    else:
        bad_map[num] = False

def isBadVersion(n: int) -> bool:
    return bad_map[n]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        mid = 0
        high = n
        while low <= high :
            print(f"low {low}\tmid {mid}\thigh {high}")
            mid = (high+low) // 2
            if isBadVersion(mid):
                if mid-1 == 0 or not isBadVersion(mid-1):
                    return mid
                high = mid - 1

            else:
                low = mid + 1


s = Solution()

print(s.firstBadVersion(B))
