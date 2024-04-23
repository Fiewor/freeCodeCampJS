# https://leetcode.com/problems/flood-fill/

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    ROWS, COLS = len(image), len(image[0])
    initial = 0

    def bfs(r, c):
        image[sr][sc] = color
        stack = []
        vis = set()
        stack.append((r, c))

        while stack:
            row, col = stack.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in vis and image[nr][nc] == initial:
                    image[nr][nc] = color
                    vis.add((nr, nc))
                    stack.append((nr, nc))

    for r in range(ROWS):
        for c in range(COLS):
            if r == sr and c == sc:
                initial = image[r][c]
                bfs(r, c)

    return image