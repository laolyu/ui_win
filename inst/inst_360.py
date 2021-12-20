# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
from lackey import *
import sys
from loguru import logger
from time import sleep

Settings.InfoLogs = False
sys.path.append(r'C:\liangdamou\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_360 import version


def install():
    t = time.strftime("%H:%M:%S")
    logger.info(t, '*******allow install*********', end=',')
    # type(Key.F11)
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 126))
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 150))
    wait(0.1)


def procp():
    t = time.strftime("%H:%M:%S")
    logger.info(t, '***************process protection************', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("procp.png").targetOffset(422, 150))
    wait(0.1)
    click(Pattern("zuzhi.png"))
    wait(0.1)


def bingdu():
    t = time.strftime("%H:%M:%S")
    logger.info(t, '***************Virus removal************', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("bingdu.png").targetOffset(159, -21))
    wait(0.1)


def UI():
    t = threading.Timer(5, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("install.png", 1):
            install()
        elif exists("procp.png", 1):
            procp()
        if exists("bingdu.png", 1):
            bingdu()
        else:
            pass
            # logger.info('no safe messages'
    except Exception as e:
        logger.info('UI-error:', e, end=',')


def cmd_send(project, path, vc_list):
    logger.info('thread %s >>%s is running...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        m = random.randint(20, 60)
        sleep(m)
        for i in range(0, 3):
            p = subprocess.Popen(cmd, cwd=path, shell=True)
            try:
                p.communicate(timeout=90)
            except subprocess.TimeoutExpired as e:
                logger.info(e, 'retry', '***********')
                subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)], shell=True)
                continue
            break
        t = time.strftime("%H:%M:%S")
        logger.info(f'{t}, {project}, {x + 1}, {vc_list[x]}')

    logger.info('thread %s >>%s is ended...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"%s,start time: %s" % (project, s1), end=',')
    logger.info("%s,end time: %s：" % (project, e1), end=',')

    start = datetime.datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(e1, '%Y-%m-%d %H:%M:%S')
    total = end - start
    if (total.seconds) > 60:
        m = float(total.seconds) / 60
        logger.info("%s,total(min)：%s" % (project, m))
    else:
        m = total.seconds
        logger.info("%s total(s)：%s" % (project, m))


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    logger.info('thread %s is running...' % threading.current_thread().name)
    path_0 = r'C:\liangdamou\package\\'
    UI()
    version = version()
    projects = list(version.keys())
    for i in list(projects):
        project = i
        path = path_0 + project
        vc_list = version[i]
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        sleep(30)
    logger.info('thread %s is ended...' % threading.current_thread().name)
