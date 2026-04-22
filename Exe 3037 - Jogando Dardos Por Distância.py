# -*- coding: utf-8 -*-

num = int(input())
somamaria = somajoao = 0
for cont in range (num):
    # JOÃO
    jp,jd = map(int,input().split())
    jp1, jd1 = map(int,input().split())
    jp2, jd2 = map(int,input().split())
    somajoao = (jp * jd) + (jp1 * jd1) + (jp2 * jd2)
    # MARIA
    mp,md = map(int,input().split())
    mp1,md1 = map(int,input().split())
    mp2,md2 = map(int,input().split())
    somamaria = (mp * md) + (mp1 * md1) + (mp2 * md2)

    if somajoao > somamaria:
        print("JOAO")
    elif somamaria > somajoao:
        print("MARIA")
