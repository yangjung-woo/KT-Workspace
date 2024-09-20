n = int(input())

scores = []
for i in range(n):
    
    (paper , meet) = tuple(map(int, input().split()))
    scores.append((paper,meet))

rank = [1] * n  # 등수 전부 1로 초기화 

for i in range(n):
    for j in range( i +1, n):
        if i != j:
            if (scores[i][0] > scores[j][0]) and (scores[i][1] > scores[j][1]) or ((scores[i][0] == scores[j][0] and scores[i][1] > scores[j][1]) or(scores[i][0] > scores[j][0] and scores[i][1] == scores[j][1])): # i 보다 낮은 성적이면  j=i+ 1
                rank[j] = rank[j] +  1
                
            elif (scores[i][0] < scores[j][0]) and (scores[i][1] > scores[j][1]) or (scores[i][0] > scores[j][0]) and (scores[i][1] < scores[j][1]) or(scores[i][0] == scores[j][0] and scores[i][1] == scores[j][1]):
                rank[i] = rank[j] = min(rank[i], rank[j])
            else:
                pass
for r in rank:            
    print(r ,end = ' ')

'''
# 라벨을 등수로 변환
label_to_rank = {}
current_rank = 1

for label in sorted(set(rank)):
    label_to_rank[label] = current_rank
    current_rank += rank.count(label)

final_rank = [label_to_rank[label] for label in rank]

for f in final_rank:
    print(f,end=' ')

'''
