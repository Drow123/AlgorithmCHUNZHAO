1. 编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def dp(i, j):
            #如果有一个字符串是空串
            if i * j == 0:
                return i + j
            #如果最后一个字符相等，则不用进行操作
            elif word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)
            else:
            #否则，就挑插入、删除、替换中最少操作数
                return min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
        return dp(len(word1), len(word2))

2. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #处理特殊情况
        if not grid or not grid[0]:
            return 0
        #dp数组初始化
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        #行
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        #列
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        #状态转移方程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


3. 解码方法

class Solution:
    def numDecodings(self, s: str) -> int:

        #边界条件
        if s[0] == '0': return 0
        #dp数组
        n = len(s)
        dp = [0]*(n + 1)
        dp[0],dp[1]=1, 1
        for i in range(1,n):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i+1] = dp[i-1]
            else:
                if s[i-1] == "1" or (s[i-1] == "2" and "1" <= s[i] <= "6"):
                    dp[i+1] = dp[i] +dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[n]



4. 最大正方形

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #特判
        if not matrix:
            return 0
        #定义dp数组
        #dp[i][j]表示以第i行，第j列处为右下角的最大正方形的边长
        #仅当该位置为1时，才有可能存在正方形，且递推公式为：
        #dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        #若当前位置为1，则此处可以构成的最大正方形的边长，是其正上方，左侧，和左上界三者共同约束的，且为三者中的最小值加1。
        #边界条件和特殊情况需要处理
        m, n = len(matrix), len(matrix[0])
        #初始化最大边长0
        res = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    res = max(dp[i][j], res)
        return res*res


5. 回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    res += 1
        return res



6. 最长有效括号

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:return 0
        dp = [0]*n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ")" and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1]- 1] == "(":
                    dp[i] = dp[i-1] + 2 + dp[i- dp[i-1]-2]
                if dp[i] > res:
                    res = dp[i]
        return res
