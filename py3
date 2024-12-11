class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 1 or len(list(set(nums))) == 1:
            return length
        nums.sort()
        max_s, factor = 1, 2 * k
        l = 0
        for r in range(length):
            if nums[r] - nums[l] <= factor:
                max_s = max(max_s, r - l + 1)
            else:
                l += 1
        return max_s
