# 第1周（5.23—5.29）

## 看板

| 序号/题号 |         题目          | 难度系数 |        阿宫        |        阿唐        |
| :-------: | :-------------------: | :------: | :----------------: | :----------------: |
|    1/1    | [两数之和](#两数之和) |  :star:  | :heavy_check_mark: | :heavy_check_mark: |
|           |                       |  :star:  |        :x:         |                    |
|           |                       |          |                    |                    |
|           |                       |          |                    |                    |
|           |                       |          |                    |                    |
|           |                       |          |                    |                    |
|           |                       |          |                    |                    |

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

##### 另外一种解法





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