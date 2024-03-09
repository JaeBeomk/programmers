package 수묶기;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 1. 값 입력
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr= new int[n];
        int sum=0;
        int minus=0;

        // 2. 배열 정렬
        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();

            // 2-1. 음수 체크
            if(arr[i]<=0){
                minus++;
            }
        }
        Arrays.sort(arr);
        // 음수 두개면 묶어서 곱하기
        for (int i=1; i<minus; i+=2){
            sum+=(arr[i-1] * arr[i]);
        }
        // 음수 홀수면 더하기
        if(minus % 2 ==1) sum +=arr[minus-1];

        // 양수 홀수면 더하기
        if((n-minus)%2==1) sum +=arr[minus];

        // 양수 두개 곱하기
        for(int i=n-1; i>minus; i -=2){
            int plus=arr[i]+arr[i-1];
            int mul=arr[i]*arr[i-1];
            if (plus>mul){
                sum+=plus;
            }else {
                sum+=mul;
            }
        }
        System.out.println(sum);
    }
}
