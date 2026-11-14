class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        min = None
        for length in range(l, r+1):
            for start in range(len(nums) - length + 1):
                sum = 0
                for index in range(start, start + length):
                    sum += nums[index]

                if sum > 0 and (min is None or sum < min):
                    min = sum

        return -1 if min is None else min

if __name__ == "__main__":
    import sys #Useage: python .\SortAnArray.py 8 3 5 7 5 4 2 where 8 is the target and the following numbers are the list

    l = int(sys.argv[1])
    r = int(sys.argv[2])
    sumList = [int(arg) for arg in sys.argv[3:]]
    print(Solution().minimumSumSubarray(sumList, l, r))