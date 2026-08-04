class Solution:
   def runningSum(self, nums: List[int]) -> List[int]:
    runsum=[]
    ans=0
    n=len(nums)
    for i in range(0,n):
        ans=ans+nums[i]
        runsum.append(ans)
    return runsum


