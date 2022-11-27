"""
6248. 统计中位数为 K 的子数组 显示英文描述 
通过的用户数3
尝试过的用户数3
用户总通过次数3
用户总提交次数4
题目难度Hard
给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。

注意：

数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。
 

示例 1：

输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
示例 2：

输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
nums 中的整数互不相同
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = [1 if ii > k else (0 if k == ii else -1) for ii in nums]
        s = 0
        idx = -1
        c = defaultdict(list)
        c[0].append(-1)
        b = defaultdict(list)
        d = defaultdict(list)
        res = 0
        b[0].append(-1)
        for ii, jj in enumerate(nums):
            if jj == 0:
                idx = ii
            s += jj
            
            if idx != -1:
                k = len(c[s])
                if ii % 2 == 0:
                    k2 = len(d[s - 1])
                else:
                    k2 = len(b[s - 1])
                res += k + k2
                # print(c[s], d[s - 1], b[s - 1], s, idx, k, k2, ii, jj)
            else:
                c[s].append(ii)
                if ii % 2 == 0:
                    d[s].append(ii)
                else:
                    b[s].append(ii)
            
            
        return res
