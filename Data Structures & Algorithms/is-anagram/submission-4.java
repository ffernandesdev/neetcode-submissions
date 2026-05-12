class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<String, Integer> mapS = new HashMap();
        HashMap<String, Integer> mapT = new HashMap();

        for (int i = 0; i < s.length(); i++) {
            String keyS = Character.toString(s.charAt(i));
            mapS.put(keyS, mapS.getOrDefault(keyS, 0) + 1);

            String keyT = Character.toString(t.charAt(i));
            mapT.put(keyT, mapT.getOrDefault(keyT, 0) + 1);
        }

        return mapS.equals(mapT);
    }
}
