# 第6周（6.27 — 7.3）

## 看板

|                          序号/题号                           |   题目   |   难度系数   | 阿宫 | 阿唐 |
| :----------------------------------------------------------: | :------: | :----------: | :--: | :--: |
| 1/[面试题 02.06. 回文链表](https://leetcode.cn/problems/palindrome-linked-list-lcci/) | 回文链表 |    :star:    |      |      |
| 2/[面试题 02.07. 链表相交](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/) | 链表相交 | :star::star: |      |      |
| 3/[面试题 02.08. 环路检测](https://leetcode.cn/problems/linked-list-cycle-lcci/) | 环路检测 | :star::star: |      |      |
|                                                              |          |              |      |      |

## 题目

### 回文链表

#### 题目

编写一个函数，检查输入的链表是否是回文的。

**示例1:**

```
输入： 1->2
输出： false 
```

**示例2:**

```
输入： 1->2->2->1
输出： true 
```

- **进阶：**
  你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？



#### 题解



### 链表相交

#### 题目

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

![image-20220701224451098](C:\Users\Tangshanjie\AppData\Roaming\Typora\typora-user-images\image-20220701224451098.png)

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

示例 1:

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

示例 2:

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

示例 3:

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

#### 题解





### 环路检测

#### 题目

给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际

**示例 1：**

![image-20220701224918781](C:\Users\Tangshanjie\AppData\Roaming\Typora\typora-user-images\image-20220701224918781.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

```
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

```
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```


进阶：

- 你是否可以不用额外空间解决此题？

#### 题解

#### 





# 内卷小天地

可按照每日记录的格式，记录下规定任务之外的完成的算法题目

## 阿宫：

### 题目（链接）

题目详述

示例

提示

#### 题解

## 阿唐：

### 题目（链接）

题目详述

示例

提示

#### 题解