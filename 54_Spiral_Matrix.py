from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        m, n = len(matrix), len(matrix[0])
        if m==1:
            return matrix[0]
        num = m * n
        index_list = []
        if n==1:
            for i in range(m):
                index_list.append(matrix[i][0])
            return index_list
        start_n, end_n = 0, n - 1
        start_m, end_m = 0, m - 1
        while True:
            if num < 1:
                return index_list
            # right
            for i in range(start_n, end_n+1):
                if num<1:
                    return index_list
                index_list.append(matrix[start_m][i])
                num -= 1
            start_m += 1
            # down
            for i in range(start_m, end_m+1):
                if num<1:
                    return index_list
                index_list.append(matrix[i][end_n])
                num -= 1
            end_n -= 1
            # left
            for i in range(end_n, start_n-1, -1):
                if num<1:
                    return index_list
                index_list.append(matrix[end_m][i])
                num -= 1
            end_m -= 1
            # up
            for i in range(end_m, start_m-1, -1):
                if num<1:
                    return index_list
                index_list.append(matrix[i][start_n])
                num -= 1
            start_n += 1



matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
matrix = [[2,5],[8,4],[0,-1]]
matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix = [[3],[2]]
matrix=[[6,9,7]]
matrix = [[6],[9],[7]]
matrix = [[1,2],[3,4]]
print(Solution().spiralOrder(matrix))