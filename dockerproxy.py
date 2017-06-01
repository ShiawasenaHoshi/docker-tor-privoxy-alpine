import os
import re

import sys

cmdStart = 'docker run -d -p {0}:8118 -p {1}:9050 shiawasenahoshi/tor'
cmdStop = 'docker stop {0}'
cmdPs = 'docker ps'
containerRegex = '^(.*?)\s*?shiawasenahoshi/tor'
startportHttp = 10000
startportSocks = 11000
def start(count):
    for i in range(count):
        curportHttp = startportHttp + i
        curportSocks = startportSocks + i
        cmd = cmdStart.format(curportHttp, curportSocks)
        call(cmd)
        if i == 999:
            break


def stopAll():
    out = os.popen(cmdPs).read()
    for l in out.splitlines():
        try:
            container = re.search(containerRegex, l)
            stop(container.group(1))
        except BaseException:
            continue

def stop(containerId):
    call(cmdStop.format(containerId))

def call(cmd):
    print cmd
    return os.popen(cmd).read()


if sys.argv.__contains__("-s"):
    print sys.argv
    start(int(sys.argv[2]))
elif sys.argv.__contains__("-S"):
    print sys.argv
    stopAll()