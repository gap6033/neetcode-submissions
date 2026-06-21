class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if flowerbed[i] == 0:
                if i - 1 < 0:
                    if i + 1 == len(flowerbed):
                        n -= 1
                        flowerbed[i] = 1
                    elif flowerbed[i + 1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i - 1] == 0:
                        if i + 1 == len(flowerbed):
                            n -= 1
                            flowerbed[i] = 1
                        elif flowerbed[i + 1] == 0:
                            n -= 1
                            flowerbed[i] = 1
        if n:
            return False
        return True



