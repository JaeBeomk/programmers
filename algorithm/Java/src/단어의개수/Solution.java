package 단어의개수;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
//          단어가 몇개인지 구하는 프로그램
        Scanner sc=new Scanner(System.in);
        String insert=sc.nextLine().trim();
        if (insert.isEmpty()) {
            System.out.println(0);
        }else {
            System.out.println(insert.split(" ").length);
        }
    }
}
