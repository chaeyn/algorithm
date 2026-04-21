class Solution {
    public int solution(int[] num_list) {
        int multiple = 1;
        for (int i = 0; i < num_list.length; i++){
            multiple *= num_list[i];
        }

        int sum_square = 0;
        for (int i = 0; i < num_list.length; i++){
            sum_square += num_list[i];
        }
        sum_square = sum_square * sum_square;

        if (multiple < sum_square){
            return 1;
        } else {
            return 0;
        }
    }
}