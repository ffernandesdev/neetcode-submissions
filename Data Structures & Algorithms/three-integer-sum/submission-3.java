class Solution {
    // T = O(n^2) where n is the number of elements in nums
    // AUX = O(log n), but O(1) if we disregard the space used to sort, since the other extra space used was to build the output
    public List<List<Integer>> threeSum(int[] nums) {
        // AUX = O(n) where n is the number of elements in nums
        List<List<Integer>> triplets = new ArrayList();
        Arrays.sort(nums); // T = (n log n), AUX = (log n), where n is the number of elements in nums

        // T = O(n^2)
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i-1] == nums[i]) continue;

            int l = i + 1, r = nums.length - 1;
            // T = O(n)
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    triplets.add(List.of(nums[i], nums[l], nums[r]));
                    l++;
                    while (nums[l] == nums[l-1] && l < r) {
                        l++;
                    }
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        return triplets;
    }
}
