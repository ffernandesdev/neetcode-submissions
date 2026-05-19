class Solution {
    // T: Overall O(n) | O(n) + O(n) where n is the number of elements in nums
    // AUX: O(n) where n is the number of elements in nums
    public int[] productExceptSelf(int[] nums) {
        int zeroCount = 0;
        int totalProduct = 1;

        // O(n) where n is the number of elements in nums
        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
                if (zeroCount > 1) {
                    return new int[nums.length];
                }
            } else {
                totalProduct *= num;
            }
        }

        // O(n) where n is the number of elements in nums
        int[] result = new int[nums.length];

        // O(n) where n is the number of elements in nums
        for (int i = 0; i < nums.length; i++) {
            if (zeroCount > 0) {
                if (nums[i] == 0) {
                    result[i] = totalProduct;
                }
            } else {
                result[i] = totalProduct / nums[i];
            }
        }

        return result;
    }
}  
