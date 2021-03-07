学习笔记

布隆过滤器和LRU Cache
布隆过滤器
HashTable + 拉链存储重复元素
Bloom Filter vs Hash Table
一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。

优点是空间效率和查询时间都远远超过一般的算法，
缺点是有一定的误识率和删除困难。

LRU Cache
两个要素：大小、替换策略
Hash Table + Double LinkedList
O(1)查询
O(1)修改、更新

class LRUCache:

    def __init__(self, capacity: int):
        #结合了哈希表与双向链表的数据结构OrderedDict
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  #key as the newest one
        return v
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

高阶动态规划
小结提纲
1 动态规划复习；附带递归、分治
2 多种情况的动态规划的状态转移方程串讲
3 进阶版动态规划的习题
分治+记忆化缓存 == 动态规划

DP顺推公式
function DP():
  dp = [][]  #二维情况
  for i in range(m):
    for j in rang(n):
      dp[i][j] = function(dp[i'][j']...)
  return dp[M][N]

爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        #dp求解
        """
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]


最小路径和

定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

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

编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        #dp[i][j]代表word1的前i-1个字符的子串与word2的前j-1个字符的子串的编辑距离
        #若最右边的字符不同，则通过一次增删或者替换操作
        #转移方程的理解(从word1变成word2)
        #dp[i-1][j]:删除
        #dp[i][j-1]:插入
        #dp[i-1][j-1]:替换
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:#边界条件，任一字符为空
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


排序算法
初级排序和高级排序的实现和特性
1 比较类排序：时间复杂度不能突破O（nlogn），因此也称为非线性时间比较类排序
2 非比较类排序：对于整型相关的数据类型，线性时间，辅助额外内存空间
快速排序（Quick Sort）
数组取标杆pivot，将小元素放在pivot左边，大元素放右边，然后依次对右边和右边的子数组继续快排；以达到整个序列有序。
def qick_sort(begin, end, nums):
    if begin >= end:
        return 
    pivot_index = partition(begin, end, nums)
    qick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)

def partition(begin, end,nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
归并排序（Merge Sort）
“快排的逆向操作”
归并排序（Merge Sort） —— 分治
1 把长度为n的输入序列分成两个长度为n/2的子序列；
2 对这两个子序列分别采用归并排序；
3 将两个排序好的子序列合并成一个最终的排序序列。
def mergesort(nums, left, right):
    if right <= left:
        return 
    mid = (left + right) >> 1   #(left + right) / 2
    mergesort(nums, left, mid)
    mergesort(nums, mid + 1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left #第一段数组开始的下标
    j = mid+1 #第二段数组开始的下标
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left:right+1] = temp
堆排序（Heap Sort）
1 数组元素依次建立小顶堆
2 依次取堆顶元素，并删除
特殊排序O(n)
计数排序
桶排序
基数排序


高级字符串算法
最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #很快可以判断的情况
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        #dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        #dp[i][j]代表word1的前i-1个字符的子串与word2的前j-1个字符的子串的编辑距离
        #若最右边的字符不同，则通过一次增删或者替换操作
        #dp[i-1][j]:删除
        #dp[i][j-1]:插入
        #dp[i-1][j-1]:替换
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1#只能等于1
        start = 0
        for j in range(1, size):
            for i in range(0, j):

                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

