class Solution {
    public int[] anagramMappings(int[] nums1, int[] nums2) {
        Map<Integer, Integer> valueToPos = new HashMap<>();
        int n = nums1.length;
        int[] res = new int[n];

        for (int i = 0; i < n; i++) {
            valueToPos.put(nums2[i], i);
        }

        for (int i = 0; i < n; i++) {
            res[i] = valueToPos.get(nums1[i]);
        }

        return res;
    }
}
