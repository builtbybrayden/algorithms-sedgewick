class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == "__main__":
    import sys #Useage: python .\SortAnArray.py 8 3 5 7 5 4 2 where 8 is the target and the following numbers are the list

    target = int(sys.argv[1])
    twoSumList = [int(arg) for arg in sys.argv[2:]]
    print(Solution().twoSum(twoSumList, target))