class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastIndex = -1
        matched = 0
        
        if len(t) < len(s):
            return False

        for i in range(len(s)):
            for j in range(lastIndex, len(t)):
                if s[i] == t[j] and lastIndex < j:
                    lastIndex = j
                    matched += 1
                    break
        
        if matched == len(s):
            return True
        else:
            return False


if __name__ == "__main__":
    import sys #Useage: python .\IsSubsequence.py abc agbhnc

    seq1 = str(sys.argv[1])
    seq2 = str(sys.argv[2])
    print(Solution().isSubsequence(seq1, seq2))