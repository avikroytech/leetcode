class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        
        previous = -1
        peaked = False
        peakIndex = arr.index(max(arr))

        if len(arr[peakIndex+1:]) == 0 or len(arr[:peakIndex]) == 0:
            return False

        for num in arr:
            if num > previous and not peaked:
                previous = num
            elif num < previous:
                previous = num
                if not peaked:
                    peaked = True
            elif num == previous:
                return False
            elif num > previous and peaked:
                return False
        
        return True