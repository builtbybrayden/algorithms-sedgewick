class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result = []
        
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                result.append(asteroids[i])
            elif asteroids[i] < 0:
                while True:
                    if not result:
                        result.append(asteroids[i])
                        break
                    else:
                        compare = result.pop()
                        if compare < 0:
                            result.append(compare)
                            result.append(asteroids[i])
                            break
                        elif compare > abs(asteroids[i]):
                            result.append(compare)
                            break
                        elif compare == abs(asteroids[i]):
                            break

        return result

if __name__ == "__main__":
    import sys #Useage: python3 AsteroidCollision.py 5 10 -5

    asteroids = [int(arg) for arg in sys.argv[1:]]
    print(Solution().asteroidCollision(asteroids))