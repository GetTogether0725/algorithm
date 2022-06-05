# 第2周（5.30 — 6.5）

## 看板

|                          序号/题号                           |         题目          |   难度系数   |        阿宫        | 阿唐 |
| :----------------------------------------------------------: | :-------------------: | :----------: | :----------------: | :--: |
| 1/[面试题 01.03. URL化](https://leetcode.cn/problems/string-to-url-lcci/) |    [URL化](#URL化)    |    :star:    | :heavy_check_mark: |      |
| 2/[面试题 01.04. 回文排列](https://leetcode.cn/problems/palindrome-permutation-lcci/) | [回文排列](#回文排列) |    :star:    | :heavy_check_mark: |      |
| 3/[面试题 01.05. 一次编辑](https://leetcode.cn/problems/one-away-lcci/) | [一次编辑](#一次编辑) | :star::star: |                    |      |
|                                                              |                       |              |                    |      |



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

##### 借助数组

数组的**索引为单字符的ASCII码值**，**值为出现的次数**，当**至少有两个字符**出现的次数为**奇数时**，说明当前字符串中不包含某个回文串的排列。

```cpp
class Solution {
public:
    bool canPermutePalindrome(string s) {
        int map[256] = {0};
        for(int i=0; i<s.size(); ++i) {
            map[ s[i] ] += 1; 
        }

        int count=0;
        for(int i=0; i<sizeof(map)/sizeof(map[0]); ++i) {
            if(map[i]) {
                if(map[i] % 2 == 1) {
                    count++;
                }
            }
        }
        return (count < 2) ? true : false;
    }
};
```

更优的一个解法

借助 bitset，使空间占用最小，默认b被初始化为`0000000...`，`b.flip(pos)`将第`pos`位翻转，然后至少当2个字符有奇数个时，说明当前字符串中不包含某个回文串的排列。

```cpp
class Solution {
public:
    bool canPermutePalindrome(string &s) {
        bitset<128> b;
        for(auto &c : s) 
            b.flip(c);
        return b.count() < 2;
    }
};
```





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

```cpp
class Solution {
public:
    bool oneEditAway(string first, string second) {
        int len = first.size() - second.size(); // 计算两字符串的差值
        bool once = true;                       // 仅支持一次修改
        if(len > 1 || len < -1)                 // 这两种情况均不符合要求
            return false;
        for(int i=0,j=0; i < first.size() && j < second.size();i++,j++) {
            if(first.at(i) != second.at(j)) {   // 如果二者字符不匹配，说明要添加/删除字符
                if(once) {                      // 如果未修改，则可修改；如果修改了，直接返回不满足条件。
                    if(len == 1) {              // second 要不要添加一个字符
                        --j;
                    } else if (len == -1) {     // second 要不要删除一个字符
                        --i;
                    }
                    once =! once;
                }
                else {
                    return once;
                }
            }
        }
        return true;
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