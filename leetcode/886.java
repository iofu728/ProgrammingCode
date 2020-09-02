/*
 * @Author: gunjianpan
 * @Date:   2020-09-02 12:44:41
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-02 12:44:42
 */

class Solution {
    ArrayList<Integer>[] edges;
    Map<Integer, Integer> color;

    public boolean possibleBipartition(int N, int[][] dislikes) {
        edges = new ArrayList[N + 1];
        for (int ii = 1; ii <= N; ++ii){
            edges[ii] = new ArrayList();
        }
        for (int[] edge: dislikes) {
            edges[edge[0]].add(edge[1]);
            edges[edge[1]].add(edge[0]);
        }
        color = new HashMap();
        for (int ii = 1; ii <= N; ++ii){
            if (!color.containsKey(ii) && !dfs(ii, 0)) {
                return false;
            }
        }
        return true;
    }

    public boolean dfs(int node, int c){
        if (color.containsKey(node)) {
            return color.get(node) == c;
        }
        color.put(node, c);
        for (int ii: edges[node]) {
            if (!dfs(ii, c ^ 1)){
                return false;
            }
        }
        return true;

    }
}
