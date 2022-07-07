# 第7周（7.4 — 7.10）

## 看板

|                          序号/题号                           | 难度系数 | 阿宫 | 阿唐 |
| :----------------------------------------------------------: | :------: | :--: | :--: |
| 1/[面试题 03.01. 三合一](https://leetcode.cn/problems/three-in-one-lcci/) |  :star:  |      |      |
| 2/[面试题 03.02. 栈的最小值](https://leetcode.cn/problems/min-stack-lcci/) |  :star:  |      |      |
|                                                              |          |      |      |
|                                                              |          |      |      |

## 题目

### [面试题 03.01. 三合一 ](https://leetcode.cn/problems/three-in-one-lcci/)

三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1

```
 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
```

示例2

```
 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]
```

#### 题解







### [栈的最小值](https://leetcode.cn/problems/min-stack-lcci/)

请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。

示例：

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```



#### 题解







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