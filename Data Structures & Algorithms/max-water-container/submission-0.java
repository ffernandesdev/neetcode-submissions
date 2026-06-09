class Solution {
    // brute force
    // T = O(n^2)
    // AUX = O(1)
    public int maxArea(int[] heights) {
        int biggerContainerArea = 0;

        for (int i = 0; i < heights.length - 1; i++) {
            for (int j = i + 1; j < heights.length; j++) {
                int containerHeight = heights[i] < heights[j] ? heights[i] : heights[j];
                int containerLength = j - i;
                int area = containerHeight * containerLength;
                if (area > biggerContainerArea) {
                    biggerContainerArea = area;
                }
            }
        }

        return biggerContainerArea;
    }
}
