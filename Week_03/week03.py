1. 买卖股票的最佳时机II

#使用贪心来进行计算
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit


2. 分发饼干

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #贪心算法
        #胃口排序，饼干尺寸排序
        g.sort()
        s.sort()
        i, j = 0, 0
        #当没有遍历完时
        while i < len(g) and j < len(s):
            #如果刚好把小的胃口喂饱，胃口值++，如果不能喂饱，那饼干尺寸不够，需要更大，所以j++
            if g[i] <= s[j]:
                i += 1
            j += 1
        #返回孩子的最大数
        return i


3. Pow(x, n) 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickpow(x, n):
            #终止条件
            if n == 1: return x
            if n == 0: return 1
            #定义分治后的乘积
            y = quickpow(x, n // 2)
            #偶数时直接y的平方
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x
        #当指数小于0时，转换下
        if n < 0:
            return 1 / self.myPow(x, -n)
        return quickpow(x, n)


4. 子集（迭代和回溯解法）

#对于回溯的理解还不够明朗
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        #迭代的算法，这代码绝了
        for i in nums:
            res = res + [[i] + j for j in res]
        return res


5. 搜索旋转排序数组

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

"""
当[0, mid] 序列是升序: nums[0] <= nums[mid], 当target > nums[mid] || target < nums[0] ,则向后规约
当[0, mid] 序列存在旋转位: nums[0] > nums[mid],当target < nums[0] && target > nums[mid],则向后规约
当然其他其他情况就是向前规约了
看着例子比较容易懂nums = [4,5,6,7,0,1,2], target = 0
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #套用二分模板
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #向右边找
            if (target < nums[left] <= nums[mid]) or(nums[left] <= nums[mid] < target) or (nums[mid] <= target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        return -1


6. 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r","s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y","z"]
        }
        if digits == "":
            return []
        res = []
        chain= []
        self.dfs(digits, 0, chain, res)
        return res

    def dfs(self, digits, cur, chain, res):
        #递归终止条件
        if cur == len(digits):
            chain = "".join(chain)
            res.append(chain)
            return
        #遍历节点
        for char in self.map[digits[cur]]:
            chain.append(char)
            cur += 1
            self.dfs(digits, cur, chain, res)
            cur -= 1
            chain.pop()


