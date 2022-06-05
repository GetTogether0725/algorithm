# 第2周（5.30 — 6.5）

## 看板

|                          序号/题号                           |         题目          |   难度系数   | 阿宫 | 阿唐 |
| :----------------------------------------------------------: | :-------------------: | :----------: | :--: | :--: |
| 1/[面试题 01.03. URL化](https://leetcode.cn/problems/string-to-url-lcci/) |    [URL化](#URL化)    |    :star:    |      |      |
| 2/[面试题 01.04. 回文排列](https://leetcode.cn/problems/palindrome-permutation-lcci/) | [回文排列](#回文排列) |    :star:    |      |      |
| 3/[面试题 01.05. 一次编辑](https://leetcode.cn/problems/one-away-lcci/) | [一次编辑](#一次编辑) | :star::star: |      |      |
|                                                              |                       |              |      |      |



## 题目

### [URL化](https://leetcode.cn/problems/string-to-url-lcci/)

#### 题目

URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）



**示例 1：**

```
输入："Mr John Smith    ", 13
输出："Mr%20John%20Smith"
```

**示例 2：**

```
输入："               ", 5
输出："%20%20%20%20%20"
```


提示：

- 字符串长度在 [0, 500000] 范围内

#### 题解

##### 逆序暴力解

借助**栈**特性，**先入后出**

逆序遍历一次数组，若当前为空格（ascii码为0x20）则将%20存储到stack中，注意为逆序；不为空格，则正常存到stack中。

最后在遍历一遍stack，将其存到字符串中。。

```cpp
class Solution {
public:
    string replaceSpaces(string S, int length) {
        std::stack<char> s;
        string tmp("%20");
        for (int i=length-1; i>=0; --i) {
            if(S[i] == 0x20) {
                for(int j=0; j<tmp.size(); ++j) 
                    s.push(tmp[3-j-1]);  
            } else {
                s.push(S[i]);
            }
        }
        int ssize = s.size();
        string res(ssize,0);
        for(int i=0; i<ssize; ++i) {
            res[i] = s.top();
            s.pop();
        }
        return res;
    }
};
```







### 回文排列

#### 题目

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

**示例1：**

```
输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
```

#### 题解





### 一次编辑

#### 题目

字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

*示例1*

```
输入: 
first = "pale"
second = "ple"
输出: True
```

*示例2*

```
输入: 
first = "pales"
second = "pal"
输出: False
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