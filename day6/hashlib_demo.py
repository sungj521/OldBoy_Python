#!/usr/bin/env python
# coding:utf-8
'''
Created on: 

@author: 张晓宇

Email: 61411916@qq.com

Version: 1.0

Description:

Help:
'''
if __name__ == '__main__':
    import hashlib
    m = hashlib.md5()
    m.update(b'hello')
    print(m.digest())
