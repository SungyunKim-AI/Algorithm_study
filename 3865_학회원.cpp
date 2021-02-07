#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<string> split(string str, char delimiter);

int main() {

    vector<int> result;
    while (1) {     //여러 테스트 케이스가 가능 하도록 반복문 사용
        string str;
        getline(str);
        if (str == "0") break;

        int N;
        if (str.length() < 4) {
            N = stoi(str);      // 학회 수 N 저장
        } else {

            vector<string> academy;     //학회 저장
            vector<string> name;
            for (int i = 0; i < N; i++) {
                getline(str);
                vector<string> temp = split(str, ":");
                academy.push_back(temp[0]);
                name = split(temp[1], ",");
            }



        }


    }

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }

    return 0;
}

vector<string> split (string input, char delimiter) {
    vector<string> answer;
    stringstream ss(input);
    string temp;

    while (getline(ss, temp, delimiter)) {
        answer.push_back(temp);
    }

    return answer;
}