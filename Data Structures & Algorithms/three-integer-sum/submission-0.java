class Solution {
    // T = O(n^2) where n is the number of elements in nums
    // AUX = O(log n)
    public List<List<Integer>> threeSum(int[] nums) {
        // AUX = O(n) where n is the number of elements in nums
        Set<List<Integer>> triplets = new HashSet();
        Arrays.sort(nums); // T = (n log n), AUX = (log n), where n is the number of elements in nums

        // T = O(n^2)
        for (int i = 0; i < nums.length; i++) {
            int l = i + 1, r = nums.length - 1;
            // T = O(n)
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    triplets.add(List.of(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        // Space complexity disregarded because it is used for the result
        List<List<Integer>> result = new ArrayList();

        // O(n)
        for (List<Integer> triplet : triplets) {
            result.add(triplet);
        }

        return result;
    }
}
