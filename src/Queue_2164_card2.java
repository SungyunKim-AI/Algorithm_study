import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/* ==== Queue 사용법 정리 ====
         [예외 발생]               [값 리턴]
    추가 : q.add()        or      q.offer()
    삭제 : q.remove()     or      q.poll()
    검사 : q.element()    or      q.peek()
*/

public class Queue_2164_card2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            q.offer(i);
        }

        while (q.size() > 1) {
            q.poll();
            q.offer(q.poll());
        }

        System.out.println(q.poll());
    }
}
