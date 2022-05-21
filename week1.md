# 第1周（5.23—5.29）

## 看板

|                          序号/题号                           |                     题目                      | 难度系数 |        阿宫        |        阿唐        |
| :----------------------------------------------------------: | :-------------------------------------------: | :------: | :----------------: | :----------------: |
|                             1/1                              |             [两数之和](#两数之和)             |  :star:  | :heavy_check_mark: | :heavy_check_mark: |
| 2/[面试题 01.01](https://leetcode.cn/problems/is-unique-lcci/) |     [判定字符是否唯一](#判定字符是否唯一)     |  :star:  | :heavy_check_mark: |                    |
| 3/[面试题 01.02](https://leetcode.cn/problems/check-permutation-lcci/) | [判定是否互为字符重排](#判定是否互为字符重排) |  :star:  |                    |                    |
|                                                              |                                               |          |                    |                    |
|                                                              |                                               |          |                    |                    |
|                                                              |                                               |          |                    |                    |
|                                                              |                                               |          |                    |                    |

## 题目

### [两数之和](https://leetcode.cn/problems/two-sum/)

#### 题目

给定一个整数数组 `nums` 和一个整数目标值 target，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```




提示：

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- 只会存在一个有效答案

**进阶**：你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？

#### 题解



##### 暴力解法

~~时间复杂度$$O(n^2)$$?~~，此处不对，应为xxxxx，空间复杂度$$O(1)$$

> 上面不对，应为xxxxx
>
> > 你说的不对，应该是xxxx
> >
> > > 你说我说的有不对。。。。。

分为两个循环，外循环遍历数组中的全部元素，

内循环遍历**除外循环遍历的当前元素之后的元素**，直至找到二者和满足要求的。

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0; i<nums.size(); ++i) {
            for(int j=i+1; j<nums.size(); ++j)
            if(target - nums[i] == nums[j]) {
                return vector<int> ({i,j});
            }
        }
        return vector<int>{};
    }
};
```





抄作业啦，暴力解法2

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums),1):
            v = target-nums[i]
            if v in nums:
                if i!=nums.index(v):
                    return[i,nums.index(v)]
```

##### 查表法（hash table）

**借助容器特性提高查找速度，降低整体时间复杂度。**

`unordered_map`是一个无序map，通过接口count接口查找时间复杂度为$$O(1)$$，外层一个循环$$O(n)$$

```cpp
/* 参考 https://en.cppreference.com/w/cpp/container/unordered_map */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> res(2,0);
        for(int i=0; i<nums.size(); ++i) {
            if(map.count(target - nums[i])) {
                res[0] = map.at(target - nums[i]);
                res[1] = i;
            }
            map.insert(pair<int, int>(nums[i], i));
        }
        return res;
    }
};
```



##### 另一种解法

先排序（快排可达$$O(nlog_2n)$$），然后。。。已经没上一种速度快了。





### [判定字符是否唯一](https://leetcode.cn/problems/is-unique-lcci/)

#### 题目

实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

```
输入: s = "leetcode"
输出: false 
```

示例 2：

```
输入: s = "abc"
输出: true
```

限制：

- 0 <= len(s) <= 100
- 如果你不使用额外的数据结构，会很加分。



#### 题解

借助数组，数组的**索引为单字符的ASCII码值**，**值为出现的次数**，当出现次数大于`1`时，即表示有重复数据。

时间复杂度$$O(n)$$，空间复杂度$$128$$?

```cpp
class Solution {
public:
    bool isUnique(string astr) {
        // 借助数组，数组的索引为单字符的ascii码，value为出现的次数
        int array[128] = {0};
        for(auto c : astr) {
            array[c] += 1;
        }
        for(int i=0; i<sizeof(array)/sizeof(array[0]); ++i) {
            if(array[i] >= 2) 
                return false;
        }
        return true;
    }
};
```



### [判定是否互为字符重排](https://leetcode.cn/problems/check-permutation-lcci/)

#### 题目

给定两个字符串 `s1` 和 `s2`，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

```
输入: s1 = "abc", s2 = "bca"
输出: true 
```

示例 2：

```
输入: s1 = "abc", s2 = "bad"
输出: false
```

说明：

- 0 <= len(s1) <= 100
- 0 <= len(s2) <= 100



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