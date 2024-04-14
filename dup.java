class SY {
    public static void main(String args[]) {
        int num = isValid();
        System.out.println(num);
    }

    public static int isValid() {
        String s1 = "2023BCT507";
        String sit = "BIT";
        String scs = "BCS";
        String str = s1.substring(4, 7); // Extract the substring "BIT"

        // Check if the substring is "BIT"
        if (str.equals(sit)) {
            return 2;
        } else if (str.equals(scs)) {
            return 1;
        } else {
            return -1;
        }
    }
}

