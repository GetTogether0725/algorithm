# 第3周（6.6 — 6.12）

## 看板

|                          序号/题号                           |           题目            |   难度系数   | 阿宫 |        阿唐        |
| :----------------------------------------------------------: | :-----------------------: | :----------: | :--: | :----------------: |
| 1/[面试题 01.06. 字符串压缩](https://leetcode.cn/problems/compress-string-lcci/) | [字符串压缩](#字符串压缩) |    :star:    |      | :heavy_check_mark: |
| 2/[面试题 01.07. 旋转矩阵](https://leetcode.cn/problems/rotate-matrix-lcci/) |   [旋转矩阵](#旋转矩阵)   | :star::star: |      |                    |
| 3/[面试题 01.08. 零矩阵](https://leetcode.cn/problems/zero-matrix-lcci/) |     [零矩阵](#零矩阵)     | :star::star: |      |                    |
|                                                              |                           |              |      |                    |

## 题目

### [字符串压缩](https://leetcode.cn/problems/compress-string-lcci/)

#### 题目

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

**示例1:**

```
 输入："aabcccccaaa"
 输出："a2b1c5a3"
```

**示例2:**

```
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
```

提示：

- 字符串长度在[0, 50000]范围内。



#### 题解

##### 暴力解

```python
class Solution:
    def compressString(self, S: str) -> str:
        i = 0
        S_new = ""
        while i<len(S):
            time = 1
            j=i+1
            while j<len(S):
                if S[i]==S[j]:
                    time += 1
                    j+=1
                else:
                    j = len(S)+1
            S_new = S_new+S[i]+str(time)
            i = i+time
        if len(S_new)>=len(S):
            return S
        else:
            return S_new
```

不推荐使用字符串直接 res += s[i] 拼接，在 Python 中字符串是「不可变对象」，每次字符串拼接都会生成一个新字符串，效率低下。推荐使用列表，先将结果按照顺序添加，最终返回前拼接为字符串，因此只需要一次拼接操作。

```python
class Solution:
    def compressString(self, S: str) -> str:
        i = 0
        S_new = []
        while i<len(S):
            time = 1
            j=i+1
            S_new.append(S[i])
            while j<len(S):
                if S[i]==S[j]:
                    time += 1
                    j+=1
                else:
                    j = len(S)+1
            S_new.append(str(time))
            i = i+time
        S_ = "".join(S_new)
        if len(S_)>=len(S):
            return S
        else:
            return S_
```





### [旋转矩阵](https://leetcode.cn/problems/rotate-matrix-lcci/)

#### 题目

给你一幅由 `N × N` 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

示例 2:

```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

注意：本题与主站 48 题相同：https://leetcode-cn.com/problems/rotate-image/



#### 题解







### [零矩阵](https://leetcode.cn/problems/zero-matrix-lcci/)

#### 题目

编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

**示例 1：**

```
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

**示例 2：**

```
输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```



#### 题解





### 题目（链接）

#### 题目



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