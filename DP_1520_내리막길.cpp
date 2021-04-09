//DP, 그래프
#include <iostream>
using namespace std;

// 상, 하, 좌, 우 이동 배열
int direction[][2] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

int map[502][502] = {0, };    //각 지점의 높이는 10,000 이하의 자연수
int cache[502][502];
int M, N;                     // ( 1 <= M,N <= 500)

int movePointer(int row, int col);

int main() {
    int height;
    cin >> M >> N;
    for (int i = 1; i <= M; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> height;
            map[i][j] = height;
        }
    }

    fill(&cache[0][0], &cache[501][501], -1);

    int result = movePointer(1, 1);
    cout << result << endl;
    return 0;
}

int movePointer(int row, int col) {
    if (row > M || col > N || row < 1 || col < 1) return 0;
    if (row == M && col == N) {
        return 1;
    }

    int& ret = cache[row][col];
    if (ret != -1) return ret;
    ret = 0;
    //상, 하, 좌, 우 가능한 길 탐색
    for (int i = 0; i < 4; i++) {
        int nextRow = row + direction[i][1];
        int nextCol = col + direction[i][0];

        if (map[row][col] > map[nextRow][nextCol]) {
            ret += movePointer(nextRow, nextCol);
        }
    }
    return ret;
}