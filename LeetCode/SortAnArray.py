class Solution:

    aux = []

    def sort(self, nums: list[int]) -> None:
        self.aux = [0] * (len(nums))
        self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums: list[int], lo: int, hi: int) -> None:
        if hi <= lo: 
            return
        
        mid = lo + (hi - lo) // 2
        self._sort(nums, lo, mid)
        self._sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums: list[int], lo: int, mid: int, hi: int) -> None:
        for k in range(lo, hi + 1):
            self.aux[k] = nums[k]
        
        i = lo 
        j = mid + 1

        for k in range(lo, hi + 1):
            if i > mid:                                 
                nums[k] = self.aux[j]
                j +=1
            elif j > hi:                                
                nums[k] = self.aux[i]
                i += 1
            elif (self.less(self.aux[j], self.aux[i])): 
                nums[k] = self.aux[j]
                j += 1
            else:                                       
                nums[k] = self.aux[i]
                i += 1

    def less(self, v: int, w: int) -> bool:
        return self.compareTo(v, w) < 0

    def compareTo(self, a: int, b: int) -> int:
        return (a > b) - (a < b)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.sort(nums)
        return nums

if __name__ == "__main__":
    import sys #Useage: python .\SortAnArray.py 3 5 7 5 4 2

    listToSort = [int(arg) for arg in sys.argv[1:]]
    print(Solution().sortArray(listToSort))