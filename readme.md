# 阿唐&阿宫的奇妙算法屋

开始学习算法，阿唐&阿宫两个人分别使用不同的语言实现。

**争取每天完成一个小题目。**



题目一起维护，主要来自leetcode或者是xx网站上的题目。

题解：必须明晰

要求：代码必须编译通过



| 日期     | 题目     | 代码路径   | 完成情况 |
| -------- | -------- | ---------- | -------- |
| 22/05/18 | 两数之和 | 01_two-sum | :hammer: |
|          |          |            |          |
|          |          |            |          |
|          |          |            |          |



推荐题目：[程序员面试宝典](https://leetcode.cn/problem-list/xb9lfcwi/)

推荐题目：[剑指offer](https://leetcode.cn/problem-list/xb9nqhhg/)

推荐标题命名：**日期\_序号\_leetcode序号\_题目名称**，题目是个超链接，其指向题目的实际位置





## [220518_01_xx_两数之和](https://leetcode.cn/problems/two-sum/)

### 题目

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。

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

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



### 题解

#### 思路1

暴力解法，时间复杂度$$O(n^2)$$?，空间复杂度$$O(1)$$

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





### 冲突测试

冲突测试。


这样就可以了，但是呢，每次要写东西前，都必须执行

git pull，拉一下最新的代码，防止本地本地代码不是最新的。

欧克

修改完之后呢，通过`git add .`将数据添加到暂存区，然后`git commit -m "提交日志"`

接着`git push`就传到云端的小仓库了。



还有一情况，就是咱俩都在改东西，此时呢 云端仓库比咱俩的都要旧，也就是这个情况，咱俩的版本都要比云端新，但是呢，咱俩的版本又不同，这个情况下？要怎么办呢？ 

```
我	|- ver2
	 |
云端 ver1
     |
你	|- ver3
```

 此时，应分为两个情况

首先你先 git push，此时需要我去解决冲突，我先把你推的代码拉下来，拉的过程中会出现冲突，我得先把工作区清空，也就是`git stash`，之后合并云端的ver2到我的本地，也就是`git merge`，然后在 `git stash pop`去恢复我的工作区，此时在通过查看是否有问题，没问题直接就保存了，接着`git add .` ;`git commit -m ""`，接着`git push` 就结束了。

```
我	|- ver2
	 |	\
云端 ver1 ver2
     |		\
你	|- ver3-(ver2+ver3)
```

另外一种情况呢，正好相反。我就不写了，宝贝。就i是你先提交我去解决冲突，对的 咱俩同时修改一个文件的话，就得是这个样子的 宝，你看，我这边提交一下。

你先把这个复制一下。



## 参考

1. [如何系统的学习算法](https://www.zhihu.com/question/20588261)
