# `PAT A by iofu728 `

This are some solutions for `PAT A ` by iofu728.

The idea of the problem is in my blog: [wyydsb.xin][1]
completion：109/151
-----
Recent article:

### ★★★★☆:
> 1.[PAT A 1026:Table Tennis (30).][9] 排队，模拟，sort

### ★★★★:
> 2.[PAT A 1068: Find More Coins (30)][20] 01背包
> 3.[PAT A 1033: To Fill or Not to Fill (25).][10] 贪心,模拟
> 4.[PAT A 1018：Public Bike Management (30).][2] Dijkstra + DFS
> 5.[排队模拟问题][3]
> 6.[PAT A 1014: Waiting in Line (30).][5] 排队，模拟，sort,queue

### ★★★☆:
> 7.[ANOJ  1024: C – 宇宙树(25)][22] DFS
> 8.[PAT A 1057: Stack (30)][17] 二分查找，二维哈希，栈模拟
> 9.[PAT A 1021: Deepest Root (25).][8] 无环判断,树的深度,最深源点

### ★★☆☆:
> 10.[PAT A 1087: All Roads Lead to Rome (30)][31] Dijkstra DFS

### ★★☆:
> 11.[PAT A 1082: Read Number in Chinese (25)][25] 字符串

### ☆☆★:
> 12.[PAT A 1107: Social Clusters (30)][32] 合并 并查集
> 13.[PAT A 1086: Tree Traversals Again (25)][30] 二叉树遍历
> 14.[PAT A 1080: Graduate Admission (30)][29] sort
> 15.[PAT A 1056: Mice and Rice (25)][16] 模拟，晋级赛
> 16.[PAT A 1049: Counting Ones (30)][15] 递归，数学问题

### ☆☆☆:
> 17.[ANOJ  1023: B – 缺失数(25)][23] bitMap
> 18.[PAT A 1079: Total Sales of Supply Chain (25)][28] BFS DFS
> 19.[PAT A 1076: Forwards on Weibo (25)][27] 图，BFS
> 20.[PAT A 1075: PAT Judge (25)][26] sort
> 21:[PAT A 1072: Gas Station (30)][21] Dijkstra
> 22.[PAT A 1066: Root of AVL Tree (25)][19] AVL,建树
> 23.[PAT A 1044: Shopping in Mars (25)][14] dp
> 24.[PAT A 1040: Longest Symmetric String (25)][13] 动态规划dp
> 25.[PAT A 1034: Head of a Gang (30)][11] DFS,map
> 26.[PAT A 1017: Queueing at Bank (25).][4] 排队，模拟
> 27.[PAT A 1022: Digital Library (30).][7] map,引用传参&

### ☆★:
> 28.[PAT A 1038: Recover the Smallest Number (30)][12]字符串

### ☆:
> 29.[ANOJ  1022: A – 库洛值(20)][24] hashMap
> 30.[PAT A 1063: Set Similarity (25)][18] set
> 31.[PAT A 1015: Reversible Primes (20).][6] 素数，进制转换
-----
`updated 10/7/2018`


[1]:http://wyydsb.xin/pat/            "乌云压顶是吧"
[2]: http://wyydsb.xin/pat/1018.html  "PAT A 1018: Public Bike Management (30)★★★★"
[3]: http://wyydsb.xin/pat/sort.html  "排队模拟问题分析"
[4]: http://wyydsb.xin/pat/1017.html  "PAT A 1017: Queueing at Bank (25)☆☆☆"
[5]: http://wyydsb.xin/pat/1014.html  "PAT A 1014: Waiting in Line (30)★★★★"
[6]: http://wyydsb.xin/pat/1015.html  "PAT A 1015:  Reversible Primes (20)☆"
[7]: http://wyydsb.xin/pat/1022.html  "PAT A 1022: Digital Library (30)☆☆☆"
[8]: http://wyydsb.xin/pat/1021.html  "PAT A 1021: Deepest Root (25)★★★☆"
[9]: http://wyydsb.xin/pat/1026.html  "PAT A 1026: Table Tennis (30)★★★★☆"
[10]:http://wyydsb.xin/pat/1033.html  "PAT A 1033: To Fill or Not to Fill (25)★★★★"
[11]:http://wyydsb.xin/pat/1034.html  "PAT A 1034: Head of a Gang (30) ☆☆☆"
[12]:http://wyydsb.xin/pat/1038.html  "PAT A 1038: Recover the Smallest Number (30)☆☆★"
[13]:http://wyydsb.xin/pat/1040.html  "PAT A 1040: Longest Symmetric String (25)☆☆☆"
[14]:http://wyydsb.xin/pat/1044.html  "PAT A 1044: Shopping in Mars (25)☆☆☆"
[15]:http://wyydsb.xin/pat/1049.html  "PAT A 1049: Counting Ones (30)☆☆★"
[16]:http://wyydsb.xin/pat/1056.html  "PAT A 1056: Mice and Rice (25)☆☆★"
[17]:http://wyydsb.xin/pat/1057.html  "PAT A 1057: Stack (30)★★★☆"
[18]:http://wyydsb.xin/pat/1063.html  "PAT A 1063: Set Similarity (25)☆"
[19]:http://wyydsb.xin/pat/1066.html  "PAT A 1066: Root of AVL Tree (25)☆☆☆"
[20]:http://wyydsb.xin/pat/1068.html  "PAT A 1068: Find More Coins (30)★★★★"
[21]:http://wyydsb.xin/pat/1072.html  "PAT A 1072: Gas Station (30)☆☆☆"
[22]:http://wyydsb.xin/pat/anoj2018II.html#_1024-c-–-宇宙树-★★★☆ "ANOJ 2018 模拟2 C 宇宙树"
[23]:http://wyydsb.xin/pat/anoj2018II.html#_1023-b-–-缺失数-☆☆☆  "ANOJ 2018 模拟2 B 缺失数"
[24]:http://wyydsb.xin/pat/anoj2018II.html#_1022-a-–-库洛值-☆    "ANOJ 2018 模拟2 A 库洛值"
[25]:http://wyydsb.xin/pat/1082.html  "PAT A 1082: Read Number in Chinese (25)★★☆"
[26]:http://wyydsb.xin/pat/1075.html  "PAT A 1075: PAT Judge (25)☆☆☆"
[27]:http://wyydsb.xin/pat/1076.html  "PAT A 1076: Forwards on Weibo 30 ☆☆☆"
[28]:http://wyydsb.xin/pat/1079.html  "PAT A 1079: Total Sales of Supply Chain 25 ☆☆☆"
[29]:http://wyydsb.xin/pat/1080.html  "PAT A 1080: Graduate Admission 30 ☆☆★"
[30]:http://wyydsb.xin/pat/1086.html  "PAT A 1086: Tree Traversals Again 25 ☆☆★"
[31]:http://wyydsb.xin/pat/1086.html  "PAT A 1087: All Roads Lead to Rome 30 ★★☆☆"
[32]:http://wyydsb.xin/pat/1107.html  "PAT A 1107: Social Clusters 30 ☆☆★"

