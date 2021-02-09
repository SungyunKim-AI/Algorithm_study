import java.util.*;

public class academic_member_3865 {

    static HashMap<String, ArrayList<String>> map = new HashMap<>();  // key : 학회 이름, value : 회원 이름
    static HashSet<String> visit = new HashSet<>();

    public static void main(String[] args) {
        ArrayList<Integer> results = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {     //여러 테스트 케이스가 가능 하도록 반복문 사용
            String input = scanner.nextLine();
            if (input.equals("0")) break;

            map.clear();
            visit.clear();
            int N = Integer.parseInt(input);     // 학회 수 N (N <= 100)
            String academy = "";
            for (int i = 0; i < N; i++) {
                input = scanner.nextLine();
                StringTokenizer temp = new StringTokenizer(input, ":|,|.");
                String key = temp.nextToken();
                if (i == 0) academy = key;

                ArrayList<String> members = new ArrayList<>();
                while (temp.hasMoreTokens()) {
                    members.add(temp.nextToken());
                }
                map.put(key, members);
            }
            visit.add(academy);
            results.add(recursive(academy, 0));
        }
        scanner.close();
        for (Integer result : results) {
            System.out.println(result);
        }
    }

    private static int recursive(String key, int count) {
        if (map.containsKey(key)) {
            for (String child : map.get(key)) {
                if (!visit.contains(child)) {
                    visit.add(child);
                    count += recursive(child, map.get(child) == null ? 1 : 0);
                }
            }
        }
        return count;
    }
}