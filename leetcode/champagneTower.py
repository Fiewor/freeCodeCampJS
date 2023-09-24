# https://leetcode.com/problems/champagne-tower/

def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    tab = [[0] * x for x in range(1, 102)]

    tab[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            quantity = (tab[r][c] - 1.0) / 2.0

            if quantity > 0:
                tab[r + 1][c] += quantity
                tab[r + 1][c + 1] += quantity
    
    return min(1, tab[query_row][query_glass])