def loopover_solver(mixedUpBoard, solvedBoard):
    rows, cols = len(mixedUpBoard), len(mixedUpBoard[0])
    mixedUpState = ''.join(''.join(row) for row in mixedUpBoard)
    solvedState = ''.join(''.join(row) for row in solvedBoard)
    visited = {mixedUpState: None}
    queue = [(mixedUpState, '')]
    while queue:
        state, path = queue.pop(0)
        if state == solvedState:
            return path.split()
        zero_idx = state.index('0')
        for offset in [-1, 1, -cols, cols]:
            neighbor_idx = zero_idx + offset
            if abs(offset) == 1 and zero_idx // cols != neighbor_idx // cols:
                continue  # cannot move left/right between rows, or up/down between columns
            if 0 <= neighbor_idx < rows*cols:
                new_state = state[:zero_idx] + state[neighbor_idx] + state[zero_idx+1:neighbor_idx] + '0' + state[neighbor_idx+1:]
                if new_state not in visited:
                    visited[new_state] = state
                    queue.append((new_state, path + 'LRUD'[offset]))
    return None  # unsolvable
