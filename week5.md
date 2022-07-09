# 第5周（6.20 — 6.26）

## 看板

|                          序号/题号                           |             题目              |   难度系数   |        阿宫        |        阿唐        |
| :----------------------------------------------------------: | :---------------------------: | :----------: | :----------------: | :----------------: |
| 1/[面试题 02.03. 删除中间节点](https://leetcode.cn/problems/delete-middle-node-lcci/) | [删除中间节点](#删除中间节点) |    :star:    | :heavy_check_mark: | :heavy_check_mark: |
| 2/[面试题 02.04. 分割链表](https://leetcode.cn/problems/partition-list-lcci/) |     [分割链表](#分割链表)     | :star::star: | :heavy_check_mark: | :heavy_check_mark: |
| 3/[面试题 02.05. 链表求和](https://leetcode.cn/problems/sum-lists-lcci/) |     [链表求和](#链表求和)     | :star::star: | :heavy_check_mark: | :heavy_check_mark: |
|                                                              |                               |              |                    |                    |

## 题目

### [删除中间节点](https://leetcode.cn/problems/delete-middle-node-lcci/)

#### 题目

若链表中的某个节点，既不是链表头节点，也不是链表尾节点，则称其为该链表的「中间节点」。

假定已知链表的某一个中间节点，请实现一种算法，将该节点从链表中删除。

例如，传入节点 c（位于单向链表 a->b->c->d->e->f 中），将其删除后，剩余链表为 a->b->d->e->f

**示例1:**

```
输入：节点 5 （位于单向链表 4->5->1->9 中）
输出：不返回任何数据，从链表中删除传入的节点 5，使链表变为 4->1->9
```

#### 题解

题目写得不清不楚的，理解：给定了一个链表，node指向了链表中的某一个中间节点，要做的久删除node指向的那个节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

确实写的迷迷糊糊

```cpp
class Solution {
public:
    // node 为要删除的节点。。
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```





### [分割链表](https://leetcode.cn/problems/partition-list-lcci/)

#### 题目

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你不需要 保留 每个分区中各节点的初始相对位置。

示例 1:

![](C:\Users\Tangshanjie\AppData\Roaming\Typora\typora-user-images\image-20220701223242156.png)

```
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

示例 2:

```
输入：head = [2,1], x = 2
输出：[1,2]
```

**提示：**

- 链表中节点的数目在范围 `[0, 200]` 内
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

#### 题解

双指针

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        min = head
        max = head
        while max:
            if max.val < x:
                min.val, max.val = max.val, min.val
                min = min.next
            max = max.next
        return head
```

还是快慢指针，快指针先走，慢指针只想小于x的区域，如果满足条件，则交换快慢指针域的值。

```cpp
class Solution {
public:
    void swap(int &a, int &b) {
        int c = a;
        a = b;
        b = c;
    }

    ListNode* partition(ListNode* head, int x) {
        // 快慢指针，快指针先走，慢指针指向小于x的区域
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast) {
            if(fast->val < x) { /* 如果小于x,交换快慢指针域的值 */
                swap(fast->val,slow->val);
                slow = slow->next;
            } 
            fast = fast->next;
        }

        return head;
    }
};
```



### [链表求和](https://leetcode.cn/problems/sum-lists-lcci/)

#### 题目

给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

**示例 1：**

```
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
```

**示例 2：**

```
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
```

**进阶：**思考一下，假设这些数位是正向存放的，又该如何解决呢?

#### 题解

转整数，再转回来

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        data_l1 = 0
        while l1:
            data_l1 += l1.val*(10**i)
            i += 1
            l1 = l1.next
        i = 0
        data_l2 = 0
        while l2:
            data_l2 += l2.val*(10**i)
            i += 1
            l2 = l2.next
        data_sum = data_l1+data_l2

        value=ListNode(data_sum%10)
        link3=value#输出的链表
        data_sum=data_sum//10
        while 1:
            if data_sum//10 == 0 and data_sum%10 == 0:
                print(data_sum)
                break
            link3.next=ListNode(data_sum%10)
            link3 = link3.next
            data_sum=data_sum//10
        return value

```

进位

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode((l1.val + l2.val)%10)
        l3 = sum
        up = (l1.val + l2.val)//10
        while l1.next and l2.next:
            l3.next = ListNode((l1.next.val + l2.next.val + up)%10)
            l3 = l3.next
            up = (l1.next.val + l2.next.val + up)//10
            l1 = l1.next
            l2 = l2.next
        while l1.next:
            l3.next = ListNode((l1.next.val + up)%10)
            l3 = l3.next
            up = (l1.next.val + up)//10
            l1 = l1.next
        while l2.next:
            l3.next = ListNode((l2.next.val + up)%10)
            l3 = l3.next
            up = (l2.next.val + up)//10
            l2 = l2.next
        if up != 0:
            l3.next = ListNode(up)
        return sum
```

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0); // 创建dummy节点
        ListNode* head = dummy;            // 创建指向dummy节点的指针，返回dummy节点的下一个
        int tmp=0;                         // 临时存储的结果

        while(l1 != nullptr || l2 != nullptr || tmp != 0) {
            if(l1 != nullptr) { // 如果l1不为空，则相加并下移 
                tmp += l1->val;
                l1 = l1->next;
            }
            if(l2 != nullptr) {// 如果l2不为空，则相加并下移 
                tmp += l2->val;
                l2 = l2->next;
            }
            // 创建新节点并加到head的下一个节点
            head->next = new ListNode(tmp%10);
            // 往后移
            head = head->next;
            // 取出高位
            tmp /= 10;
        }
        return dummy->next;
    }
};
```



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