1. 位1的个数

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）

class Solution:
    def hammingWeight(self, n: int) -> int:
        #return bin(n).count('1')
        #二进制中最低位的1会通过n-1操作消失，而比最低位1高的位不变，通过n&=n-1保留剩余高位的1及低位的0；
        #示例：n=12，其二进制为1100，n-1为1011，n&(n-1)为1000，消掉了最低位的1
        #时间复杂度：O(1)，n为32位的数，操作次数为二进制中1的个数
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

2. 2的幂

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #转换为2进制则只有一个1
        return (n>0) and (n &(n-1)==0)

3. 颠倒二进制位

class Solution:
    def reverseBits(self, n):
        #bin()返回一个整数int或者长整数long int的二进制表示，前面会带有“0b”
        #zfill()方法返回指定长度的字符串，原字符串右对齐，前面填充0
        #最后还是转换为2进制
        return int(bin(n)[2:].zfill(32)[::-1], base=2)


#通过位运算实现，取出n的最低位，加入结果res中。然后n右移，res左移。循环此过程。
class Solution：
    def reverseBits(self, n):
        res = 0
        count = 32

        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n&1
            n >>= 1
            count -= 1

        return int(bin(res), 2)


4. 实现Trie（前缀树）

实现一个Trie（前缀树），包含insert，search，和startsWith这三个操作。

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


5. 括号生成

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l, r, s):
            #当左右括号的数量为n时，结束递归
            if l == r == n:
                res.append(s)
            #当左括号个数小于n时，则添加左括号
            if l < n:
                dfs(l + 1, r, s + "(")
            #当右括号个数小于左括号个数时，添加右括号
            if r < l:
                dfs(l, r + 1, s + ")" )
        dfs(0, 0 , '')
        return res

6. 比特位计数

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

输入: 2
输出: [0,1,1]

#迭代统计每个数二进制位为1的个数
#n = n & (n-1)方式消掉二进制最低位的1，累计次数直到n为0
#时间复杂度O(nk)
class Solution:
    def countBits(self, num: int) -> List[int]:
        def bin_count(n):
            count=0
            while n:
                n&=n-1
                count+=1
            return count

        res=[]
        for i in range(num+1):
            res.append(bin_count(i))
        return res

#时间复杂度O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            dp[i]=dp[i&(i-1)]+1
        return dp



