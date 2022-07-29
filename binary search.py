class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(0,len(nums)):
                if target==nums[i]:
                    index=i
                 
        else:
            index=-1
        return index
