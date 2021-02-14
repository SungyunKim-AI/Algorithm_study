// 그래프 이론, 그래프 탐색, 이분 탐색, 너비 우선 탐색, 깊이 우선 탐색, 두 포인터
#include <iostream>
#include <algorithm>
using namespace std;

// 우체국은 'P', 집은 'K', 목초지는 '.'
// 수평, 수직, 대각선으로 인접한 칸으로 이동 가능
// 마지막 편지 배달 후 다시 우체국으로
// 피로도 : 가장 높은 곳과 낮은 곳의 고도 차이
int N;                    // 2 <= N <= 50
char map[50][50];
int height[50][50];       //고도는 1,000,000보다 작거나 같은 자연수
int direction[][2] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
int fatigue;

void delivery(int row, int col, int high, int low) {
    high = max(high, height[row][col]);
    low = min(low, height[row][col]);
    fatigue = high - low;

    for (int i = 0; i < 8; i++) {
        int nextRow = row + direction[i][1];
        int nextCol = col + direction[i][0];


    }
}

int main() {
    int startingPoint[2] = {-1, -1};  //우체국 시작점
    cin >> N;
    cin.ignore();                      //cin 에 들어가는 개행문자 무시
    for (int i = 0; i < N; i++) {
        cin.getline(map[i], N + 1);

        if (startingPoint[1] != -1) continue;
        for (int j = 0; j < N; j++) {
            if (map[i][j] == 'P') {
                startingPoint[0] = i;
                startingPoint[1] = j;
            }
        }
    }

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> height[i][j];

    delivery(startingPoint[0], startingPoint[1], 0, 1000001);
    cout << fatigue << endl;

    return 0;
}