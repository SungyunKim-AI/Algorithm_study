#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;

vector<string> dict;     //단어 저장하는 사전 벡터
vector<string> result;   //결과 문장을 저장하는 벡터

bool stringCheck(string word);
void makeString(int N, vector<int>& picked, int M);


int main() {
    int N;      //단어의 개수(1 <= N <= 25), 한 단어의 최대 길이는 100
    cin >> N;
    for (int i = 0; i < N; i++) {
        string word;
        cin >> word;
        dict.push_back(word);
    }

    //N개의 단어 중 M개를 선택하여 모든 조합을 찾는 재귀 함수(완전 탐색)
    for (int M = 1; M <= N; M++)
    {
        vector<int> picked;
        makeString(N, picked, M);      
    }
    cout << result.size();
    return 0;
}


//N개의 단어 중 M개를 선택하여 모든 조합을 찾는 재귀 함수(완전 탐색)
void makeString(int N, vector<int>& picked, int M) {

    //조합이 완성된 문장은 temp에 임시로 담아서 알파벳 26개가 모두 있는지 검사한 후 result에 push_back()
    if (M == 0) {
        string temp = "";
        for(int i = 0; i < picked.size(); i++) {
            temp += dict[picked[i]];
        }
        if (temp.size() >= 26 && stringCheck(temp)) { result.push_back(temp); }
        return; 
    }

    // M이 0이 될때까지 재귀 호출하며 문장 조합
    int smallest = picked.empty() ? 0 : picked.back() + 1;
    for (int next = smallest; next < N; next++)
    {
        picked.push_back(next);
        makeString(N, picked, M - 1);
        picked.pop_back();
    }

}


// 알파벳이 26개 다 있는지 검사하고, 26개 다 있으면 true, 없으면 false 반환.
bool stringCheck(string str) {   
    set<char> alphabet;
    for (int i = 0; i < str.size(); i++) {
        alphabet.insert(str.at(i));
        if(alphabet.size() == 26) { return true; }   
    }
    return false;
}