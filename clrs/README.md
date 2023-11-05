20230331
任选以下的一个递归式，使用递归树得到其好的渐进上界，并使用代入法验证：

1. T(n)=T(n/2)+n^2.
2. # T(n)=4T(n/2+2)+n.
   注意打卡格式：
   请至少在打卡消息的附近至少发一条带今日日期的消息，形如："20230331"。此后请说明挑选的问题。如果无法字数达到 100，能够比较清晰地说明问题也可。

提示：今天北京时间下午一点要进行第一次查卡，请尚未打卡的朋友记得此前完成 前天或昨天 的打卡任务~

20230331 1
递推树第 k 层，n^2 _ (2)^-(k - 1)，求和得 T(n) <= n^2 + n^2 _ 1/4 + n^2 _ 1/16 + ... + n^2 _ 1/2^(k - 1) <= n^2 _ (1 + 1/4 + 1/16 + ... + 1/2^(k - 1)) <= n^2 _ 2 <= 2n^2
假设 T(n) <= cn^2，代入可得 T(n)=T(n/2) + n^2 <= c(n/2)^2 + n^2 = (c/4 + 1)n^2 <= cn^2
取 c >= 3/4,得证

20230402 1
T(n) = T(n - a) + T(a) + n
= T(n - 2a) + 2T(a) + (n + n - a)
... = T(n % a) + (n // a)T(a) + (n + n - a + n - 2a + ... + n - (n // a)a)
T(n % a)为常数量级
(n // a)T(a)~O(n)
(n + n - a + n - 2a + ... + n - (n // a)a)=((n + n - (n // a)a)) _ (n // a)/2 ~ 1/2a _ n^2 ~ O(n^2)
渐进为 1/2a \* n^2

20230404 1
T(n)=4T(n/2)+n^2 lg n
套用主定理可得，a=4, b=2, f(n)= n^2 lgn
故 n^(logba) = n^2
f(n)不是多项式意义的渐进大于 n^2, 不存在\varepsilon > 0 使得 f(n)=Ω(n^logba + \varepsilon)
故不能使用主方法
T(n)=4T(n/2)+n^2 lgn
=4(4T(n/4) + 1/4 n^2lgn/2) = 4^2T(n/4) + n^2(lgn - 1)
= ... = 4^kT(1) + n^2\sum*0^k(lgn - k) = n^2 + n^2 *(lgn \_ lgn - (1 + k) \* k / 2)
= n^2(1 + 1/2 lgn^2 - 1/2 lgn) = O(n^2lgn^2)

其中 n/2^k = 1 => k = lgn

20230406

1. T(n)=√nT(√n)+n
   =√n(√nT(n^1/4)+n^1/2) + n
   = ... =
   =n^-2kT(n^-2k) + nk
   其中 n^-2k=1 => k = lglgn
   =>T(n) <= nlglgn

2. T(n)=T(n/2)+T(n/4)+T(n/8)+n
   猜测 T(n) = O(n)
   即 T(n) <= cn
   =7/8cn + n <= cn
   当 c >= 8 时成立
   现有


20230408 2

def random_half():
   while True:
      a, b = RANDOM(), RANDOM()
      if a > b:
         return 1
      elif a < b:
         return 0
每一轮返回结果的概率为2p(1-p)
则期望运行时间为t=\sum_j^\infty{j * (1 - 2p(1-p))^j * 2p(1-p)}
令y=2p(1-p)
t = y[1 * (1 - y) ^ 1 + 2 * (1 - y)^2 + ... + n * (1 - y)^n]
= y(1 - y)[1 * (1 - y) ^ 0 + 2 * (1 - y)^1 + ... + n * (1 - y)^n-1]
注意到右式是-1/(1 - (1 - y))泰勒展开的导数
= y(1 - y)(-y^-1)'=y(1-y)y^-2=(1-y)/y=(1-2p(1-p))/(2p(1-p))

20230410 2
记E(x)为最后连续掷出x次6，还需次数的期望
则E(0) = 1 + 5/6E(0) + 1/6E(1) => E(0) = E(1) + 6 = 5/6E(0) + 1 + 6
E(1) = 1 + 5/6E(0) + 5/6E(2) 
E(2) = 0
=> E(0) = 42

20230414 1
每次INCREMENT成功的概率为1/(n_{k+1} - n_k),成功后增加n_{k+1} - n_k
则增加期望为1，根据期望累加性可得N次INCREMENT的期望为N

20230416 1
最多节点为2^(h+1) - 1
最少节点最后一层仅有一个节点 2^(h) - 1 + 1 = 2^h
2^(h) <= n <= 2^(h + 1) - 1 < 2^(h + 1) => h = logn向下取整

20230418 1
FIFO可由栈表示，即只需要用优先队列构建栈。
维护一个自增变量k，将(k, 元素) append到优先队列(小顶堆)。因为k为自增，push->O(1)
如果使用大顶堆pop，调整堆复杂度O(lgn)不满足要求。
记录堆队尾子节点指针，pop时修剪，O(1)

20230420 2
```python
def sortArray(nums: List[int]) -> List[int]:
    def paration(left, right):
        privot = random.randint(left, right)
        nums[right], nums[privot] = nums[privot], nums[right]
        jj = left - 1
        for ii in range(left, right):
            if nums[ii] < nums[right]:
                jj += 1
                nums[ii], nums[jj] = nums[jj], nums[ii]
        jj += 1
        nums[jj], nums[right] = nums[right], nums[jj]
        return jj

    def quicksort(left, right):
        if left >= right:
            return
        mid = paration(left, right)
        quicksort(left, mid - 1)
        quicksort(mid + 1, right)

    quicksort(0, len(nums) - 1)
    return nums
```

20230422 1
privot 为随机选取的数，故α的渐进为[0, 0.5]的均匀分布，E(α)=L/2=0.25
如果元素均相等则random选取privot对paration没有优化，最坏时间复杂度为Θ(n^2)
可考虑当遇到元素相等时，以一定概率分至左侧或者右侧

20230426 1
最小深度的最大值和最大深度的最小值均是在比较排序决策树平衡时取到，分别为均为⌈log2(n!)⌉，当排序算法能够最大程度地减少比较次数时，需要进行的最少的比较次数，例如归并排序或堆排序，而叶子节点数为n!<= 2^x => 树的高度最小为⌈log2(n!)⌉

20230428 1
桶排序需要数据基本满足均匀的分布，是因为它的时间复杂度和空间复杂度都和桶的数量和大小有关。如果数据分布很不均匀，那么可能有些桶非常空，有些桶非常满，这样会导致桶排序的效率降低.
根据数据的先验分布，选择合适的桶的数量和大小；优化桶内排序算法至O(nlgn)，比如快排,归并等。

20230430 2
对字符串数组先建前缀树，再依次先序遍历前缀树，得到排序后的字符串序列。其时间复杂度为O(n),n为所有字符串的字符个数和。

20230502 1
(1) 假设存在 i=0,...,n-1-k，使得 nums[i] > nums[i+K]，则考虑 K 元子数组 nums[i:i+K] 和 nums[i+1:i+K+1]，它们的均值分别为
avg1 = (nums[i] + ... + nums[i+K-1]) / K
avg2 = (nums[i+1] + ... + nums[i+K]) / K
由于 nums[i] > nums[i+K]，我们有
avg1 - avg2 = (nums[i] - nums[i+K]) / K > 0
与 nums 是 K-sorted 的定义矛盾。所以不存在这样的 i，即对于 i=0,...,n-1-k，都有 nums[i] <= nums[i+K]，证毕。

(2) 将数组 nums 按照 index % k 分成 n/k 个长度为 k 的子序列，然后对每个子序列进行排序。整体O(nlog(n/k))

20230504 1
```python
def get_max_min_value():
   n = input()
   if n % 2 == 0:
      print("?", 0, 1)
      u, v = [0, 1] if (input() == '<') else [1, 0]
   else:
      u, v = 0, 0
   s = 2 if n % 2 == 0 else 1
   for ii in range(s, n, 2):
      print("?", ii, ii + 1)
      x, y = [ii, ii + 1] if (input() == '<') else [ii + 1, ii]
      print("?", u, x)
      if input() == '>':
         u = x
      print("?", v, y)
      if input() == '<':
         v = y
   print(u, v)

```

20230506 1
```python

def partition(nums, pivot_index = 0):
    i = 0
    if pivot_index !=0:
      nums[0], nums[pivot_index] = nums[pivot_index], nums[0]
    for j in range(len(nums)-1):
        if nums[j+1] < nums[0]:
            nums[j+1], nums[i+1] = nums[i+1], nums[j+1]
            i += 1
    nums[0], nums[i] = nums[i], nums[0]
    return nums, i

def randomized_select(nums, k):
   nums, now = partition(x, random.randrange(len(nums)))
   if now == k:
      return nums[k]
   if now > k:
      return randomized_select(nums[:now], k)
   return randomized_select(nums[now:], k - now)


def RANDOMIZED_SELECT(A, p, r, i):
    while p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        k = q - p + 1
        if i == k: return A[q]
        if i < k:
            r = q - 1
        else:
            p = q + 1
            i -= k
    return A[p]
```

20230508 1
利用最坏复杂度为O(n)的快速选择算法选择privot 使得privot划分数组尽量均匀，从而避免快排的最坏情况。

20230510 1
利用median of medians快速选择带权中位数，k比较S1时替换为比较S1的权值和。
依次迭代，直到S1的权值和与1/2相等。
由于median of medians的最坏复杂度为O(n), 使得上述select过程的最坏复杂度为O(n)

20230512 
a
如果选择的privot 不在min(zi, zj, zk)与max(zi, zj, zk)之间时，需要再次采样。
若zk <= zi < zj, 则期望为2/(j-k+1); 若zi <= zk < zj, 则期望为2/(j-i+1); 若zi < zj <= zk, 则期望为2/(k-i+1);

这个概率问题类似拒绝采样模型，当选择的 pivot 的位置不在 min(i, j, k) 和 max(i, j, k) 之间时，那就还要继续「采样」。真诚产生效果分化的情况，是 pivot 选在了 min(i, j, k) 和 max(i, j, k) 之间，此时如果选中 i 或者 j（zi 与 zj 发生比较），那么指示器为 1，否则指示器为 0 （永远不会比较 zi 和 zj）。
所以  E[X_ijk] = 2 / (max(i, j, k) - min(i, j, k) + 1)
b.
应用 a 的结论，将 k 分别放在 k < i; i < k < j; j < k 三部分，分别求和就容易得出结论。



20230514
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 使用一个单链表模拟一个栈
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data

    def __len__(self):
        return self.size

# 使用一个单链表模拟一个队列
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        # 入队
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        # 出队
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data

    def __len__(self):
        return self.size
```


20230516 1

对象的多数组表示：将对象的每个属性或方法存储在一个不同的数组中，并用一个索引数组来记录每个对象在各个数组中的位置。
对象的单数组表示：将对象的所有属性或方法存储在一个连续的数组中，然后用一个偏移量来记录每个对象的起始位置

两种方法都是利用数组表示链表和对象结构。
多数组可以方便的增删对象的属性，不需要移动其他对象数据。可快速实现继承和多态。但是其需要维护多个数组和一个索引数组，有可能导致内存碎片。
单数组表示可以简化管理，只需要维护一个数组，此外查询效率高，只需要一次访问数组即可。但难以增删对象的属性。


20230518 
记录上一个遍历节点prev和当前遍历节点now
若prev为now的父节点，则向下遍历(若左子非空则左子，若左子空，右子非空，则右子，反之回到父节点)
若prev为now的左子节点且右子节点非空，则向右子节点遍历
否则，回到父节点

20230520 1
假设所有的keys都是完全有序的 {k1, k2, ..., kn}
根据简单均匀散列假设，则碰撞概率为\sum_{j>i}P(h(ki) == h(kj)) = \sum_{j>i}1/m = (n - i)/m
则预期碰撞次数为\sum_i^n (n-i)/m = (n^2 - n)/2m

20230522 1
满足简单均匀散列假设、计算高效、对近似值的区分敏感


20230524 11.3-3
设x和y是两个由基数2^p的字符组成的字符串，且x可由y通过其自己的字符置换排列导出。则存在置换函数f，使得x[i]=y[f(i)]，对任意i=1,2,...,|x|，则有

h(x)=\sum_{i=1}^{|x|} x[i]2^{p(i-1)} mod (2^p-1)
   = \sum_{i=1}^{|x|} y[f(i)]2^{p(i-1)} mod (2^p-1)
   = \sum_{i=1}^{|x|} y[f(i)] mod (2^p-1) * (2^{p} mod 2^p - 1) ^ ((i-1))
   = \sum_{i=1}^{|x|} y[f(i)] mod (2^p-1)
   = \sum_{j=1}^{|y|} y[j]2^{p(f^{-1}(j)-1)} mod (2^p-1)
   = \sum_{j=1}^{|y|} y[j] mod (2^p-1)
故h(x) = h(y)
例如p=2, h(x) = (100101) mod 3 = 1
h(y) = (011001) mod 3 = 1
不适用于密码学中的消息验证等场景

20230601 1
假设节点 x 有两个孩子，则它的后继就是以 x.right 为根的 BST 的最小元素。 
如果后继节点有一个左子节点，那么它就不是BST的最小元素。 所以，它一定没有左子节点。 
同理，前驱必须是左子树的最大元素，所以不能有右子节点。

20230603 1
比较Tree-Insert 与 Tree-Search 其while循环部分相同，即while循环部分查找的节点数相同。
但Insert过程除了上述查找过程，还需要比较插入节点与父节点之间的大小，确定插入节点位于父节点的子树位置。
故其查询节点数为搜索查询节点数+1.

20230605 1
12.3右式等效于n+3个物体选4个组合数。
假设被选中的四个物体，最右侧物体的index为i+4, 则i的范围为[0, n-1].
则剩下三个物体的组合数为C_{i+3}^3.
由于最右侧物体index可以为[0, n-1]，故4个物体的组合数为\sum_0^{n-1}C_{i+3}^3=C_{n+3}^4.
得证

20230607 1
考虑n个节点的二叉树，补充n+1个叶子节点，使其成为满二叉树。
而满二叉树与之前的二叉树一一对应。
则问题转化为求节点数为2n+1的满二叉树的形态数。
除去根节点，先序遍历，满二叉树共有n个左节点记为0和n个右节点记为1.
且0的前缀个数比1多，则排序个数为卡特兰数Cn=1/(n+1)C_2n^n.

20230612 1
黑高k，最多内部节点为黑红交替(黑k，红k)，内部节点最多2^2k-1
外部节点为第2k层，节点数为2^2k

20230614 1
RIGHT-ROTATE(T, y)  
    x = y.left  
    y.left = x.right    
    if x.right ≠ NIL  
        x.right.parent = y  
    x.parent = y.parent  
    if y.parent == NIL  
        T.root = x  
    else if y == y.parent.right  
        y.parent.right = x  
    else  
        y.parent.left = x  
    x.right = y  
    y.parent = x  

20230618 2
若不能使用父节点，则可以利用map记录当前父子关系，将RB-INSERT和fixup中间使用父节点的逻辑改由从map中获得
RB-INSERT(T, z)
    let P be a new dictionary
    x = T.root
    y = T.nil
    P[x] = y
    while x != T.nil
        y = x
        if z.key < x.key
            x = x.left
        else x = x.right
        P[x] = y
    P[z] = y
    if y == T.nil
        T.root = z 
    else if z.key < y.key
        y.left = z
    else y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = RED
    RB-INSERT-FIXUP(T, z, P)    

20230621 2
1. 如果节点y在RB_DELETE 没有子节点，且x=T.nil,将会在line2 检查T.nil
2. 如果根节点被删除，x=T.nil,且root=x时，将会在line23修改x to black

20230623 2
记录每一个顶点的圆周角值，按顺时针排序，每条弦的两个顶点分别记为u,v, u < v
顺时针依次添加顶点，若为u则添加到sortedlist, 若为v则二分查找大于u的个数，并从sortedlist中删除u

20230625 1

···python
def rectangleArea(rectangles):
    def dfs():
        res, pre = 0, -1
        for ii, jj in ps:
            res += max(0, jj - max(pre, ii))
            pre = max(pre, jj)
        return res

    line = []
    for x1, y1, x2, y2 in rectangles:
        line.append((y1, 0, x1, x2))
        line.append((y2, 1, x1, x2))
    ps, ans, pre_y = SortedList(), 0, None
    for y, state, x1, x2 in sorted(line):
        if pre_y is not None:
            ans += dfs() * (y - pre_y)
        pre_y = y
        if state == 0:
            ps.add((x1, x2))
        else:
            ps.remove((x1, x2))
    return ans
```

20230627 1
利用动态规划
设 M[i, j] 表示计算从矩阵 i 到矩阵 j 的最小标量乘法次数，其中 1 <= i <= j <= n。
初始化对角线元素 M[i, i] = 0
使用自底向上的方法，计算 M[i, j] 的值。
对于每个子问题规模 l = 2, 3, ..., n：
对于每个可能的起始矩阵 i = 1, 2, ..., n-l+1：
1. 计算结束矩阵 j = i + l - 1。
2. 初始化 M[i, j] 为无穷大。
3. 遍历所有可能的分割点 k（i <= k < j），计算代价 c = M[i, k] + M[k+1, j] + p(i-1) * p(k) * p(j)（其中 p 表示矩阵的维度）。如果 c 小于当前的 M[i, j] 值，则更新 M[i, j] = c，并记录分割点 k。
故M[1, n] 存储了整个矩阵链的最优括号化方案的最小乘法次数。
其时间复杂度为O(n^3)

20230629 1

```python
def lcs(X, Y):  
    n, m = len(X), len(Y)  
    if n < m:  
        X, Y, n, m = Y, X, m, n
  
    dp = [0] * (m + 1)
    for i in range(1, n + 1):  
        prev = dp[0]  
        for j in range(1, m + 1):  
            temp = dp[j]  
            if X[i - 1] == Y[j - 1]:  
                dp[j] = prev + 1  
            else:  
                dp[j] = max(dp[j], dp[j - 1])  
            prev = temp  
    return dp[-1]  
```

20230703 1
dp[i][j] 为前i+1行写入j+1个单词的的额外空格^3和.
则dp[i][j] = min_{k=i}^{j-1}{dp[i-1][k-1] + cost(k, j)^3}
其中cost为第k到第j单词在一行内的额外空格数
时间复杂度O(n^2) 空间复杂度O(n^2)

20230705 15-6
dp[i][1/0]为以i为根节点的子树中选择/不选择i的最大社交值和
dp[i][0] = max_{k\in i.son}(dp[k][0], dp[k][1])
dp[i][1] = max_{k\in i.son}(dp[k][0])
自底向上遍历

20230707 2
相似：
两者都是求解优化问题的方法，可以在一定条件下得到问题的最优解，都需要满足最优子结构性质。

不同：
贪心需要每一步都满足局部最优，而dp则通过寻找子问题之间的关系，自底向上或自顶向下地构建最优解。
贪心不一定能找到全局最优解，而dp总是能找到全局最优解。
dp通常cache子问题结果，需要更高的时间和空间复杂度，而贪心不需要cache子问题结果，时间和空间复杂度较低。

20230710 1
对{x} 从小到大排序，依次选择第一个未被覆盖的点作为左端点，设立长度为1的区间。
只考虑当前未被覆盖的子问题，如果该点x2不是左端点，设其左端点为x1 < x2
而x2左侧已无其他点 \in {x} 则该区间所涵盖点数 < 已x2为左端点的线段。


20230712 2
用一棵二叉树来表示前缀码。树的叶子节点表示字符，非叶子节点表示码字的前缀。从根节点到叶子节点的路径表示码字，左分支表示0，右分支表示1。
定义先序遍历，则需要2n-1位表示二叉树。
除此之外，还需要传递叶子节点序列，共有n个叶子节点，可以用⌈log₂n⌉位来表示每个字符。总共有n个字符，所以需要n * ⌈log₂n⌉位来表示所有叶子节点的字符。
综上，需要2n-1 + n * ⌈log₂n⌉位来表示并传输最优前缀码。

20230714 a
按处理时间从小到大对任务进行排序，并按该顺序依次执行。
这个贪心是最优的，子结构：若在最优解中运行第一个任务，则以最小化平均完成时间的方式运行剩余任务即可获得最优解。
\sum_time = n p_1 + (n - 1) p_2 + ... + (1) p_n
若第一个执行的是p_i > p_1, 且除去p_i, p_1外的任务顺序不变，则 \sum_time_2 = n p_i + (n - 1) p_2 + ... + (1) p_n > \sum_time
故贪心是最优的。
时间复杂度O(nlogn)


20230717 1 
摊还分析评价的是一个操作序列中所执行的所有操作的平均时间，保证最坏情况下每个操作的平均性能。

20230719 2
记翻转一位的代价为1，对置位操作的摊还成本为2。
在二进制递增过程中，while循环中复位操作代价用该位存储的1美元支付，递增过程中最多发生一次置位。
对n次递增操作，其总摊还代价最多为O(n), 故其平均摊还成本为O(n)/n=O(1)

20230721 1
令φ‘(D_i) = φ(D_i) - φ(D_0)
则φ‘(D_0) = φ(D_0) - φ(D_0) = 0, φ‘(D_i) = φ(D_i) - φ(D_0) >= 0
则摊还成本，\hat{c_i}' = c_i + φ‘(D_i) - φ‘(D_{i-1}) = c_i + φ(D_i) - φ(D_{i-1}) - φ(D_0) + φ(D_0) = c_i + φ(D_i) - φ(D_{i-1}) = \hat{c_i}
故摊还成本不变

20230724 1
虽然动态表的插入和删除会引起动态表的扩张和收缩，但其动态表的摊还代价为O(1)。
动态表的空闲空间相交总空间的比例不会超过一个常数分数。
利用势能法分析插入删除的摊还成本，势函数={2T.num - T.size, if \alpha >=1/2; T.size/2 - T.num, if \alpha < 1/2}
空表的势为0，且势永远大于0，故势函数定义的操作序列总摊还成本是总实际代价的上界。
插入操作的摊还成本至多为3，删除操作的摊还成本至多为2，故其摊还代价为O(1)

20230726 
a 中序遍历得到排序后的数组，选择中位数为根依次递归遍历左右子数组。
b 最坏搜索复杂度为树高，而树高至少为logα(n).
如果每个节点的子节点大小都不超过α倍的父节点大小，那么这个子树的大小至少是α^0 + α^1 + … + α^(h-1) = (1 - α^h) / (1 - α)
故n ≥ (1 - α^h) / (1 - α)，从而得到h ≤ logα(n(1-α) + α)。
故其最坏搜索复杂度为O(logn)

20230728 2
节点关键字个数[1, 3]
(1)[2](3,4,5)
(1,2)[3](4,5)
(1,2,3)[4](5)
(1)[2,4](3)(5)

20230731 1
B树最小关键字，先序遍历，直到找到叶子节点。
给定关键字的前序节点，
若该节点x_i为不是叶子节点，则返回第i个子节点中最大的元素。
否则若i > 1, 则返回叶子节点中x_{i - 1}
否则返回小于value的父节点。

20230802 1
1. 若关键字所在的节点的左子树的根节点包含的关键字数量大于t-1（t为B树的最小度数），则可以用该子树中最大的关键字替换要删除的关键字，然后在左子树中递归删除替换过来的关键字。
2. 若关键字所在的节点的右子树的根节点包含的关键字数量大于t-1，则可以用该子树中最小的关键字替换要删除的关键字，然后在右子树中递归删除替换过来的关键字。
3. 若关键字所在的节点的左子树和右子树的根节点都只包含t-1个关键字，那么可以将要删除的关键字和右子树根节点的所有关键字合并到左子树根节点中，然后在合并后的左子树中递归删除关键字。

20230804 1
斐波那契堆是具有最小堆序的有根树集合。特点是结构相对松散，允许度数随着节点数的增加而变化。具有较低的平摊时间复杂度，例如插入、删除最小值和合并堆等操作。
节点的孩子链表是指在斐波那契堆中，每个节点的子节点所形成的环形双向链表。
孩子链表中出现的次数为节点的度，度的大小决定了斐波那契堆的性能。

20230807 1
斐波那契堆的合并是将两个堆的根链表链接成为H的新根链表。
其势函数Φ(H) = t(H) + 2m(H)
Φ(H) + Φ(H2) = t(H1) + t(H2) + 2m(H1) + 2m(H_2)
而t(H) = t(H_1) + t(H_2), m(H) = m(H_1) + m(H_2)
故Φ(H1) + Φ(H2) = Φ(H)
故其摊还代价等于实际代价，即O(1)

20230809 1
循环重复的将包含节点w的以x为根的树与和x度数相同的根相同的根相链接，
如果存在相同度数的子树，则合并，度数加1，
直到没有与x度数相同的根为止。

20230814 1
DECREASE-KEY的实际代价为O(c) (级联切断操作，c次调用CASCADING-CUT)
设H为初始的堆，则最终包含t(H) + c棵树，最多有m(H) - c + 2个标记的节点
因此，势最多变化为(t(H) + c + 2(m(H) - c + 2)) - (t(H) + 2m(H)) = 4 - c
因此，其摊还代价最多为O(c) + 4 - c = O(1)

20230816 1
斐波那契堆删除节点过程
1. 减小节点的关键字为负无穷，O(1)
2. 然后FIB-HEAP-EXTRACT-MIN将移除斐波那契堆，O(lgn)
总摊还时间为O(lgn)

20230818 1
19.3 归纳法，带入斐波那契数的递归式和假设，并结合黄金分割率的定义，得证
19.4 设s_k 为斐波那契堆中度数为k的任意节点的最小可能size。
则size(x) >= s_k >= 2 + \sum_{i=2}^ks_yi degree >= 2 + \sum_{i=2}^k s_{i-2}
>= 2 + \sum_{i=2}^k F_i = 1 + \sum_{i=0}^k F_i = F_{k+2} >= \phi^k 得证
19.5 根据引理19.4，得n>=size(x)>=\phi^k, 得 k<= lg_\phi n=>最大度数D(n)为O(lgn)


20230821 1
若 k == x.key 不操作, 若 k < x.key 则运行key减值操作，时间复杂度O(1)。 如果 k > x.key，则删除再插入新值，复杂度为O(lgn)。

20230823 1
叠加一颗度为\sqrt(n)的树，高度为2，每个节点存储的是其子树的逻辑或。
使用summary数组可以在O(\sqrt(n))的时间内实现minimum，maximum，successor，predecessor和delete操作。

20230825 1
每次递归以平方根大小缩减全域，直至项数大小为2。
考虑到目标时间复杂度为O(lglgu)。
而T(u) = T(\sqrt{u}) + O(1), 则递归到下一层次前，在每一层耗费常数时间。

20230828 1
1. 若 V.u == 2，则直接查找对应位是否为1。
2. 否则将查询值 x 分解为两部分：高位部分 x_high 和低位部分 x_low。其中 x_high = x // sqrt(u)，x_low = x % sqrt(u)。
递归查询 x_high 和 x_low。若summary 中不存在 x_high，则说明 x 也不在集合中。如果 summary 中存在 x_high，那么继续在 cluster[x_high] 中查找 x_low。如果 cluster[x_high] 中存在 x_low，则 x 存在于集合中；否则不存在。

20230830 1
if V.u == 2, 则将A数组A中x位设为1，
否则递归将x插入对应簇中。
最坏情况，做2次递归调用，则运行时间T(u) = 2T(\sqrt{n}) + O(1) => O(lgu)

20230901 1
在delete的else分支中检查n是否为1，若为1则将summary位设为0，将表中指针清空，并直接return。
否则和之前相同。最坏复杂度不改变，最好复杂度可节省至lglgn

20230904 1
最大最小值：查找min,max值，O(1)
元素是否在集合内，递归查找子树，若等于max/min 则存在集合内，否则递归直到根节点，则不存在，O(lglgn)

20230906 1
vEB树插入元素
若树为空，则新建根节点
若 x < V.min, 交换x与V.min
若V.u > 2 则先判断x簇是否为空，若为空将x的簇号插入summary中，否则将x插入簇中。
若x > V.max 则更新max值


20230908 1
添加一个记录关键词次数的属性，用来维护插入和删除

20230911 1
MAKE-SET(x): 新建一个新的集合，x不会出现在别的集合中
UNION(x, y): 并集，由于要求不相交，故需要删除原有的x y集合
FIND-SET(x): 返回指向集合x的指针

20230914 1
不相交集合森林是不相交集合的有根树表示，每个集合为一棵有根树。
查找路径是从一个节点到其所在集合根节点的路径。
启发式策略包括按秩合并和路径压缩两种方式。
按秩合并，在执行 UNION 操作时，将秩较小的树的根节点链接到秩较大的树的根节点。
路径压缩，执行 FIND-SET 操作时，将查找路径上的每个节点直接连接到根节点。
两趟方法，包括第一次遍历从给定元素沿着查找路径找到根节点。第二次遍历是将查找路径上的每个节点的父指针设置为根节点。

20230921 1
图的表示方法有：
1）邻接矩阵，N * M的矩阵表示是否存在边，适合稠密图
2）邻接表，记录连接的边对应的节点pair，适合稀疏图
3）十字链表，边记录相邻点，点记录相邻边，适用于点边稠密有向图

20230923 2
邻接矩阵表示的图，其BFS复杂度为O(V^2)
便利每个节点需要便利整列数据需要V，共V个节点，故复杂度为O(V^2)


20230926 2
树边和前向边有u.d<v.d, u.f>v.f
反向边 u.d>v.d, u.f<v.f
交叉边 u.d>v.d,u.f>v.f

20230929 2
if E >= V, 则图中存在环
else，dfs 遍历，若节点被遍历两次则存在环

20231002 1
STRONG-CONNECTED-COMPONENTS 缩点，若得到的图为链，则为半连通

20231004
22.3
a 必要性 如果图G中的每个顶点的入度等于出度，则图G存在欧拉回路。
从任意顶点出发，遍历图G，直到无法继续遍历，根据入度=出度，得当前节点一定为初始顶点，则得到一个欧拉回路。
如果图G存在欧拉回路，则图G中的每个顶点的入度等于出度。
充分性 且若图G中存在欧拉回路，则从任意顶点出发，沿回路遍历，每经过一顶点，则会在一条边的入度进去，出度离开，故整个回路中每个顶点的入度=出度。
b 任意选取顶点开始遍历，选择不重复的边遍历，直至回到起点。依次从未遍历过的顶点重复上述操作，直至所有边都被遍历过。

20231008 1
若边集合不为树，则存在环，而去除环中任意边均会使得总权值更小，故与原条件相悖。
则该边集合必定为树。
反例，当边权值存在负值时，且存在环，则选取全为负值的环组成的边集合，其权值和最小，但不为树。


20231010 1
假设T'不是G'的最小生成树，则一定存在另外一个T’‘，在包含V'所有节点的前提下，其权值和小于T'。
考虑边T\T'，有w(T\T' U T'') = w(T\T') + w(T'') < w(T\T') + w(T') = w(T)
这与T为最小生成树相悖，故T'为G'的最小生成树。

20231012
首先获得最小生成树祖先路径上的最大边权和严格次大边权，
遍历其他不在数中的边，用路径上最大边权或者严格次大替换掉原边，
即得到严格次小生成树。

20231014
1. 为最小生成树，保留任意一个e，意味着改边为最小的达成连通的边，故其为最小生成树。
2. 不为最小生成树，因为是random order必然会生成任意树

20231017 1
松弛操作是指通过中间顶点来更新两个顶点之间的路径长度。
最短路径的特点是通过一系列的松弛操作，可以找到图中所有顶点对之间的最短路径。
Dijkstra最多松弛|V|-1次，BF会松弛(|V|-1) * |E|次

20231019 1
```python
def RELAX(u, v, w):
    if d[u] + w < d[v]:
        d[v] = d[u] + w
        return True
    return False

for i in range(len(G.V) - 1):
    flag = True
    for u, v, w in G.E:
        if RELAX(u, v, w):
            flag = False
        if flag:
            break
for u, v, w in G.E:
    if d[v] > d[u] + w:
        print("存在负环")
        return False
return True
```

20231021 2
将以节点为顶点的路径数存储在节点中，记为.paths
拓扑排序更新每个节点的路径数，u.paths = u.paths + 1 + v.paths
输出最后节点的paths

20231024 1
假设有一个图含有节点{a,b,c,d,e}
其中(a,b),(b,c),(c,d),(a,e),(c,e)连通
故按照a,e,c,d,b的顺序遍历，即(c,d)之后松弛(b,c)
而到d的最短路为(a,b)(b,c)(c,d)先出现的路径反而后松弛，原假设不成立

20231026 1
利用自平衡二叉搜索树或者vEB替代优先队列，使得插入，删除，查找最小的复杂度为O(lgW)

20231028 1
[−5,−3,0,−1,−6,−8]

20231031 1
引入虚拟变量x, 令yi = xi + x, 则x_n 为差分约束当前仅当yn为差分约束。
对于x_i <= b_k 的每个约束，创建边(x, y_i), 权重为b_k;
对于x_i >= b_k 的每个约束，创建边(y_i, x), 权重为-b_k;
其余与之前一致

10231102
24.12
根据上界性质，若不存在路径，∞=d(s,v)<=v.d => v.d = ∞ = d(s, v)
24.13
若松弛前，v.d > u.d + w(u, v), 则松弛后 v.d = u.d + w(u, v)
若松弛前，v.d <= u.d + w(u, v), 则松弛后 v.d <= u.d + w(u, v)
综上，松弛后v.d <= u.d + w(u, v)
