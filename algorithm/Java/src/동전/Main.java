package 동전;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 1. 입력 처리
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        // 2. 동전의 가격 처리
        int [] price= new int[n];
        for (int i = 0; i< n; i++){
            price[i]=sc.nextInt();
        }
        // 3. count할 변수
        int coin=0;

        // 4. 최소=> for문 역으로
        for (int i = n-1; i >= 0; i--){
            if(price[i] <= k){
                coin += (k/price[i]);
                k = k % price[i];
            }
        }
        System.out.println(coin);
    }
}
