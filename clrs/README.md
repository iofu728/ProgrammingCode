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

