"""
백준 11659(실버3) : 수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합 구하기
Input  : 데이터의 개수, 질의 개수, 구간합을 구할 대상 배열
Output : 총 M개의 줄에 입력으로 주어진 i번째 수에서 j번째 수까지의 합 출력
"""
import sys

if __name__=="__main__":
    input = sys.stdin.readline
    suNo, quizNo = map(int, input().split())
    numbers = list(map(int, input().split()))

    prefix_sum = [0]                                 # []로 선언하지 않고, [0]으로 선언하는 이유
    temp = 0
    for num in numbers:
        temp += num
        prefix_sum.append(temp)
        
    # print(prefix_sum)
        
    for _ in range(quizNo):
        i, j = map(int, input().split())
        print(prefix_sum[j] - prefix_sum[i-1])      # 0이 없다면 여기서 i-1을 할때, i==0 이라면 out of range 나오게됨