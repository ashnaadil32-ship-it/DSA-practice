class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // g[i] will store the component ID for node i
        int[] g = new int[n];
        int cnt = 0;
        
        // Step 1: Assign nodes to connected components
        // Since nums is sorted, a 'break' in the path only occurs if 
        // the difference between consecutive elements is greater than maxDiff.
        for (int i = 1; i < n; ++i) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                cnt++; // Start a new component group
            }
            g[i] = cnt;
        }
        
        // Step 2: Answer each query in O(1) time
        int m = queries.length;
        boolean[] ans = new boolean[m];
        
        for (int i = 0; i < m; ++i) {
            int u = queries[i][0];
            int v = queries[i][1];
            
            // If they belong to the same component, a path exists
            ans[i] = (g[u] == g[v]);
        }
        
        return ans;
    }
}