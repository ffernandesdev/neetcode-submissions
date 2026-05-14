class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap();

        for (String str : strs) {
            String sortedString = sort(str);
            map.putIfAbsent(sortedString, new ArrayList());
            map.get(sortedString).add(str);
        }

        return new ArrayList(map.values());
    }

    private String sort(String str) {
        char[] chars = str.toCharArray();
        Arrays.sort(chars);

        return new String(chars);
    }
}
