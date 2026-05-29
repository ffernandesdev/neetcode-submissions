class Solution {
    // T = O(n) where n is the numbers of elements in the array numbers
    // AUX = O(1)
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;

        while (l < r) {
            int leftRightSum = numbers[l] + numbers[r];

            if (leftRightSum == target) {
                return new int[]{l+1, r+1};
            } else if (leftRightSum > target) {
                r--;
            } else { // leftRightSum < target
                l++;
            }
        }

        return new int[2];
    }
}
