package ATM;


import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. 정보 입력
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        // 2. 배열 정렬
        Arrays.sort(arr);

        // 3. 이전 값과 합계 초기화
        int before =0;
        int sum = 0;

        // 4. 이전값에 현재값 더 하고 이전값은 증가
        for(int i = 0; i < n; i++){
            sum += arr[i]+before;
            before += arr[i];
        }

        System.out.println(sum);
    }
}

