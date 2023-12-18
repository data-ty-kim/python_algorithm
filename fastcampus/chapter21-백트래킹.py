# N Queen

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col \
        or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def dfs(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])   # 얇은 복사
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    dfs(N, 0, [], final_result)
    return final_result


print(solve_n_queens(4))
