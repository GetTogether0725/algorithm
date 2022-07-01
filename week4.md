# 第4周（6.13 — 6.19）

## 看板

|                          序号/题号                           |                   题目                   | 难度系数 |        阿宫        |        阿唐        |
| :----------------------------------------------------------: | :--------------------------------------: | :------: | :----------------: | :----------------: |
| 1/[面试题 01.09. 字符串轮转](https://leetcode.cn/problems/string-rotation-lcci/) |        [字符串轮转](#字符串轮转)         |  :star:  | :heavy_check_mark: | :heavy_check_mark: |
| 2/[面试题 02.01. 移除重复节点](https://leetcode.cn/problems/remove-duplicate-node-lcci/) |      [移除重复节点](#移除重复节点)       |  :star:  | :heavy_check_mark: | :heavy_check_mark: |
| 3/[面试题 02.02. 返回倒数第 k 个节点](https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/) | [返回倒数第20个节点](#返回倒数第k个节点) |  :star:  |                    | :heavy_check_mark: |
|                                                              |                                          |          |                    |                    |

## 题目

> 注意：本周题目中2、3涉及链表操作，先去了解链表的数据结构，在来做题



### [字符串轮转](https://leetcode.cn/problems/string-rotation-lcci/)

#### 题目

字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:

```
 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
```

示例2:

```
 输入：s1 = "aa", s2 = "aba"
 输出：False
```

提示：

- 字符串长度在[0, 100000]范围内。

说明:

- 你能只调用一次检查子串的方法吗？



#### 题解

##### 将某一字符串本身相连接

```python
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        S=s1+s1
        if (s2 in S) and len(s1)==len(s2):
            return True
        else:
            return False
```

##### 找到字符串的分割方式

```python
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        if s1 == s2:
            return True
        for i in range(len(s1)):
            if s1[0:i]==s2[-i:len(s2)]:
                S=s1[i:len(s1)]+s1[0:i]
                if S==s2:
                    return True
                else:
                    return False
        return False
```



##### 遍历遍历还是遍历

怎么感觉我写的这么复杂。。。

```cpp
class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        int s1sz = s1.size(); // s1长度
        int s2sz = s2.size(); // s2长度
        if(s1sz == s2sz) {    // 如果s1与s2长度相等，则进行判断，斗则false
            int j=0;
            if(s1sz == 0)     // 且都为0，返回true
                return true;
                                    // 否则，进行比较
            for(int i=0; i<s2sz * 2; ++i) {   // 循环次数2*s2sz
                if(s2[i%s2sz] == s1[j]) { 
                    while(s2[++i % s2sz] == s1[++j]);
                    if(j == s1sz)
                        return true;
                    else 
                        j = 0;
                }  
            }
        }
        return false;
    }
};
```





### [移除重复节点](https://leetcode.cn/problems/remove-duplicate-node-lcci/)

#### 题目

编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

```
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
```

示例2:

```
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
```

提示：

- 链表长度在[0, 20000]范围内。
- 链表元素在[0, 20000]范围内。
    进阶：

如果不得使用临时缓冲区，该怎么解决？



#### 题解

##### 使用`set`缓冲区

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
    ListNode* removeDuplicateNodes(ListNode* head) {
        if(!head) return head;  // 先判空
        unordered_set<int> set; // 缓冲区存val值
        ListNode* newList;      // 返回值指针
        newList = head;         // 将返回值指针指向head
        set.insert(head->val);  // 将head值添加到缓冲区
        while(head->next) {     // 当前head中的next是否为空，不为空，则判断下一个节点值是否在缓冲区中
            int &val = head->next->val;
            if(set.count(val)) {// 如果在，则将当前head中的next指针指向下一个节点的next值
                // 移除当前节点
                head->next = head->next->next;
            } else {            // 否则将当前head的val保存到缓冲区，链表后移
                set.insert(val);
                head = head->next;
            }
        } 
        return newList;        
    }
};
```

使用缓冲区，枚举前驱节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ret = head   #ret和head指向同一个链表的第一个节点
        vals = {head.val}
        while ret.next:
            if ret.next.val not in vals:
                vals.add(ret.next.val)
                ret = ret.next   #移动ret的指针不会改变head
            else:
                ret.next = ret.next.next    #改变ret.next会改变head
        return  head
```



### [返回倒数第k个节点](https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/)


#### 题目

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

```
输入： 1->2->3->4->5 和 k = 2
输出： 4
```

说明：

- 给定的 k 保证是有效的。

#### 题解

求解链表长度，并将元素按顺序保存为list

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        vals=[]
        lens=0
        while head:
            lens += 1
            vals.append(head.val)
            head = head.next
        return vals[lens-k]
```

求解长度，遍历两次链表

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        length = 0
        hea = head
        while hea:
            length+=1
            hea = hea.next
        i = length - k
        for li in range(0,i,1):
            head = head.next
        return head.val

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