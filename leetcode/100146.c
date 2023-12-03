/*
 * @Author: gunjianpan
 * @Date:   2023-12-03 12:00:49
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2023-12-03 12:01:06
 */


// 100146. 统计感冒序列的数目 显示英文描述 
// 通过的用户数33
// 尝试过的用户数59
// 用户总通过次数33
// 用户总提交次数114
// 题目难度Hard
// 给你一个整数 n 和一个下标从 0 开始的整数数组 sick ，数组按 升序 排序。

// 有 n 位小朋友站成一排，按顺序编号为 0 到 n - 1 。数组 sick 包含一开始得了感冒的小朋友的位置。如果位置为 i 的小朋友得了感冒，他会传染给下标为 i - 1 或者 i + 1 的小朋友，前提 是被传染的小朋友存在且还没有得感冒。每一秒中， 至多一位 还没感冒的小朋友会被传染。

// 经过有限的秒数后，队列中所有小朋友都会感冒。感冒序列 指的是 所有 一开始没有感冒的小朋友最后得感冒的顺序序列。请你返回所有感冒序列的数目。

// 由于答案可能很大，请你将答案对 109 + 7 取余后返回。

// 注意，感冒序列 不 包含一开始就得了感冒的小朋友的下标。

 

// 示例 1：

// 输入：n = 5, sick = [0,4]
// 输出：4
// 解释：一开始，下标为 1 ，2 和 3 的小朋友没有感冒。总共有 4 个可能的感冒序列：
// - 一开始，下标为 1 和 3 的小朋友可以被传染，因为他们分别挨着有感冒的小朋友 0 和 4 ，令下标为 1 的小朋友先被传染。
// 然后，下标为 2 的小朋友挨着感冒的小朋友 1 ，下标为 3 的小朋友挨着感冒的小朋友 4 ，两位小朋友都可以被传染，令下标为 2 的小朋友被传染。
// 最后，下标为 3 的小朋友被传染，因为他挨着感冒的小朋友 2 和 4 ，感冒序列为 [1,2,3] 。
// - 一开始，下标为 1 和 3 的小朋友可以被传染，因为他们分别挨着感冒的小朋友 0 和 4 ，令下标为 1 的小朋友先被传染。
// 然后，下标为 2 的小朋友挨着感冒的小朋友 1 ，下标为 3 的小朋友挨着感冒的小朋友 4 ，两位小朋友都可以被传染，令下标为 3 的小朋友被传染。
// 最后，下标为 2 的小朋友被传染，因为他挨着感冒的小朋友 1 和 3 ，感冒序列为  [1,3,2] 。
// - 感冒序列 [3,1,2] ，被传染的顺序：[0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] 。
// - 感冒序列 [3,2,1] ，被传染的顺序：[0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] 。
// 示例 2：

// 输入：n = 4, sick = [1]
// 输出：3
// 解释：一开始，下标为 0 ，2 和 3 的小朋友没有感冒。总共有 3 个可能的感冒序列：
// - 感冒序列 [0,2,3] ，被传染的顺序：[0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3] 。
// - 感冒序列 [2,0,3] ，被传染的顺序：[0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3] 。
// - 感冒序列 [2,3,0] ，被传染的顺序：[0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3] 。
 

// 提示：

// 2 <= n <= 105
// 1 <= sick.length <= n - 1
// 0 <= sick[i] <= n - 1
// sick 按升序排列。

const int MODS = 1e9 + 7;

// Function to compute power modulo MODS
long long modPow(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        exp = exp >> 1;
        base = (base * base) % mod;
    }
    return result;
}

// Function to compute modular inverse
long long modInverse(long long n, long long mod) {
    return modPow(n, mod - 2, mod);
}

// Function to compute nCr modulo MODS
long long nCrMod(long long n, long long r, long long mod) {
    if (r == 0) return 1;

    long long numerator = 1;
    for (long long i = 0; i < r; i++) {
        numerator = (numerator * (n - i)) % mod;
    }

    long long denominator = 1;
    for (long long i = 1; i <= r; i++) {
        denominator = (denominator * i) % mod;
    }

    return (numerator * modInverse(denominator, mod)) % mod;
}


class Solution {
public:
    int numberOfSequence(int n, vector<int>& sick) {
        int m = n - sick.size();
        long long res = 1;
        sick.insert(sick.begin(), -1);
        sick.push_back(n);
        
        for (size_t idx = 0; idx < sick.size() - 1; idx++) {
            int ii = sick[idx], jj = sick[idx + 1];
            if (jj == ii + 1) continue;
            
            int k = jj - ii - 1;
            res = (res * nCrMod(m, k, MODS)) % MODS;
            m -= k;
            if (ii != -1 && jj != n) {
                res = (res * modPow(2, k - 1, MODS)) % MODS;
            }
        }
        return res;
        
    }
};