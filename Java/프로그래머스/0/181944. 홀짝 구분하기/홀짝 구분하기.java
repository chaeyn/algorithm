import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String result = "";

        if (n % 2 == 0) result = n + " is even";
        else result = n + " is odd";

        System.out.println(result);
    }
}