//태그 : 그리디, 두 포인터
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Student {
    int d;              //해당 학생의 실력
    int M;              //해당 학생이 알고 있는 알고리즘의 수
    int A = 0;          //해당 학생이 알고 있는 알고리즘들 (1 <= K <= 30)이므로 비트마스크 연산력
} student;

//원소 개수 계산 함수
int bitCount(int x) {
    if (x == 0) return 0;
    return x % 2 + bitCount(x / 2);
}

int main() {
    //Fast IO
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    int N, K, D;    //학생의 수 (1<= N <= 10^5), 알고리즘 수 (1<= K <= 30), 학생들의 실력 차이 (0 <= D <= 10^9)
    vector<Student> students;   //student 구조체 vector

    //input
    cin >> N >> K >> D;
    for (int i = 0; i < N; i++) {
        Student tempStudent;
        cin >> tempStudent.M >> tempStudent.d;
        for (int j = 0; j < tempStudent.M; j++) {
            int A;
            cin >> A;
            tempStudent.A |= (1 << (A - 1));     //0번째 부터 넣기 위해 -1
        }
        students.push_back(tempStudent);
    }

    //학생들의 실력 기준으로 오름차순 정렬
    sort(students.begin(), students.end(),
         [] (const Student& s1, const Student& s2) -> bool {
             return s1.d < s2.d;
    });

    //조건 1 : 그룹 내에서 가장 잘 하는 학생과 가장 못 하는 학생의 실력 차이가 D 이하여야 한다.
    //조건 2 : 그룹의 효율성 E = (그룹 내의 학생들이 아는 모든 알고리즘의 수 - 그룹 내의 모든 학생들이 아는 알고리즘의 수)*그룹원의 수

    //두 포인터 알고리즘
    //low가 high 이하이고, high가 N 미만일 때 아래와 같은 상황을 계속 확인한다.
    //1. 구간 차가 D 이하일 때, high를 오른쪽으로 옮기고 count 배열 갱신
    //3. 구간 차가 D 초과일 때, low를 오른쪽으로 옮기고 count 배열 갱신
    //3-1. 이때, low가 High를 역전하고 low가 N 미만일 경우 while문의 조건을 맞추기 위해 high를 low 위치와 같게 만들고 구간을 low에서부터 다시 시작

    int E = 0;                  //스터디 그룹의 효율성
    int low = 0, high = 0;      //투 포인터 인덱스
    int algoCount[30] = {0, };  //학생들이 알고있는 알고리즘의 개수 카운트하는 배열

    while (low <= high && high < N) {
        int dif = students[high].d - students[low].d;
        if (dif <= D) {  //구간의 차가 D 이하일 때 (스터디 조건 만족)
            int num = high - low + 1;   //그룹 내 학생 수
            int algoAll = 0;            //학생들이 아는 모든 알고리즘의 수
            int stuAll = 0;             //모든 학생들이 아는 알고리즘의 수

            //high 인덱스의 학생 정보 추가
            for (int i = 0; i < K; i++) {
                if ((1 << i) & students[high].A) algoCount[i]++;
                if (algoCount[i] != 0) algoAll++;
                if (algoCount[i] == num) stuAll++;
            }

            E = max((algoAll - stuAll)* num, E);     //효율성이 더 큰 값으로 갱신
            high++;     //high를 오른쪽으로 이동

        } else {    //구간의 차가 D 초과일 때 (스터디 조건 불만족)
            //low 인덱스의 학생 정보 제거
            for (int i = 0; i < K; i++) {
                if ((1 << i) & students[low].A) algoCount[i]--;
            }
            low++;  //low를 오른쪽으로 이동
            if (low > high && low < N) high = low;
        }
    }

    cout << E;

    return 0;
}

/* input 예시
3 3 10
2 20
1 2
1 10
2
1 0
3
*/