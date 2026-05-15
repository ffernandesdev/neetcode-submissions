// Problem one: count the frequency of each number
// Problem two: find the top K frequent numbers 
// How do I count the frequency? HashMap
// How do I find the top K? Iterate through the Map K times
// Expected time compl. N = length of nums[],,K = top freq, O(N + K * N)
// Can I do better? 

class Solution {
    // TC O(N + K * N)
    // AC O(N + K) where N is nums.length, used to populate the map, 
    // and K is the number of most frequent elements to return, used to create an array of top K elements
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap();

        // O(N) where N == nums.length
        for (Integer num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<Integer> topFrequent = new ArrayList();

        // O(K * N) where N == nums.length and K = number of most frequent elements to return
        for (int i = 0; i < k; i++) {
            Integer topFreq = 0;
            Integer frequency = 0;
            for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
                Integer key = entry.getKey();
                Integer value = entry.getValue();
                if (value > frequency && !topFrequent.contains(key)) {
                    frequency = value;
                    topFreq = key;
                }
            }

            topFrequent.add(topFreq);
        }

        return topFrequent.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}
