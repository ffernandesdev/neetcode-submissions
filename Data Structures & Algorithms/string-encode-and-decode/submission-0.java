class Solution {
    // T: O(n) where n is the number of strings in the list of strings to encode
    // AUX: O(1)
    public String encode(List<String> strs) {
        String encodedList = "";

        for (String str : strs) {
            int stringLength = str.length();
            encodedList += stringLength + ";" + str;
        }
        return encodedList;
    }

    // T: O(n) where n is the number of characters in the encoded string
    // AUX: O(s) where s is the number of encoded strings
    public List<String> decode(String str) {
        List<String> decodedList = new ArrayList();

        int cursor = 0;
        while (cursor < str.length()) {
            int delimiterIndex = cursor;
            while (str.charAt(delimiterIndex) != ';') {
                delimiterIndex++;
            }
            int wordLength = Integer.parseInt(str.substring(cursor, delimiterIndex));
            int beginWord = delimiterIndex + 1;
            decodedList.add(str.substring(beginWord, beginWord + wordLength));
            cursor = beginWord + wordLength;
        }

        return decodedList;
    }
}
