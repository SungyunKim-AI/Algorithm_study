#include <iostream>
#include <string>
using namespace std;

int main() {
    string cipher;
    cin >> cipher;

    // 점화식
    // dp[n] = (dp[n] + dp[n-1]) + (dp[n] + dp[n-2])
    int dp[5000];
    for (int i = 1; i <= cipher.length(); i++) {

    }



    return 0;
}


//1. 3개 이상의 숫자를 합칠 수는 없다.
//2. 3~9는 두자리로 합칠 수 없다.
//3. 0은 무조건 앞에 다른 숫자와 함께 와야 한다.
//4. 7~9는 앞에 2가 올수 없다.