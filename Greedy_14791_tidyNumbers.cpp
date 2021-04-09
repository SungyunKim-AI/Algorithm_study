// Google Code Jam 2017 - Qualification Round B2
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 벡터에 있는 각 자리수의 값을 하나의 숫자로 합치는 함수
long long vec_to_long(const vector<int>& tidy) {
    long long num = 0;
    for (int i : tidy)
        num = (num * 10) + i;
    return num;
}

int main() {
    int T;      //the number of test cases
    cin >> T;
    int testCase = 0;
    while ((testCase++) != T) {
        long long N;      //the last number (1 ≤ N ≤ 10^18)
        cin >> N;

        vector<int> digits;
        while (N != 0) {
            digits.push_back(N % 10);
            N /= 10;
        }
        reverse(digits.begin(), digits.end());      // 역순으로 되어있는 숫자들을 정방향으로 재배치

        // 각 자릿수의 값에서 1을 빼고, 그 다음 자릿수의 값을 9로 바꾸면 된다.
        // 주의 : 1220, 1110 과 같이 앞뒤 숫자가 같을때 1을 빼면, 1219, 1109 처럼 예외 처리가 불가능
        // 시간 제한이 5초 이므로, 그냥 반복문을 처음부터 한번 더 돌리면서 해결
        for (int i = 0; i < digits.size() - 1; ++i) {
            for (int j = 0; j < digits.size() - 1; ++j) {
                if (digits[j] > digits[j + 1]) {
                    digits[j] -= 1;
                    for (int k = j + 1; k < digits.size(); ++k)
                        digits[k] = 9;
                    break;
                }
            }
        }

        long long result = vec_to_long(digits);
        cout << "Case #" << testCase << ": " << result << '\n';
    }
    return 0;
}
