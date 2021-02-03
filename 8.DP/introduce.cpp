/*
 * Dynamic Programming (동적 계획법)화
 *  - 재귀 함수에서 두 번 이상 반복 계산되는 부분 문제들의 답을 미리 저장함으로써 속도의 향상을 꾀하는 알고리즘 설계 기법
 *
 * 1. (예시) 이항 계수 (binomial coefficient)
 *    - (n r) : n개의 서로 다른 원소 중에서 r개의 원소를 순서없이 골라내는 방법의 수
 *    - 점화식 : (n r) = (n-1 r-1) + (n-1 r)
 *    - 코드 : int bino (int n, int r) {
 *              if (r==0 || n==r) return 1;
 *              return bino(n-1, r-1) + bino(n-1, r);
 *            }
 *    - 문제점 : 예를 들어 bino(4,2)를 계산한다고 했을 때, bino(2,1)는 bino(3,1), bino(3,2) 에서 호출되므로 중복 호출된다.
 *             여기서 n, r이 커지면 호출 횟수는 기하 급수적으로 증가하게 되므로 매우 비효율적이다.
 *    - 해결 방법 : 입력인 n, r이 정해져 있을 때 bino(n,r)의 반환 값이 일정하다는 것을 이용하여 각 n,r조합에 대해 답을 저장하는 캐시 배열을 만들고,
 *               각 입력에 대한 반환 값을 저장한다.
 *               함수는 매번 호출될 때마다 이 배열에 접근해 값이 저장되어 있는지 확인한 뒤, 저장되어 있다면 반환하고 저장이 안되어 있으면 저장후 반환.
 *               이를 메모이제이션이라고 한다.
 *
 *     - 문제점을 해결한 코드
 *     int cache[30][30];       //-1로 초기
 *     int bino2(int n, int r) {
 *       //기저 사례
 *       if (r==0 || n==r) return 1;
 *       //-1이 아니라면 한 번 계산했던 값이니 바로 반환
 *       if(cache[n][r] != -1) return cache[n][r];
 *       //-1이면 직접 계산한 뒤 배열에 저장
 *       return cache[n][r] = bino2(n-1, r-1) + bino2(n-1, r);
 *
 * 2. 메모이제이션을 적용할 수 있는 경우
 *  - 참조적 투명함수의 경우에만 적용 가능
 *  - 참조적 투명 : 함수의 반환 값이 그 입력 값만으로 결정되는 함수
 *  - 즉, 입력이 같더라도 외부 요소에 따라 다른 값이 반환된다면 캐싱을 할 수가 없다.
 *
 * 3. 메모이제이션 구현 패턴
 *  - 패턴을 정해놓고 구현하면 작성하기도 편하고, 오류 고치기도 편하기 때문에 항상 같은 패턴으로 구현하도록 한다.
 *
 *  - 예시: int someObscureFunction(int a, int b) 라는 재귀 함수가 있다.
 *      1. 항상 기저 사례를 제일 먼저 처리한다.
 *      2. 함수의 반환 값이 항상 0 이상이라는 점을 이용해 cache[]를 모두 -1로 초기화 한다.
 *      3. int& ret = cache[a][b] : 매번 귀찮게 cache[][]라고 할 필요도 없고, 인덱스 에러가 날 확률도 낮춰준다.
 *      4. memset()으로 cache 배열을 초기화 한다.
 *
 *      int cache[2500][2500];
 *      int someObscureFunction(int a, int b) {
 *          // 기저 사례 먼저 처리
 *          if (...) return ...;
 *          // (a, b)에 대한 답이 cache에 있으면 바로 반환
 *          int& ret = cache[a][b];
 *          if (ret != -1) return ret;
 *          //여기에서 답을 계산한다.
 *          ...
 *          return ret;
 *      }
 *
 *      int main() {
 *          //memset()을 이용해 cache 배열을 초기화 한다.
 *          memset(cache, -1, sizeof(cache));
 *      }
 *
 *
 * */