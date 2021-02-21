// 그리디
#include <iostream>
using namespace std;

int main() {
    //Fast IO
    ios::sync_with_stdio(false);
    cin.tie(nullptr), cout.tie(nullptr);

    int G, P, gi;              // 게이트 수 (1 ≤ G ≤ 10^5), 비행기 수 (1 ≤ P ≤ 10^5), 게이트 번호 (1 ≤ gi ≤ G)
    int gate[100001] = {0,};   // 게이트 배열
    int result = 0;

    cin >> G >> P;
    bool flag = false;
    for (int p = 1; p <= P; ++p) {
        cin >> gi;
        if (flag) break;

        // 1. 최대 번호의 게이트에 도킹하고 카운트 1 증가
        // 2. 도킹이 불가하면 한 칸씩 앞으로 옮기면서 자리가 있는지 확인하고, 자리가 있으면 카운트 1 증가
        // 3. 자리가 없다면 반복문 종료
        if (gate[gi] == 0) {
            gate[gi] = p;
            result++;
        } else {
            bool flag2 = true;
            for (int i = gi; i >= 1; --i) {
                if (gate[i] == 0) {
                    gate[i] = p;
                    result++;
                    flag2 = false;
                    break;
                }
            }
            if (flag2) flag = true;
        }
    }

    cout << result << '\n';
    return 0;
}