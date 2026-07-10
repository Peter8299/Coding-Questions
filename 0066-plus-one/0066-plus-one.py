class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num,p=0,1
        for i in digits[::-1]:
            num+=i*p
            p*=10
        num+=1
        digits=[]
        while num:
            digits.append(num%10)
            num//=10
        return digits[::-1]