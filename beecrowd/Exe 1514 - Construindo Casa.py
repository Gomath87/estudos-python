# -*- coding: utf-8 -*-
A, B, C = map(int, input().split())

if A > B and (B < C or B == C):
    print(":)")
elif A < B and (B > C or B == C):
    print(":(")

if A < B and B < C:
    if (B - A) > (C - B):
        print(":(")
elif A < B and B < C:
    if (C - B) >= (B - A):
        print(":)")

if A > B and B > C:
    if (B - C) < (A - B):
        print(":)")
elif A > B and B > C:
    if (B - C) <= (A - B):
        print(":(")

if A == B and B < C:
    print(":)")
elif A == B and B > C:
    print(":(")


