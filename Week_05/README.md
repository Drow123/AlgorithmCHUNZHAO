学习笔记

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

结点存储额外信息     结点的内部实现

核心思想
1 Trie树的核心思想是空间换时间
2 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
并查集（Disjoint Set）
适用场景：
组团、配对问题
Group or not？
基本操作：
makeSet（s）：建立一个新的并查集，其中包含s个单元素集合。
unionSet（x，y）：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并。
find（x）：找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。



高级树、AVL树和红黑树
AVL树
1 Balance Factor（平衡因子）
   是它的左子树的高度减去它的右子树的高度（有时相反）。
   balance factor={-1,0,1}
2 通过旋转操作来进行平衡（四种）
左旋、右旋、左右旋、右左旋
平衡因子定的由来：因为平衡树查询的时间复杂度是等于树的深度的，所以记录深度差，得到平衡因子，平衡因子不平衡，就进行旋转操作
左左树：右旋
右右树：左旋
左右树：左右旋
右左树：右左旋
AVL总结
1 平衡二叉搜索树
2 每个结点存 balance factor = {-1， 0 ， 1}
3 四种旋转操作
不足：结点需要额外额外信息、且调整次数频繁
近似平衡二叉树
红黑树
红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树：
每个结点要么是红色，要么是黑色
根结点是黑色
每个叶结点（NIL结点，空结点）是黑色的
不能有相邻接的两个红色结点
从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点
关键性质：高度差小于两倍
• AVL trees provide faster lookups than Red Black Trees because they are more strictly
balanced.
• Red Black Trees provide faster insertion and removal operations than AVL trees as
fewer rotations are done due to relatively relaxed balancing.
• AVL trees store balance factors or heights with each node, thus requires storage for
an integer per node whereas Red Black Tree requires only 1 bit of information per
node.
• Red Black Trees are used in most of the language libraries
like map,multimap,multisetin C++whereas AVL trees are used in databases（数据库） where faster retrievals are required.
位运算
XOR-异或
异或：相同为0，不同为1。也可用“不进位加法”来理解。
