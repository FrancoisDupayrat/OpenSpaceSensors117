#!/usr/bin/env python

import mraa
import sys
import time

# dust sensor on D6 (or anyother) on Grove Shield
class Counter:
  count = 0

c = Counter()

# inside a python interupt you cannot use 'basic' types so you'll need to use
# objects
def test(args):
  c.count+=1

x = mraa.Gpio(6)
x.dir(mraa.DIR_IN)
x.isr(mraa.EDGE_FALLING, test, test)

while (True):
  print c.count
  c.count = 0
  time.sleep(3)
