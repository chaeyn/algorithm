class Solution {
    public String solution(String code) {
        int mode = 0;
        String ret = "";

        for (int i = 0; i <= code.length() - 1; i++) {
            char c = code.charAt(i);
            if (mode == 0) {
                if (c == '1') {
                    mode = 1;
                } else {
                    if (i % 2 == 0) {
                        ret += c;
                    }
                }
            } else if (mode == 1) {
                if (c == '1') {
                    mode = 0;
                } else {
                    if (i % 2 != 0) {
                        ret += c;
                    }
                }
            }
        }
        
        if (ret.equals("")) {
            return "EMPTY";
        }
        
        return ret;
    }
}