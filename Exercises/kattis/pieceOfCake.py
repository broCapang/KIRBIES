n, h, v = map(int, input().split())
print((n - h if n - h > h else h) * (n - v if n - v > v else v) * 4)