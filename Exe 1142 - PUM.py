# -*- coding: utf-8 -*-

n = int(input())
a = [1,2,3]
for cont in range(1,n+1):
    print(*a, "PUM")
    a[0] = a[2] + 2
    a[1] = a[0] + 1
    a[2] = a[0] + 2

