public class Solution {

    private List<int[]> rects;
    private List<Integer> weights;
    private int total;
    private Random random;

    // Updated constructor to accept int[][] and convert it to List<int[]>
    public Solution(int[][] rectsArray) {
        this.rects = new ArrayList<>();
        this.weights = new ArrayList<>();
        this.random = new Random();
        this.total = 0;

        // Converting int[][] to List<int[]>
        for (int[] rect : rectsArray) {
            this.rects.add(rect);
            int weight = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            this.weights.add(weight);
            this.total += weight;
        }
        
        for (int i = 1; i < this.weights.size(); i++) {
            this.weights.set(i, this.weights.get(i) + this.weights.get(i - 1));
        }
        this.weights.add(0, 0);
    }

    public int[] pick() {
        int index = binarySearch(this.weights, random.nextInt(this.total) + 1);
        int[] rect = this.rects.get(index - 1);
        return new int[] {
            rect[0] + random.nextInt(rect[2] - rect[0] + 1),
            rect[1] + random.nextInt(rect[3] - rect[1] + 1)
        };
    }

    private int binarySearch(List<Integer> weights, int value) {
        int low = 0;
        int high = weights.size() - 1;

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (weights.get(mid) < value) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}