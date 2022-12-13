from datetime import time, date

dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])

[print(dd.strftime('%d/%m/%Y'), sep='\n') for dd in dates]
