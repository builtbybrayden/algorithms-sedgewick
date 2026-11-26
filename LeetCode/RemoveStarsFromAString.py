class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for i in range(len(s)):
            if s[i] != "*":
                output.append(s[i])
            elif s[i] == "*":
                output.pop()

        return "".join(output)

if __name__ == "__main__":
    import sys #Useage: python3 RemoveStarsFromAString.py "leet**cod*e"

    sumList = [str(arg) for arg in sys.argv[1:]]
    print(Solution().removeStars("".join(sumList)))