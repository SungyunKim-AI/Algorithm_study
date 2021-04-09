#include <iostream>
using namespace std;

int N;
long long result = 0;

int main() {
    cin >> N;

    // 1 -> 1
    // 2 -> 2
    // 3 -> 3
    // 4 -> 4
    // 5 -> 3*2 = 6
    // 6 -> 3*3 = 9
    // 7 -> 3*4 = 12
    // 8 -> 3*3*2 = 18
    // 9 -> 3*3*3 = 27

    int k = 1;
    while (N >= 5)
    {
        k *= 3;
        k %= 10007;
        N -= 3;
    }

    cout << (N*k)%10007;
}