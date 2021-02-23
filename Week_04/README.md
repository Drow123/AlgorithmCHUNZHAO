学习笔记

1.0 成就表
Array 数组                           Search 查询
Linked List 链表                   Recursion 递归
Stack 栈                               DFS 深度优先搜索
Queue 队列                          BFS 广度优先搜索
HashTable 哈希表                 Divide & Conquer 分治
Set 、Map                             Backtracking 回溯
Tree 二叉树                            Greedy 贪心
BST 二叉搜索树                        Binary Search 二叉查找
1.0.1 递归代码模板
#Python
def recursion(level, param1, param2, ...):
  #recursion terminator
  if level > MAX_LEVEL:
    process_result
    return

  #process logic in current level
  process（level，data...）

  #drill down
  self.recursion(level + 1, p1,...)

  #reverse the current level status if needed
1.0.2 分治代码模板
# Python
def divide_conquer(problem, param1, param2, ...):
# recursion terminator
if problem is None:
print_result
return

# prepare data
data = prepare_data(problem)
subproblems = split_problem(problem, data)

# conquer subproblems
subresult1 = self.divide_conquer(subproblems[0], p1, ...)
subresult2 = self.divide_conquer(subproblems[1], p1, ...)
subresult3 = self.divide_conquer(subproblems[2], p1, ...)
…

# process and generate the final result
result = process_result(subresult1, subresult2, subresult3, …)
# revert the current level states
1.1 动态规划关键点
感触
1 人肉递归低效、很累
2 找到最近最间方法，将其拆解成可重复解决的问题
3 数学归纳法思维（抵制人肉递归的诱惑）
本质——>寻找重复性
动态规划
关键点
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）
共性：找到重复的子问题
差异性：最优子结构、中途可以淘汰次优解
实战例题
重点：
递归       ——>    递归 + 记忆化搜索       ——>        递推/for循环（Bottom Up）
自顶向下                                                                    自底向上
复杂递归（面试题递归）：维度变化 +  取舍最优

路径计数
最优子结构 opt[n] = best_of(opt[n -1], opt[n - 2], ...)
储存中间状态：opt[i]
递推公式（状态转移方程或者DP方程）
FIb：opt[i] = opt[n -1] + opt[n - 2]
二维路径：opt[i,j] = opt[i +1][j] + opt[i][j+1](且判断a[i,j]是否空地）

