class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            k=0
            j=0
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    k+=1
            
            ans.append(k)
        return ans


        