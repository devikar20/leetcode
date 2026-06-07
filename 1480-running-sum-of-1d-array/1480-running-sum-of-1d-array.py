class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[nums[0]]
        k=nums[0]
        for i in range(1,len(nums)):
            k=k+nums[i]
            result.append(k)
        return result
        