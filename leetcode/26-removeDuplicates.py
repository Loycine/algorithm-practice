from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        last_value = nums[0]
        length = 1
        for i in range(1, n):
            if nums[i] != last_value:
                last_value = nums[i]
                nums[length] = nums[i]
                length = length +1
        
        return length
 