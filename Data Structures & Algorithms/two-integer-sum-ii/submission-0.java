class Solution {
    // T = O(n^2)
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers.length; j++) {
                if (i != j && numbers[i] + numbers[j] == target) {
                    int smaller = i < j ? i : j;
                    int bigger = i > j ? i : j;
                    return new int[]{smaller + 1, bigger + 1};
                }
            }
        }

        return new int[2];
    }
}
