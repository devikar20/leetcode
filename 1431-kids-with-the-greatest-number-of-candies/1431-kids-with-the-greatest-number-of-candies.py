class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maximum=candies[0]
        for j in range(1,len(candies)):
           if candies[j]>maximum:
                maximum=candies[j]
          
             
        for i in range (len(candies)):
            a=candies[i]+extraCandies
            if a>=maximum:
                result.append(True)
            else:
                result.append(False)
        return result

        