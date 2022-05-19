class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums),1):
            v = target-nums[i]
            if v in nums:
                if i!=nums.index(v):
                    return[i,nums.index(v)]