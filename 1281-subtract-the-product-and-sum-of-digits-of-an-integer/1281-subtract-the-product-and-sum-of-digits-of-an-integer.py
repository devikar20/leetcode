class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        product=1
        sum=0
        while temp>0:
            a=temp%10
            b=temp%10
            temp//=10
            product=product*a
            sum=sum+b
        return (product-sum)
        