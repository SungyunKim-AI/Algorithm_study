#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Student {
    int M;          //해당 학생이 알고 있는 알고리즘의 수
    int d;          //해당 학생의 실력
    vector<int> A;  //해당 학생이 알고 있는 알고리즘들 (1 <= Ai <= K)
} student;

// 학생들을 실력기준으로 오름차순 정렬
bool cmp(const Student & a, const Student & b) {
    if (a.d < b.d) return true;
    else if (a.d == b.d) {
        if (a.M < b.M) return true;
    }
    return false;
}

//알고리즘 카운트 배열을 확인해서 (그룹 내의 학생들이 아는 모든 알고리즘의 수 - 그룹 내의 모든 학생들이 아는 알고리즘의 수) 반환
int difCalculater(int arrK[31], int N) {
    int allAlgo = 0;    //그룹 내의 학생들이 아는 모든 알고리즘의 수
    int allStud = 0;    //그룹 내의 모든 학생들이 아는 알고리즘의 수
    for (int i = 1; i <= 30; i++) {
        if (arrK[i] == N) { allStud++; }
        if (arrK[i] != 0) { allAlgo++; }
    }
    return allAlgo - allStud;
}

int main() {
    //입출력 시간 줄이기
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    
    int N, K, D;    //학생의 수 (1<= N <= 10^5), 알고리즘 수 (1<= K <= 30), 학생들의 실력 차이 (0 <= D <= 10^9)
    vector<Student> students;   //student 구조체 vector
    
    //input
    cin >> N >> K >> D;
    for (int i = 0; i < N; i++) {
        cin >> student.M >> student.d;
    
        for (int j = 0; j < student.M; j++) {
            int Ai;
            cin >> Ai;
            student.A.push_back(Ai);
        }

        students.push_back(student);
        student.A.clear();
    }

    //조건 1 : 그룹 내에서 가장 잘 하는 학생과 가장 못 하는 학생의 실력 차이가 D 이하여야 한다.
    //조건 2 : 그룹의 효율성 E = (그룹 내의 학생들이 아는 모든 알고리즘의 수 - 그룹 내의 모든 학생들이 아는 알고리즘의 수)*그룹원의 수

    sort(students.begin(), students.end(), cmp);    //실력 기준으로 오름차순 정렬
    

    //두 포인터 알고리즘
    //low가 high 이하이고, high가 N 미만일 때 아래와 같은 상황을 계속 확인한다.
    //1. 구간 차가 D보다 작다면 high를 하나 더 오른쪽으로 가고 해당 숫자 구간 갱신
    //2. 구간 차가 D와 같다면 경우의 수를 늘려주고 high를 하나 더 오른쪽으로 가고 해당 숫자도 구간 합에 더해준다.
    //3. 구간 차가 D 보다 크다면 low를 하나 더 오른쪽으로 가주고 숫자 값 갱신
    //3-1. 이때, low가 High를 역전하고 low가 N 미만일 경우 while문의 조건을 맞추기 위해 high를 low 위치와 같게 만들고 구간을 low에서부터 다시 시작
    
    int resultE = 0;        //스터디 그룹의 효율성
    int low = 0, high = 1;
    int arrK[31] = {0, };   //각각의 알고리즘 카운트하는 배열

    while (low <= high && high < N) {
        int dif = students[high].d - students[low].d;

        if (dif <= D) {  //high를 오른쪽으로 이동
            //n^2 -> 수정
            for (int i = low; i < high; i++) {
                for (int j = 0; j < students[i].M; j++) {
                    arrK[students[i].A.at(j)]++;
                }   
            }
            int num = high - low + 1;     //그룹의 학생 수
            resultE = max(difCalculater(arrK, num) * num, resultE);     //효율성이 더 큰 값으로 갱신
            high++;
        } else {        //low를 오른쪽으로 이동
            low++;
            if (low > high && low < N) {
                high = low;    
            } 
        }
    }
    
    cout << resultE;

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