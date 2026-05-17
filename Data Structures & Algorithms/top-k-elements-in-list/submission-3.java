// Problem one: count the frequency of each number
// Problem two: find the top K frequent numbers 
// How do I count the frequency? HashMap
// How do I find the top K? Iterate through the Map K times
// Expected time compl. N = length of nums[],,K = top freq, O(N^3)
// Can I do better?
// Yes, I can use a Min Heap (PriorityQueue in Java)
// Expected time compl improved to O(n log k)

class Solution {
    // Overall T: O(n) + O(n log k) + O(k log k) = O(n log k) (since n log k dominates)
    // Overall AUX: O(n) + O(k) + O(k) = O(n) (since n dominates)
    public int[] topKFrequent(int[] nums, int k) {
        // AUX = O(n) where n is the size of the nums array
        Map<Integer, Integer> frequencyCount = new HashMap();

        // T = O(n) where n is the size of the nums array
        for (Integer num : nums) {
            frequencyCount.put(num, frequencyCount.getOrDefault(num, 0) + 1);
        }

        // AUX = O(k) where k is the desired number of top frequency to return
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // T = O(nlogk) where n where n is the size of the nums array
        for (Map.Entry<Integer, Integer> frequencyEntry : frequencyCount.entrySet()) {
            Integer num = frequencyEntry.getKey();
            Integer frequency = frequencyEntry.getValue();

            // T = O(logk) where k is the desired number of top frequency to return
            heap.offer(new int[]{frequency, num});
            if (heap.size() > k) {
                // T = O(logk) where k is the desired number of top frequency to return
                heap.poll();
            }
        }

        // AUX = O(k) where k is the desired number of top frequency to return
        int[] result = new int[k];

        // O(klogk) where k is the desired number of top frequency to return
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll()[1];
        }
        return result;
    }
}
