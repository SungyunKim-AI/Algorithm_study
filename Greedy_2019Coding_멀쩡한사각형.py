"""
Summer/Winter Coding 2019 _ 멀쩡한 사각형

"""

import math         # 올림/내림 함수

def solution(w,h):
    a=0
    if w<h: # h가 큰경우 작은걸로 for 돌리면 
        for i in range(1,w+1):
            a += (math.ceil(h*i/w) - math.floor(h*(i-1)/w))
            # a += (math.ceil(h/w*i) - math.floor(h/w*(i-1))) # 이건 왜 안되지?
    elif w==h:
        for i in range(1,w+1):
            a += 1
    else : 
        for i in range(1,h+1):
            a += (math.ceil(w*i/h) - math.floor(w*(i-1)/h))
            # a += (math.ceil(w/h*i) - math.floor(w/h*(i-1))) # 이건 왜 안되지?
    answer = w*h - a
    return answer