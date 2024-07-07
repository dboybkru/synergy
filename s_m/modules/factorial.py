def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)


def factfor(n):
  summa = 1
  for i in range(1, n + 1):
    summa *=i
  return summa
