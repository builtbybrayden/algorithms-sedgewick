class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        oddSubarrays = 0
        sum = 0
        evenCount = 1
        oddCount = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1

        oddSubarrays = oddCount * evenCount
        return oddSubarrays

if __name__ == "__main__":
    import sys #Useage: python .\SortAnArray.py 8 3 5 7 5 4 2 where 8 is the target and the following numbers are the list

    sumList = [int(arg) for arg in sys.argv[1:]]
    print(Solution().numOfSubarrays(sumList))