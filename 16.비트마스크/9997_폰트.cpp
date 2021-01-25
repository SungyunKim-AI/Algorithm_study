#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int N;                   //단어의 개수(1 <= N <= 25), 한 단어의 최대 길이는 100
int dict[25] = { 0, };   //단어를 저장할 사전 배열
int result = 0;          // 결과값 저장

void DFS(int idx, int sum) {

    if (idx > (N - 1)) { return; }
    if (sum == ((1 << 26) - 1)) { 
        result += pow(2, N - (idx + 1));
        return;
    }

    //포함 하는 경우
    DFS(idx + 1, sum | dict[idx + 1]);

    //포함 안하는 경우
    DFS(idx + 1, sum);
}


int main() {
    //input
    cin >> N;
    for (int i = 0; i < N; i++) {
        string word;
        cin >> word;
        for (int j = 0; j < word.length(); j++) {
            dict[i] |= (1 << (word[j] - 'a'));      //비트로 변환해서 저장
        }
    }

    //모든 부분 집합을 순회하는 반복문 풀이  -> 시간 초과
    //subset = 부분집합, universalSet = 전체 집합
    //(subset-1)을 하면 켜져 있던 최하위 비트가 꺼지고, 그 밑의 비트들은 전부 켜진다.
    //이때, 전체집합과의 교집합을 구하면 그 중에서 전체집합에 속하지 않은 비트들은 모두 꺼지게 된다.
    // int result = 0;
    // int universalSet = ((1 << N) - 1);
    // for (int subset = universalSet; subset; subset = ((subset-1) & universalSet)) {
    //     //부분집합의 각 원소들을 모두 합집합 연산한다.
    //     int flag = 0;
    //     for (int i = 0; i < N; i++) {
    //         if (subset & (1 << i)) {
    //             flag |= dict[i];    
    //         }
    //     }
    //     //합집합의 연산 결과가 (2^26 - 1)과 같으면 문장 조합에 성공.
    //     if (flag == ((1 << 26) - 1)) { result++; }
    // }

    //재귀함수를 이용한 풀이
    DFS(-1, 0);

    cout << result;
    return 0;
}
