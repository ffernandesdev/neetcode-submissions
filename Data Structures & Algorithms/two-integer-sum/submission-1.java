class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> visitedValues = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            int targetY = target - nums[i];

            Integer visited = visitedValues.get(targetY);
            if (visited != null) {
                return new int[]{visited, i};
            }

            visitedValues.put(nums[i], i);
        }

        return new int[]{};
    }
}
