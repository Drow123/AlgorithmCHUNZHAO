学习笔记

第一周

数组、链表、跳表

Array

Java, C++  : int a[100]
Python:  list = []
JavaScript : let  x = [1, 2, 3]

Linked  List

时间复杂度
prepend O（1）
append   O（1）
lookup   O（n）
insert    O（1）
delete    O（1）

跳表 Skip List

跳表的特点
注意：只能用于元素有序的情况
所以，跳表（skip list）对标的是平衡树（AVL Tree）和二分查找，是一种 插入/删除/搜索 都是O（logN）的数据结构。1989年出现。

如何给有序的链表加速
添加多级索引

跳表查询的时间复杂度分析
n/2   n/4    n/8    、第k级索引结点的个数就是 n/(2^k)
假设索引有h级，最高级的索引有2个结点。 n/(2^h) = 2, 从而求得h = logN -1
跳表： 升维思想 + 空间换时间

优先队列

插入操作：O（1）
取出操作：O（logN）——按照元素的优先级取出
底层具体实现的数据结构较为多样和复杂：heap、bst（二叉搜索树）、treap

哈希表、映射、集合

hash table
哈希表（hash table），也叫散列表，是根据关键码值（key value）而直接进行访问的数据结构。
他通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
这个映射函数叫做散列函数（hash function），存放记录的数组叫做哈希表（或散列表）。

工程实践

电话号码簿
用户信息表
缓存（LRU Cache）
键值对存储（Redis）

hash function
返回下标，整数，很多种哈希函数

哈希碰撞
再增加一个维度，拉链式解决冲突法


第二周


树、二叉树、二叉搜索树

树和图最关键的点就是有没有环

LInked List 是特殊化的Tree

Tree 是特殊化的Graph

二叉搜索树

二叉搜索树，也称二叉排序树、有序二叉树（ordered binary tree）、排序二叉树（Sorted binary tree），是指一颗空树或者具有下列性质的二叉树：

1 左子树上所有节点的值均小于它的根节点的值
2 右子树上所有节点的值均大于它的根节点的值
3 以此类推：左、右子树也分别为二叉查找树（这就是重复性）

中序遍历：升序排序

二叉搜索树常见操作：O（logN）
1 查询
2 插入新节点（创建）
3 删除（如果是根节点，原则上取与根节点值相近的值，分左右，但默认取第一个大于根节点的值，在右子树里找）
如何进行？会讲解理解就行



堆heap、二叉堆binary heap

heap：可以迅速找到一堆数中的最大或者最小值的数据结构
将根节点最大的堆叫做大顶堆或大根堆，根节点最小的堆叫做小顶堆或小根堆，常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，则常见操作（API）：
find-max：O（1）
delete-max:O(logN)
insert（create）：O（logN）or O（1）

二叉堆性质

实现效率是比较差的，效率好的是：严格的斐波那契堆
通过完全二叉树来实现（注意：不是二叉搜索树）

二叉堆（大顶）它满足下列性质：
1 是一棵完全树
2 树中任意节点的值总是 >= 其子节点的值

二叉堆实现细节
1 二叉堆一般通过（数组）来实现
2 假设“第一个元素”在数组中的索引为0的话，则父节点和子节点的位置关系如下：

0 根节点（顶堆元素）是：a[0]
01 索引为i的左孩子的索引是（2*i+1）
02 索引为i的右孩子的索引是（2*i+2）
03 索引为i的父节点的索引是floor(（i-1）/2)(地板除，取整）

Insert插入操作（O（logN））
1 新元素一律先插入到堆的尾部
2 依次向上调整整个堆的结构（一直到根即可）

Delete Max删除堆顶操作（O（logN））
1 将堆尾元素替换到顶部（即堆顶被替代删除掉）
2 依次从根部向下调整整个堆的结构（一直到堆尾即可）

注意：二叉堆是堆（优先队列priority queue）的一种常见且简单的实现；但并不是最优的实现。

应用：最小的k个数、滑动窗口最大值等问题

	#最小的k个数
	#可以用sort实现，时间复杂度O（NlogN）
	class Solution:
    		def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        		arr.sort()
        		return arr[:k]
 
	#用python的堆（优先队列）,O(nlogK)
	import heapq
	class Solution:
    		def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        	#python使用heapq实现了最小堆
        	#heapq.heapify使得列表具备最小堆特征
        	#heapq.nsmallest(n,heap)方法可返回k个最小值列表
        	heapq.heapify(arr)
        	return heapq.nsmallest(k, arr)
        
	class Solution:
    		def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        		if k==0:
            			return [] 
       			hp = [-x for x in arr[:k]]
        		heapq.heapify(hp)
        		for i in range(k, len(arr)):
            			if -hp[0] > arr[i]:  #如果里面的数大于后面待插入的值的话，就把小的放进去，但是放的时候要取负，使满足大根堆
                			heapq.heappop(hp)
                			heapq.heappush(hp, -arr[i])
        		ans = [-x for x in hp]
        		return ans


#滑动窗口
#优先队列  #双端队列都可以做
解题思路：
1 python默认是小根堆，故加“-”，形成大根堆
2 由于堆顶元素可能不在滑动窗口内，故要维护一个二元组（num， index）
3 通过index判断堆顶元素是否在滑动窗口内
4 首先把k个元素加入大根堆
5 接着模拟滑动窗口右移，把最新的元素加入大根堆，维护堆顶元素

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 大根堆
        n = len(nums)
        # python默认是小根堆，故加"-"，形成"大根堆"
        # 由于堆顶元素可能不在滑动窗口内，故要维护一个二元组(num, index)
        # 通过index判断堆顶元素是否在滑动窗口内
        # 首先把 k 个元素加入大根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            # 把最新的元素加入大根堆
            heapq.heappush(q, (-nums[i], i))
            # 判断堆顶元素（下标）是否在滑动窗口内
            while q[0][1] <= i - k:
                heapq.heappop(q)
            # 把大根堆的堆顶元素加入ans
            ans.append(-q[0][0])
        return ans




图的实现和特性
图的属性和分类：有点有边
基于图的相关算法

图的属性
Graph（V, E）
V-vertex：点
1 度-入度和出度
2 点与点之间：连通与否
E-edge：边
1 有向和无向（单行线）
2 权重（边长）

图的表示和分类
表示：邻阶矩阵 、邻阶表（二维）（无向无权图、有向无权图、无向有权图、有向有权图）

基于图常见算法
DFS BFS
visited（） = set（）

泛型递归、树的递归

递归三要素：
1 抵制人肉递归
2 找最近重复性
3 数学归纳法思维
括号生成



第三周


分治、回溯
最近重复性
最优重复性
实战题目：Pow（x，n）、子集
1 terminator 递归终止条件
2 process（split your big problem）
3 drill down（调用函数去做子问题），merge（subresult）
4 reverse states



pow（x，n）
#分治O（logn）
1 terminator 递归终止条件
2 process（split your big problem）
3 drill down（调用函数去做子问题），merge（subresult）
4 reverse states

pow(x, n):
  subproblem:subresult = pow(x, n/2)
 merge:
   if n % 2 == 1:
      result = subresult * subresult * x
   else：
     result = subresult * subresult



class Solution:
    def myPow(self, x: float, n: int) -> float:
        #分治，其实也属于递归
        def quicklypow(x, n):  #定义分治后的函数
            #终止条件
            if n == 0:return 1
            if n == 1:return x
            #定义分治后的乘积
            y = quicklypow(x, n//2)
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x
        
        if n < 0:
            return 1/self.myPow(x, -n)
        return quicklypow(x, n)



贪心算法

在当下选择最好，最优
简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。



二分查找

前提：

1 目标函数单调性（单调递增或者递减）
2 存在上下界（bounded）
3 能够通过索引访问（index accessible）

代码模板

    left, right = 0, len(arr) - 1
    while left <= right:
      mid = (left + right) / 2
      if arr[mid] == target:
          #find the target!!
          break or return result 
      elif arr[mid] < target:
          left = mid + 1
      else:
          right = mid - 1 




第五周


字典序和并查集

字典树（Trie）

本节内容：

1 字典树的数据结构
2 字典树的核心思想
3 字典树的基本性质

基本结构：

字典树，即Trie树，又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。

它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。

基本性质：

1 结点本身不存完整单词；
2 从根节点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串；
3 每个结点的所有子节点路径代表的字符都不相同。

结点存储额外信息 (eg：单词统计频次)    结点的内部实现

核心思想

1 Trie树的核心思想是空间换时间
2 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的

实现一个trie

dict{}实现


并查集（Disjoint Set）

适用场景：

组团、配对问题
Group or not？

基本操作：

makeSet（s）：建立一个新的并查集，其中包含s个单元素集合。

unionSet（x，y）：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并。

find（x）：找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

朋友圈问题


高级树、AVL树和红黑树

AVL树

1 Balance Factor（平衡因子）
   是它的左子树的高度减去它的右子树的高度（有时相反）。
   balance factor={-1,0,1}

2 通过旋转操作来进行平衡（四种）

左旋、右旋、左右旋、右左旋

平衡因子定的由来：因为平衡树查询的时间复杂度是等于树的深度的，所以记录深度差，得到平衡因子，平衡因子不平衡，就进行旋转操作

子树形态：左左树：右旋
                 右右树：左旋
                 左右树：左右旋
                 右左树：右左旋

AVL总结

1 平衡二叉搜索树

2 每个结点存 balance factor = {-1， 0 ， 1}

3 四种旋转操作

不足：结点需要存储额外信息、且调整次数频繁

近似平衡二叉树

红黑树

红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树：

每个结点要么是红色，要么是黑色

根结点是黑色

每个叶结点（NIL结点，空结点）是黑色的

不能有相邻接的两个红色结点

从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点


'/tmp/UvZsMxzWF34z2SAt[0].png!thumbnail'


关键性质：高度差小于两倍——从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

• AVL trees provide faster lookups than Red Black Trees because they are more strictly
balanced.（读和查找——AVL更优）

• Red Black Trees provide faster insertion and removal operations than AVL trees as
fewer rotations are done due to relatively relaxed balancing.（插入和删除——红黑树更优）

• AVL trees store balance factors or heights with each node, thus requires storage for
an integer per node whereas Red Black Tree requires only 1 bit of information per
node.（AVL更多的内存（int存放高度），红黑树，一个bit，额外内容消耗少）

• Red Black Trees are used in most of the language libraries like map,multimap,multisetin C++whereas AVL trees are used in databases（数据库） where faster retrievals are required.（读操作多，AVl，插入多，红黑树，map，set（红黑树），DB，读多，看朋友圈，AVL）

'/tmp/GBWYav5jzmL6UEWe.png!thumbnail'















