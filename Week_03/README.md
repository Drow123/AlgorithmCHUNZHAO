学习笔记

1. 深度优先搜索

示例代码：

二叉树


    def dfs(node):

        if node in visited:
            #already visited
            return 
     
        visited.add(node):
    
        #process current node
        #... #logic here
        dfs(node.left)
        dfs(node.right)

多叉树

    visited = set()

    def dfs(node, visited):

        visited.add(node)

        #process current node here.
        ... 
        for next_node in node.children():
            if not next_node in visited:
                dfs(next_node, visited)


DFS代码-递归写法


    visited = set()
    def dfs(node, visited):
        if node in visited: #terminator
        #already visited
            return 
     
        visited.add(node)

        #process current node here.
        ...
        for next_node in node.children():
            if not next_node in visited:
                dfs(next_node, visited)

DFS代码-非递归（手动维护一个栈）

    def DFS(self, tree):
        if tree.root is None:
            return []
        visited, stack = [], [tree.root]
    	while stack:
            node = stack.pop()
            visited.add(node)
        
            process(node)
            node = generate_related_nodes(node)
            stack.push(nodes)

2. 广度优先遍历（用队列）


    def bfs(graph, start, end):
        queue = []
        queue.append([start])
        visited.add(star)
   
        while queue:
            node = queue.popleft()
            visited.add(node)

            process(node)
            nodes = generate_related_nodes(node)
            queue.push(nodes)


3. 通用递归模板


    def recursion(level, param1, param2, ...)
        #recursion terminator
        if level > MAX_LEVEL:
            process_result
            return 

        #process logic in current level
        process(level, data...)
    
        #drill down 
        self.recursion(level + 1, p1, ...)
    
        #reverse the current level status if needed

4. 贪心算法

贪心算法Greedy

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。

5. 二分查找的实现、特性

二分查找的前提

1. 目标函数单调性（单调递增或者递减）

2. 存在上下界（bounded）

3. 能够通过索引访问（index accessible）

二分模板（python）

    left, right = 0, len(arry) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            #find the target!!
            break or return result
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1  







