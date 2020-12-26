# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        result = dim[1]
        for i in range(dim[0]):
            left = 0
            right = result - 1
            if binaryMatrix.get(i,right) == 0:
                continue
            while left <= right:
                mid = int((left + right)/2)
                if binaryMatrix.get(i,mid) == 0:
                    left = mid + 1
                else:
                    right = mid - 1
            result = min(result,left)
            if result == 0:
                return result
        if result == dim[1]:
            return -1
        else:
            return result