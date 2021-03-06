from random import randint
import time

#배열에 10,000개의 정수를 삽입
array = []
for _ in range(300):
    array.append(randint(1, 100))
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

end_time = time.time()
print("선택 정렬 성능 측정", end_time - start_time)
start_time = time.time()

array.sort()

end_time = time.time()

print("라이브러리 성능 측정", end_time - start_time)