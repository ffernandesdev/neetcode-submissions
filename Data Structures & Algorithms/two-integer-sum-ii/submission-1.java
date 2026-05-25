class Solution {
    // T = O(n^2)
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> everyNumber = new HashMap();

        for (int i = 0; i < numbers.length; i++) {
            everyNumber.put(numbers[i], i);
        }

        for (int i = 0; i < numbers.length; i++) {
            int targetElement = target - numbers[i];
            if (everyNumber.containsKey(targetElement)) {
                int smaller = i < everyNumber.get(targetElement) ? i : everyNumber.get(targetElement);
                int bigger = i > everyNumber.get(targetElement) ? i : everyNumber.get(targetElement);
                return new int[]{smaller + 1, bigger + 1};
            }
        }

        return new int[2];
    }
}
