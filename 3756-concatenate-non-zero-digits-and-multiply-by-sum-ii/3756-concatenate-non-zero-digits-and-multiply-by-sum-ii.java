import java.util.*;

class Solution {
    static final int MOD = 1_000_000_007;

    public int[] sumAndMultiply(String s, int[][] queries) {
        int n = s.length();

        ArrayList<Integer> posList = new ArrayList<>();
        ArrayList<Integer> digitList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != '0') {
                posList.add(i);
                digitList.add(s.charAt(i) - '0');
            }
        }

        int m = digitList.size();

        long[] pow10 = new long[m + 1];
        pow10[0] = 1;
        for (int i = 1; i <= m; i++) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }

        long[] prefixNum = new long[m + 1];
        long[] prefixSum = new long[m + 1];

        for (int i = 0; i < m; i++) {
            prefixNum[i + 1] = (prefixNum[i] * 10 + digitList.get(i)) % MOD;
            prefixSum[i + 1] = prefixSum[i] + digitList.get(i);
        }

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int left = lowerBound(posList, l);
            int right = upperBound(posList, r) - 1;

            if (left > right) {
                ans[i] = 0;
                continue;
            }

            int len = right - left + 1;

            long num = (prefixNum[right + 1]
                    - (prefixNum[left] * pow10[len]) % MOD + MOD) % MOD;

            long sum = prefixSum[right + 1] - prefixSum[left];

            ans[i] = (int) ((num * sum) % MOD);
        }

        return ans;
    }

    private int lowerBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) < target) l = mid + 1;
            else r = mid;
        }
        return l;
    }

    private int upperBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) <= target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}