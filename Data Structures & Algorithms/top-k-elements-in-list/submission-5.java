// Problem one: count the frequency of each number
// Problem two: find the top K frequent numbers 
// How do I count the frequency? HashMap
// How do I find the top K? Iterate through the Map K times
// Expected time compl. N = length of nums[],,K = top freq, O(N^3)
// Can I do better?
// Yes, I can use a Min Heap (PriorityQueue in Java)
// Expected time compl improved to O(n log k)
// Can I do better?
// Yes, I can use a bucket sort

class Solution {
    // Overall T: O(n)
    // Overall AUX: O(n)
    public int[] topKFrequent(int[] nums, int k) {
        // O(n) where n is the number of numbers to count
        Map<Integer, Integer> count = new HashMap();
        // O(n) where n is the number of numbers to count
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        // O(n) where n is the number of numbers to count
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // O(n) where n is the number of numbers to count
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        // O(k) where k is the top frequent numbers to return
        int[] res = new int[k];
        int index = 0;

        // O(n)
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
