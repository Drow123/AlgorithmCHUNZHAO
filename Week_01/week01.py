1.删除排序数组中的重复项

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        #循环结束条件，快指针大于nums的长度
        while fast < len(nums):
            if nums[fast] == nums[slow]:#如果两个数相等，则快指针加1，慢指针不动
                fast += 1
            else:#慢指针加1，将快指针的值赋给加1后的慢指针
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1  #最后返回新数组长度



2. 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #旋转算法，很巧妙
        #相当于将整个数组逆置，再将前k个逆置，后将后n-k个逆置
        #时间复杂度O(2n)=O(n),空间复杂度O(1)
        #k大于数组长度时，相当于转圈，只需k对数组长度取余即可
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        reverse(0, n - 1)  #旋转整个数组
        reverse(0, k - 1)  #旋转前k个
        reverse(k, n - 1)  #旋转后n-k个


3. 合并两个有序链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #可以用递归，也可以用迭代，迭代的空间复杂度为O(1)
        #递归条件是二个有序链表为空
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

4. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        #p2如果大于p1，就需要把p2前面的数放到nums1的前面
        nums1[: p2 + 1] = nums2[: p2 + 1]


5. 两数之和
#使用字典
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if target - nums[i] in d :
                return d[target - nums[i]] , i
            else:
                d[nums[i]] = i

6. 移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快慢指针,时间复杂度O(n),空间复杂度O(1)
        if not nums:
            return 
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


7. 加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #从后往前遍历digits，如果位上是9，则变为0
        #每次return的位置很重要，避免给每一位都加+1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
                    return digits


8. 有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1

        for k in dic.values():
            if k != 0:
                return False

        return True

