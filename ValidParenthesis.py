class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None] * len(s)
        pointer = 0

        print("Starting Values")
        print(stack)
        print(pointer)
        print("----------------")

        for i in range(len(s)):
            if s[i] in "([{":
                stack[pointer] = s[i]
                pointer += 1
                print("Opening Bracket logic")
                print(f"Stack = ", stack)
                print(f"Pointer = ", pointer)
                print(f"s[{i}] = ", s[i])
                print("----------------")
            if s[i] in ")]}":
                if pointer == 0:
                    return False
                elif s[i] == ")" and stack[pointer - 1] != "(":
                    print("Closing Bracket Logic")
                    print(f"Stack[pointer - 1] = {stack} does not equal s[i] = {s[i]} so false")
                    print(f"Stack = ", stack)
                    print(f"Pointer = ", pointer)
                    print(f"s[{i}] = ", s[i])
                    print("----------------")
                    return False
                elif s[i] == "]" and stack[pointer - 1] != "[":
                    print("Closing Bracket Logic")
                    print(f"Stack[pointer - 1] = {stack} does not equal s[i] = {s[i]} so false")
                    print(f"Stack = ", stack)
                    print(f"Pointer = ", pointer)
                    print(f"s[{i}] = ", s[i])
                    print("----------------")
                    return False
                elif s[i] == "}" and stack[pointer - 1] != "{":
                    print("Closing Bracket Logic")
                    print(f"Stack[pointer - 1] = {stack} does not equal s[i] = {s[i]} so false")
                    print(f"Stack = ", stack)
                    print(f"Pointer = ", pointer)
                    print(f"s[{i}] = ", s[i])
                    print("----------------")
                    return False
                else:
                    pointer -= 1
                    print("Closing Bracket Match")
                    print(f"Stack = ", stack)
                    print(f"Pointer = ", pointer)
                    print(f"s[{i}] = ", s[i])
                    print("----------------")

        print("Matching Parenthesis")
        print(f"Stack = ", stack)
        print(f"Pointer = ", pointer)
        return pointer == 0

if __name__ == "__main__":
    import sys

    print(Solution().isValid(sys.argv[1]))