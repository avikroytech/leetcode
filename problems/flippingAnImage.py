class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        newImage = []
        for i in range(len(image)):
            newRow = image[i][::-1]
            for i in range(len(newRow)):
                if newRow[i] == 1:
                    newRow[i] = 0
                else:
                    newRow[i] = 1
            
            newImage.append(newRow)

        return newImage