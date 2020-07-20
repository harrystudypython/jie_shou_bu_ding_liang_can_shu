# ! /usr/bin/env python
# -*- coding:utf-8 -*-


# python 接受不定量参数
import sys
import os
import re


def py_main(argv):
    print " below is Statistics for input values  "
    print len(sys.argv)
    receiver_count=len(sys.argv)
    for receive_num in range(0,receiver_count):
        print "rece_value is ",sys.argv[receive_num]
if __name__ == "__main__":
    py_main(sys.argv)
