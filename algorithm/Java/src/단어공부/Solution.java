package 단어공부;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);//입력
        String alpha=sc.next().toUpperCase();//단어 입력 하고 대문자로
        int[] az= new int[26];//배열로 선언
        for (int i=0; i<alpha.length();i++){
            int num=alpha.charAt(i)-'A';//배열의 위치 한글자씩
            az[num]++;
        }
        int max=0;
        char answer='?';
        for(int i=0;i<az.length;i++){
            if(max<az[i]){
                max=az[i];
                int iA = i + 'A';
                answer=(char) iA;
            }else if(max==az[i]){
                answer='?';
            }
        }
        System.out.println(answer);
    }

}
