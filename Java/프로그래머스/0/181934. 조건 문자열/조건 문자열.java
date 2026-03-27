import java.util.Objects;

class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if (Objects.equals(ineq, "<")) {
            if (Objects.equals(eq, "=")) {
                if (n <= m) return 1;
                else return 0;
            } else if (Objects.equals(eq, "!")) {
                if (n < m) return 1;
                else return 0;
            }
        } else if (Objects.equals(ineq, ">")) {
            if (Objects.equals(eq, "=")) {
                if (n >= m) return 1;
                else return 0;
            }  else if (Objects.equals(eq, "!")) {
                if (n > m) return 1;
                else return 0;
            }
        }
        return 0;
    }
}