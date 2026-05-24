class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Set<Integer> uniqueValues = new HashSet();

        for (int num : nums) {
            uniqueValues.add(num);
        }

        int longestSequence = 1;
        int currentSequence = 1;

        for (int num : nums) {
            if (!uniqueValues.contains(num-1)) {
                int next = num+1;
                while (uniqueValues.contains(next)) {
                    next++;
                    currentSequence++;
                }
                if (currentSequence > longestSequence) longestSequence = currentSequence;
                currentSequence = 1;
            }
        }

        return longestSequence;
    }
}
