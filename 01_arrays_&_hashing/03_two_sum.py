from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[num] = i

if __name__ == '__main__':
    nums = [1,2,3,4]

    for i, num in enumerate(nums):
        print(i, num)