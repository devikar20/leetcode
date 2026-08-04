class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if (nums[i]%2!=0 and nums[j]%2==0):
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    j=j+1
                    i=i+1
                
                else:
                    j=j+1
                   
        return nums

        