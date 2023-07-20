class Solution:
    def romanToInt(self, s: str) -> int:
        num_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num_listado = [num_romanos[y] for y in s]
        valor = 0
        x = 0
        while x < len(num_listado) - 1:
            if num_listado[x] >= num_listado[x+1]:
                valor += num_listado[x]
            else:
                valor += num_listado[x+1] - num_listado[x]
                x += 1
            x += 1
        if num_listado[len(num_listado)-1] <= num_listado[len(num_listado)-2]:
            valor += num_listado[len(num_listado)-1]
        return valor
