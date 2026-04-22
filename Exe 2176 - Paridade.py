# -*- coding: utf-8 -*-

msg = input()
quantidade = msg.count("1")
quantidade = int(quantidade)
if quantidade % 2 == 0:
    msg = msg + "0"
else:
    msg = msg + "1"
print(msg)
