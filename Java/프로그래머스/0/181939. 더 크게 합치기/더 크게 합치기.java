class Solution {
    public int solution(int a, int b) {
        String stringA = String.valueOf(a);
        String stringB = String.valueOf(b);

        int sum1 = Integer.parseInt(stringA + stringB);
        int sum2 = Integer.parseInt(stringB + stringA);

        return sum1 > sum2 ? sum1 : sum2;
    }
}