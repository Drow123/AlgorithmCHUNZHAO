1. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False
        
        for k in dic.values():
            if k != 0:
                return False
        return True


2. 字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回-1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1

3. 翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

class Solution:
    def reverseWords(self, s: str) -> str:
        #使用 split 将字符串按空格分割成字符串数组；
        #使用 reverse 将字符串数组进行反转；
        #使用 join 方法将字符串数组拼成一个字符串。
        return " ".join(reversed(s.split()))

4. 最长回文子串

给你一个字符串s，找到s中最长的回文串。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #枚举中心，向两边扩散
        n = len(s)
        if n < 2:
            return s
        res = s[0]
        def extend(i, j, s):
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1: j]

        for i in range(n - 1):
            e1 = extend(i, i, s) #奇数
            e2 = extend(i, i + 1, s) #偶数
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res

5. 最长有效括号

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


6. LRU Cache

class LRUCache:

    def __init__(self, capacity: int):
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
