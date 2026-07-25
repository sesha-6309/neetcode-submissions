class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       if len(nums)==0:
         return False
       k = min(nums)
       l = max(nums)
       si = l - k + 1
       rr = si-1

       listk = [0]*si
       for i in range(len(nums)):
         rrr = rr - (l-nums[i])
         listk[rrr]+=1
       for j in listk:
         if j>1:
          return True
       return False 
       

            