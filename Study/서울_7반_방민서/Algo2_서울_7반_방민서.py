# import sys
# sys.stdin = open('algo2_sample_in.txt', 'r')
####################################################
from itertools import combinations
'''
M분 이상의 재생시간이 필요한 새로운 플레이리스트를 만드려고 한다. 
N곡의 음악 
각 곡의 재생시간은 (song[i])
선택한 곡의 개수는 L 개 이하를 선택한 플레이리스트 중 가장 재생 시간이 적은 플리의 재생 시간을 출력 
만약 주어진 N개의 음악으로 L개 이하의 음악을 선택해서 M분 이상의 플레이리스트를 만드는 것이 불가한 경우 -1을 출력 

'''

T = int(input())
for test_case in range(1,T+1):
    N,M,L = list(map(int,input().split()))  # N: 주어진 음악리스트의 길이 / M: ~이상의 재생시간(기준) / L: 꼭 선택해야 하는 개수
    songs = list(map(int,input().split()))
    playlist = []
    #L개 이하의 부분집합을 구해준다.
    for l in range(1,L+1):
        playlistcombinations = list(combinations(songs,l))
        for i in range(len(playlistcombinations)):
            playlistsum = sum(list(playlistcombinations[i]))
            if playlistsum >=M:
                playlist.append(playlistsum)
    if playlist == []:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {min(playlist)}")

# def DFS(N,M,L,songs):
#     # 방문했는지 체크하는 배열
#     visited = [[0]*N]
#     stack = []
#     playlist = []
#     # 재귀적으로 생각을 해보자...어떤 부분이 반복되어야 할까?
#     # 더이상 visited 할 값이 없으면 스택에 담긴 값을 pop해서 반환시켜야 한다.
#     # 만약에 방문하지 않은 값이 남아있다면
#     while stack:
#
#         if not visited:
#             visited[ni] = 1
#             stack.append(songs[ni])
#         if visited:
#             return song
#     # # 하나씩 값을 넣어준다.
#     # for i in range(N):
#     #     stack.append(songs[i])
#     # # 하나씩 값을 가져와 리스트에 저장
#     # song.append(stack.pop()) #아...시간복잡도...
#     #
#     # # 리스트의 값들의 합을 구해서 M과 비교
#     # if sum(song) >= M:
#
#     # 리스트의 개수 초과이면 계산하지 않는다.
#
# # DFS로 풀기
# T = int(input())
# for test_case in range(1,T+1):
#     N,M,L = list(map(int,input().split()))  # N: 주어진 음악리스트의 길이 / M: ~이상의 재생시간(기준) / L: 꼭 선택해야 하는 개수
#     songs = list(map(int,input().split()))
#     playlist = []
#     #L개 이하의 부분집합을 구해준다. -> 재귀를 이용한 DFS로 구현 가능
#     #L 개 이하의 부분집합
#     # 방문한지 안하니
#     DFS(N,M,L,songs)

