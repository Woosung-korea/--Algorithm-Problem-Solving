import sys
import heapq


def main():
    n, m, k = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        connect[a].append([b, c])
    disList = [[] for i in range(n + 1)]
    disList[1].append([0])
    hq = []
    heapq.heappush(hq, [0, 1])
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        d, pos = tmp[0], tmp[1]
        for nxt in connect[pos]:
            nxtP, tDis = nxt[0], nxt[1] + d
            l = len(disList[nxtP])
            if l < k: # k개보다 적은 거리들이 있을경우
                if bSearch(disList[nxtP], tDis) == 0:  # tDis가 없는 경우에만 추가해준다
                    disList[nxtP].append(tDis)
                    disList[nxtP].sort()
                    heapq.heappush(hq, [tDis, nxtP])
            else:  # 이미 k개가 꽉찬 경우
                maxDis = disList[nxtP][-1]
                if tDis < maxDis: # 최대 거리보다 더 작은 값을 집어넣어야 함
                    if bSearch(disList[nxtP], tDis) == 0:
                        disList[nxtP].pop()
                        disList[nxtP].append(tDis)
                        disList[nxtP].sort()
                        heapq.heappush(hq, [tDis, nxtP])
    for i in range(1, n + 1):
        if len(disList[i]) < k:
            print(-1)
        else:
            print(disList[i][k - 1])


def bSearch(nList, val):
    left, right = 0, len(nList) - 1
    while left <= right:
        mid = (left + right) // 2
        if nList[mid] == val:
            return 1
        if nList[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return 0


if __name__ == "__main__":
    main()
