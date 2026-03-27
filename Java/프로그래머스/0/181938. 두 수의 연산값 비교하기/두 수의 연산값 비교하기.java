class Solution {
    public int solution(int a, int b) {
        String stringA = String.valueOf(a);
        String stringB = String.valueOf(b);

        int sum1 = Integer.parseInt(stringA + stringB);
        int sum2 = 2 * a * b;

        return sum1 > sum2 ? sum1 : sum2;
    }
}