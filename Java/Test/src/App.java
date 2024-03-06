public class App {
    public static void main(String[] arg) {
        Solution solution= new Solution();
        System.out.println(solution.solution(1234));
        
}
}
// 120906 자릿수 더하기
class Solution {
public int solution(int n) {
    int answer = 0;
    int length = (int)Math.log10(n)+1;
    if (n/10>10){
        for (int i=0;i<length;i++){
            answer+=n%10;
            n=n/10;
        }
    }
    return answer;
}
}