package DFS_BFS;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int [][] check;//연결
    static boolean[] visit;//방문확인
    static int n;//정점
    static int m;//간선
    static int s;//시작 정점
    //dfs=> 깊이 먼저
    public static void dfs(int start){
        visit[start]=true;
        System.out.print(start+" ");

        for(int i=0; i<n+1;i++){
//            System.out.println(check[start][i]+"<-----------check[start][i]");
            if(check[start][i]==1 && visit[i]==false) dfs(i);
        }
    }
    //bfs=> 넓이 먼저
    public static void bfs(){
        //Queue=> 먼저 들어가면 먼저 나옴
        //LinkedList=> 하나씩 찾아가는 방식
        Queue<Integer> queue=new LinkedList<Integer>();
        //시작점에 Queue삽입
        queue.add(s);
        visit[s]=true;
        System.out.print(s+" ");
        //queue가 빌때까지 반복+방문 확인
        while (!queue.isEmpty()){
            int temp =queue.poll();//임시로 queue맨앞갚 가져옴

            for (int j=1; j<=n;j++){
//                System.out.println(check[temp][j]+"<--------check[temp][j]");
                if(check[temp][j]==1 && visit[j]==false){
                    queue.add(j);
                    visit[j]=true;
                    System.out.print(j+" ");
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        s=sc.nextInt();
        check=new int[1001][1001];
        visit=new boolean[1001];
        //간선 연결 저장
        for(int i=0; i<m; i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            check[x][y]=check[y][x]=1;
        }
        // 호출 하고 초기화 후 호출 줄바꿈
        dfs(s);
        visit=new boolean[1001];
        System.out.println();
        bfs();
    }
}
