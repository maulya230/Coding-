class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    arr.append(i)
                    arr.append(j)
        return arr
