import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
# 테스트 케이스 받아오는 코드
'''
연산 1 : 삽입 ((1 x) 형태로 입력)
연산 2 : 루트 노드 출력 후 삭제 

입력 :
# 테스트 케이스 수 : T
# 첫째 줄에 수행해야하는 연산의 수 : N
# 1번 테스트 케이스의 입력 해석
N = 3 | 연산 목록 => 1. 1 1 / 2. 2 / 3. 2
순서대로, 힙 트리에 1을 넣고, 루트 노드를 출력을 2회 실시한다.
그 결과, 첫번째 출력 시도에서는 힙 트리에 1이 존재하기 때문에 1이 출력되고,
1은 힙 트리에서 삭제된다.
두번째 출력 시도에서는 힙 트리에 남아있는 데이터가 없음으로 -1이 출력된다.

# 2번 테스트 케이스의 입력 해석
N = 5 | 연산 목록 => 1. 1 3 / 2. 1 5 / 3. 2 / 4. 1 1 / 5. 2
순서대로, 힙 트리에 3, 5를 넣고, 루트 노드를 출력을 1회 실시한다.
그 후에 다시 힙 트리에 1을 넣고, 루트 노드를 출력한다.
그 결과, 첫번째 출력 시도에서는 힙 트리에 3, 5가 존재하기 때문에 5가 출력되고,
5는 힙 트리에서 사라지며, 루트 노드는 3이 된다.
두번째 출력 시도에서는 힙 트리에 1, 3이 존재함으로 3이 출력된다.
'''


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, v):
        """ 최대 힙에 값 추가 """
        self.heap.append(v)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """ 최대 힙의 루트 노드를 제거하고 반환 """
        if not self.heap:
            return -1
        root = self.heap[0]
        self.heap[0] = self.heap[-1]  # 루트 노드를 마지막 원소와 교체
        self.heap.pop()  # 마지막 원소 제거 (O(1))
        self._heapify_down(0)  # 힙 성질 유지
        return root

    def _heapify_up(self, idx):
        """ 새로운 원소를 삽입할 때, 상향식 정렬 (heapify-up) """
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _heapify_down(self, idx):
        """ 루트 노드를 제거할 때, 하향식 정렬 (heapify-down) """
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == idx:
                break
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest


# ✅ 클래스 적용 후 실행 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = MaxHeap()
    res = []

    for _ in range(N):
        quest = list(map(int, input().split()))
        if quest[0] == 2:
            res.append(heap.pop())
        else:
            heap.push(quest[1])

    print(f"#{tc}", *res)

'''
# 함수로 구현
def max_heap(v):
    global tmp
    tmp.append(v)
    nn = len(tmp)-1
    p = (nn-1) // 2
    while nn > 0 and tmp[nn] > tmp[p]:
        tmp[nn], tmp[p] = tmp[p], tmp[nn]
        nn = p
        p = (nn - 1) // 2


def setting_heap(idx=0):
    global tmp
    n = len(tmp)
    xl = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    if left < n and tmp[left] > tmp[xl]:
        xl = left
    if right < n and tmp[right] > tmp[xl]:
        xl = right
    if xl != idx:
        tmp[idx], tmp[xl] = tmp[xl], tmp[idx]
        setting_heap(xl)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tmp, res = [], []
    for i in range(1, N+1):
        quest = list(map(int, input().split()))
        if quest[0] == 2:
            if tmp:
                res.append(tmp[0])
                tmp[0] = tmp[-1]
                tmp.pop()
                setting_heap()
            else:
                res.append(-1)
            continue
        max_heap(quest[1])
    print(f"#{tc}", *res)
'''
