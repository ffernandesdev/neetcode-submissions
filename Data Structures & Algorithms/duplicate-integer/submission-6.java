class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> appearences = new HashSet();

        for (int num : nums) {
            if (appearences.contains(num)) {
                return true;
            }
            appearences.add(num);
        }

        return false;
    }
}