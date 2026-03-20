class Solution {
    public static String solution(String my_string, String overwrite_string, int s) {
        String answer = "";

        for (int i = 0; i < my_string.length(); i++) {
            if (i < s) {
                answer += my_string.charAt(i);
            } else if (i == s) {
                answer += overwrite_string;
                i += overwrite_string.length() - 1;
            } else if (i > s) {
                answer += my_string.charAt(i);
            }
        }
        return answer;
    }
}