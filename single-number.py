class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_list = []
        for num in nums:
            if num in num_list:
                num_list.remove(num)
            else:
                num_list.append(num)
        return num_list[0]