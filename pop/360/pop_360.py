# -*- coding: UTF-8 -*-

from lackey import *
import datetime
import time
import subprocess
import threading
import psutil
from loguru import logger

Settings.InfoLogs = False

sys.path.append(r'C:\AI\script\gjl')
from config import *


def install():
    logger.info('****allow install*****', end=',')
    # type(Key.F11)
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 124))
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 150))
    wait(0.1)


def procp():
    logger.info('****process protection*****', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("procp.png").targetOffset(116, 124))  # no mention188*320
    wait(0.1)
    click(Pattern("procp.png").targetOffset(326, 124))
    wait(0.1)


def fil():
    logger.info('****files protection*****', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("fil.png").targetOffset(116, 150))  # no mention188*370
    wait(0.1)
    click(Pattern("fil.png").targetOffset(478, 150))  # ^-188*370
    wait(0.1)
    click(Pattern("fil.png").targetOffset(478, 230))
    wait(0.1)


def reg():
    logger.info('****files protection*****', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("reg.png").targetOffset(116, 150))  # no mention188*370
    wait(0.1)
    click(Pattern("reg.png").targetOffset(478, 150))  # ^-188*370
    wait(0.1)
    click(Pattern("reg.png").targetOffset(478, 230))
    wait(0.1)


def bingdu():
    logger.info('****Virus removal*****', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("bingdu.png").targetOffset(159, -21))
    wait(0.1)


def explorer(jpg='explorer.jpg'):
    if exists(jpg, 1):
        # find(jpg).highlight(1)
        wait(0.5)
        type(Key.F11)
        logger.info('*******explorer stopped*********')
        wait(0.1)
        click(Pattern(jpg).targetOffset(0, 100))
        wait(0.1)
    if not exists('player.jpg', 4):
        type(Key.F11)
        logger.info('++explorer&playernot found++')
        try:
            subprocess.Popen('powershell.exe Stop-Process -name explorer', shell=True)
        except Exception as e:
            logger.info(e)
        try:
            subprocess.Popen('explorer', shell=True)
        except Exception as e:
            logger.info(e)


def UI():
    t = threading.Timer(20, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("install.png", 1):
            install()
        if exists("fil.png", 1):
            fil()
        if exists("procp.png", 1):
            procp()
        if exists("reg.png", 1):
            reg()
        elif exists("bingdu.png", 1):
            bingdu()
        else:
            pass
            # print('no safe messages'
    except Exception as e:
        logger.info(e)


def result():
    try:
        subprocess.check_call(r'"C:\Program Files\360\360safe\safemon\360LogCenter.exe" /id=2000', shell=True)
        type(Key.F11)
    except Exception as e:
        logger.info(e)


def inst(package):
    try:
        subprocess.check_call(r'net use \\172.18.15.3 "2020"  /user:"administrator"', shell=True)
        subprocess.check_call(r'net time \\172.18.15.3 /set /y')
        date = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d %H:%M:%S")
        t = '06.00.00'
        subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)

    for i in range(0, 2):
        p = subprocess.Popen(package, shell=True)
        try:
            p.communicate(timeout=180)
        except subprocess.TimeoutExpired as e:
            logger.info(e)
            subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(p.pid)], shell=True)
            continue
        break
    time.sleep(10)


def setTime2M():
    try:
        subprocess.check_call(r'net use \\172.18.15.3 "2020"  /user:"administrator"', shell=True)
        subprocess.check_call(r'net time \\172.18.15.3 /set /y', shell=True)

        # try:
        #     date = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        #     t = '10.58.00'
        #     subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)


def setTime2T():
    try:
        date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        t = '16.58.00'
        subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        try:
            if psutil.Process(pid).name() == f'{process_name}.exe':
                type(Key.F11)
                time.sleep(2)
                subprocess.check_call(f'taskkill /F /IM {process_name}.exe', shell=True)
                logger.info(f'taskkill /F /IM {process_name}.exe, successed')
        except Exception as e:
            pass


def kill_p(p_list, updc):
    updc_proc = updc.split('/')[-1]
    proc_exist(updc_proc)
    proc_exist('iexplore')

    for i in range(len(p_list)):
        process_name = p_list[i]
        proc_exist(process_name)
        time.sleep(0.4)


def pb():
    pb_list = ['bqpb', 'xypbuninst', 'Kuaipb', 'parpbuninst', 'ktpb', 'ktpbuninst', 'pbxhone', 'xhpbuninst', 'GSscreensaver', 'sspbuninst', '7654pb']
    try:
        subprocess.check_call('@reg add "HKEY_CURRENT_USER\Software\ScreenSaver" /v "ScreenSaveTimeOut" /t REG_DWORD /d "15" /f>nul', shell=True)
    except Exception as e:
        logger.info(e)
    finally:
        time.sleep(20)

    for i in range(len(pb_list)):
        process_name = pb_list[i]
        proc_exist(process_name)


def b4hand(project, package, updc, p_list):
    UI()
    inst(package)
    setTime = [setTime2M]
    for i in range(len(setTime)):
        try:
            logger.info('*****city.bat********')
            subprocess.check_call("C:\AI\script\city.bat", shell=True)
        except Exception as e:
            pass

        setTime[i]()
        try:
            subprocess.Popen(f'{updc}.exe', shell=True)
            logger.info(f'**1***{updc}.exe********')
        except Exception as e:
            logger.info(e)
        time.sleep(10)
        try:
            subprocess.Popen(f'{updc}.exe', shell=True)
            logger.info(f'**2***{updc}.exe********')
        except Exception as e:
            logger.info(e)
        finally:
            explorer()
            time.sleep(180)

        if project in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
            pb()
        try:
            kill_p(p_list, updc)
        except Exception as e:
            logger.info('kill_p(p_list, updc)', e)
        try:
            logger.info('delete.bat')
            subprocess.check_call("C:\AI\script\delete.bat", shell=True)
        except Exception as e:
            pass


if __name__ == '__main__':
    logger.add("C:/AI/log/gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    projects = [xiaoyu, kuaizip, kantu, heinote, finder, browser, lszip, xinnote, qjpdf, cloudbar, haotu, xxbz, sesame, jcbz]
    for i in range(len(projects)):
        project = projects[i]
        package = project['package']
        updc = project['updc']
        p_list = project['p_list']
        b4hand(project, package, updc, p_list)
