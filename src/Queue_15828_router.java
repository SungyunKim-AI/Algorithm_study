import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Queue_15828_router {
    public static void main(String[] args) throws IOException {

        // Input
        Scanner scanner = new Scanner(System.in);
        int buffer_size = scanner.nextInt();

        Queue<Integer> q = new LinkedList<>();
        int packet = 0;
        while (packet != -1) {
            packet = scanner.nextInt();
            if (packet == 0) {
                q.poll();
            } else {
                if (packet > 0 && q.size() < buffer_size) {
                    q.offer(packet);
                }
            }
        }

        //Output
        if (q.isEmpty()) {
            System.out.println("empty");
        } else {
            while (!q.isEmpty()) {
                System.out.print(q.poll() + " ");
            }
        }

    }
}
