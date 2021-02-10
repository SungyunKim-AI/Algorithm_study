// 분할 정복
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long k;  // 1 <= k <= 10^18
    cin >> k;

    int square = log2(k);
    cout << square;


    return 0;
}

// 예제 입력1 : 1  -> 0
// 예제 입력2 : 2  -> 1
// 예제 입력3 : 10 -> 0

