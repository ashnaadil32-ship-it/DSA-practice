import java.util.List;
import java.util.ArrayList;

class SegmentTree {
    private int[] tree;
    private int n;

    public SegmentTree(List<Integer> data) {
        this.n = data.size();
        this.tree = new int[4 * Math.max(n,1)];
        if (n > 0) {
            build(data, 0, 0, n - 1);
        }
    }

    private void build(List<Integer> data, int node, int start, int end) {
        if (start == end) {
            tree[node] = data.get(start);
            return;
        }
        int mid = (start + end) / 2;
        build(data, 2 * node + 1, start, mid);
        build(data, 2 * node + 2, mid + 1, end);
        tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
    }

    public int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return 0;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int p1 = query(2 * node + 1, start, mid, l, r);
        int p2 = query(2 * node + 2, mid + 1, end, l, r);
        return Math.max(p1, p2);
    }
}

class Solution {
    class ZeroGroup {
        int start, length;
        ZeroGroup(int start, int length) {
            this.start = start;
            this.length = length;
        }
    }

    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        int n = s.length();
        int ones = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') ones++;
        }

        List<ZeroGroup> zeroGroups = new ArrayList<>();
        int[] zeroGroupIndex = new int[n];

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                if (i > 0 && s.charAt(i - 1) == '0') {
                    ZeroGroup last = zeroGroups.get(zeroGroups.size() - 1);
                    zeroGroups.set(zeroGroups.size() - 1, new ZeroGroup(last.start, last.length + 1));
                } else {
                    zeroGroups.add(new ZeroGroup(i, 1));
                }
            }
            zeroGroupIndex[i] = zeroGroups.size() - 1;
        }

        int m = zeroGroups.size();
        List<Integer> ans = new ArrayList<>();
        if (m == 0) {
            for (int q = 0; q < queries.length; q++) {
                ans.add(ones);
            }
            return ans;
        }

        List<Integer> mergeLengths = new ArrayList<>();
        for (int k = 0; k < m - 1; k++) {
            mergeLengths.add(zeroGroups.get(k).length + zeroGroups.get(k + 1).length);
        }
        SegmentTree st = new SegmentTree(mergeLengths);

        for (int[] q : queries) {
            int l = q[0], r = q[1];
            int g_l = zeroGroupIndex[l];
            int g_r = zeroGroupIndex[r];

            int leftLen = (g_l == -1) ? -1 : zeroGroups.get(g_l).length - (l - zeroGroups.get(g_l).start);
            int rightLen = (g_r == -1) ? -1 : (r - zeroGroups.get(g_r).start + 1);

            int activeSections = ones;

            int endGroupTarget = (s.charAt(r) == '1') ? g_r : g_r - 1;
            int startAdjIdx = g_l + 1;
            int endAdjIdx = endGroupTarget - 1;

            if (s.charAt(l) == '0' && s.charAt(r) == '0' && g_l + 1 == g_r) {
                activeSections = Math.max(activeSections, ones + leftLen + rightLen);
            } else if (startAdjIdx <= endAdjIdx) {
                int maxMerged = (mergeLengths.size() > 0) ? st.query(0, 0, mergeLengths.size() - 1, startAdjIdx, endAdjIdx) : 0;
                activeSections = Math.max(activeSections, ones + maxMerged);
            }

            if (s.charAt(l) == '0' && startAdjIdx <= endGroupTarget) {
                activeSections = Math.max(activeSections, ones + leftLen + zeroGroups.get(startAdjIdx).length);
            }
            if (s.charAt(r) == '0' && g_l < g_r - 1) {
                activeSections = Math.max(activeSections, ones + rightLen + zeroGroups.get(g_r - 1).length);
            }

            ans.add(activeSections);
        }

        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxActiveSectionsAfterTrade("10110111", new int[][]{{3,7},{4,6},{0,6}})); // expect [6,6,8]
        System.out.println(sol.maxActiveSectionsAfterTrade("01", new int[][]{{0,1}})); // expect [1]
        System.out.println(sol.maxActiveSectionsAfterTrade("0100", new int[][]{{0,3},{0,2},{1,3},{2,3}})); // expect [4,3,1,1]
        System.out.println(sol.maxActiveSectionsAfterTrade("1000100", new int[][]{{1,5},{0,6},{0,4}})); // expect [6,7,2]
        System.out.println(sol.maxActiveSectionsAfterTrade("01010", new int[][]{{0,3},{1,4},{1,3}})); // expect [4,4,2]
    }
}