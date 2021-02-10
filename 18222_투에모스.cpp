// 분할 정복
#include <cmath>
#include <iostream>
using namespace std;

int result;

// count 가 홀수면 바꿔주고, 짝수면 그대로 리턴
int switching(int a, int count) {
    if ((count % 2) == 1)
        return (a == 1) ? 0 : 1;
    else
        return a;
}

void square(long long k, int count) {
    if (k == 1) {
        result = switching(0, count);
        return;
    }

    long long exponent = log2(k);
    long long n = pow(2, exponent);

    if ((k - n) != 0)
        square((k - n), ++count);
    else
        result = switching(exponent % 2, count);
}

int main() {
    long long k;  // 1 <= k <= 10^18
    cin >> k;

    square(k, 0);
    cout << result;

    return 0;
}

// 예제 입력1 : 1  -> 0
// 예제 입력2 : 2  -> 1
// 예제 입력3 : 10 -> 0

