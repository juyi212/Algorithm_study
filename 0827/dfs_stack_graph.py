while stack:
    current = stack[-1]
    # 현재 노드에서 갈 수 있는 모든 노드 검사
    visited[current] = 1
    for i in range(len(matrix[current])):
        # 현재 노드와 연결되어 있고 방문하지 않은 노드라면,
        if matrix[current][i] == 1 and visited[i] == 0:
            stack.append(i)  # 다음방문추가
            break
    else:  # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
        stack.pop()
