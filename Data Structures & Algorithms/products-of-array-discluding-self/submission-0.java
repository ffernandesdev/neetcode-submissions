class Solution {
    // T: O(n^2) where n is the number of elements in nums
    // AUX: O(n) where n is the number of elements in nums
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int product = 1;
            for (int j = 0; j < nums.length; j++) {
                if (j != i) {
                    product *= nums[j];
                }
            }
            result[i] = product;
        }

        return result;
    }
}  
