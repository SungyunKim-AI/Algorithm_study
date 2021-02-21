// DP, 비트마스킹
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//전역 변수
int N, M;   //교실의 세로길이 N, 가로길이 M (1 ≤ M ≤ 10, 1 ≤ N ≤ 10)
int bitMask[10][1 << 10];
char classRoom[10][10];

void DFS(vector<string>& seats, int seat[10], int col);
int DP(vector<string>& seats, int beforeSeat, int row);


int main() {
    int C;      // 테스트케이스 개수
    cin >> C;
    while (C--) {
        // 각 테스트 케이스 시작하기 전 전역 변수 초기화
        fill(bitMask[0], bitMask[0] + (10*(1<<10)), -1);
        fill(classRoom[0], classRoom[0] + (10*10), 0);

        cin >> N >> M;
        for (int row = 0; row < N; ++row)
            for (int col = 0; col < M; ++col)
                cin >> classRoom[row][col];     // '.' (앉을 수 있는 자리), 'x'(못 앉는 자리)

        int seat[10];
        vector<string> seats;

        // 한 줄에 앉을 수 있는 자리배치의 모든 경우의 수를 벡터에 저장
        // 이 때는 앞, 뒷 줄 고려하지 않고, 부서진 책상도 고려하지 않는다.
        // 즉, 양옆에만 빈자리를 두고 모든 경우 수 계산!!
        DFS(seats, seat, 0);

        // 각 줄의 배치는 바로 앞 줄의 배치에만 영향을 받는다.
        // 즉, 왼쪽 대각선 위, 오른쪽 대각선 위에 학생이 없을 때만 현재 줄에 자리 배치가 가능!!
        // DFS 돌려서 나온 자리 배치에 따라 현재 줄에 학생을 앉히려고 할때, 문제 조건에 위배되지 않으면서 최대가 되는 학생의 수를 DP 배열에 저장
        int result = DP(seats, 0, 0);

        //정리 : DFS 에서 양옆 자리를 비워주고, DP 에서 대각선자리를 확인해 주면 싹다 확인 가능!!!
        cout << result << '\n';
    }
    return 0;
}


void DFS(vector<string>& seats, int seat[10], int col) {
    if (col == M) {
        string str;
        for (int i = 0; i < M; ++i)
            str += to_string(seat[i]);

        seats.push_back(str);
        return;
    }

    // (0 -> 빈자리, 1 -> 앉는 자리) 한번씩 재귀 호출
    seat[col] = 0;
    DFS(seats, seat, col + 1);

    //직전 자리가 1이면 그냥 리턴
    if ((0 < col) && (seat[col - 1] != 0)) { return; }
    seat[col] = 1;
    DFS(seats, seat, col + 1);
}


int DP(vector<string>& seats, int beforeSeat, int row) {
    if (row == N) return 0;
    if ( -1 < bitMask[row][beforeSeat])
        return bitMask[row][beforeSeat];

    int answer = 0;
    for (auto seat : seats) {
        int bits = 0;
        int count = 0;

        for (int col = 0; col < M; ++col) {
            // 부서진 책상이거나 빈자리이면, continue
            if (seat[col] == '0' || classRoom[row][col] == 'x') continue;
            // 왼쪽 대각선 위에 학생이 있다면, continue
            if ( (0 < col) && (beforeSeat & (1 << (col - 1))) ) continue;
            // 오른쪽 대각선 위에 학생이 있다면, continue
            if ((col < M) && (beforeSeat & (1 << (col + 1))) ) continue;

            count++;
            bits |= (1 << col);
        }
        answer = max(answer, DP(seats, bits, row + 1) + count);
    }
    bitMask[row][beforeSeat] = answer;
    return answer;
}