def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].insert(j, arr1[i][j] + arr2[i][j])
    print(answer)

arr1 = [[1],[2]]
arr2 = [[3],[4]]
solution(arr1, arr2)
