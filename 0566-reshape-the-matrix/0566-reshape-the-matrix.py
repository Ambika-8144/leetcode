class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        arr = []

        for row in mat:
            for num in row:
                arr.append(num)

        ans = []
        index = 0

        for _ in range(r):
            ans.append(arr[index:index+c])
            index += c

        return ans