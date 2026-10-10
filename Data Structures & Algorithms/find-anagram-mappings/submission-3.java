class Solution {
    public int[] anagramMappings(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] res = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (nums1[i] == nums2[j]) {
                    res[i] = j;
                    break;
                }
            }
        }

        return res;
    }
}
