# _*_coding: utf-8_*_
#defaultencoding = 'utf-8'
# @Author: r00x


import requests
import urllib
import urllib2
import subprocess
import getpass
import re
import os
import psutil
import sys


ipaddr = '192.168.0.123'

SCRIPTS_URL = 'http://192.168.1.56/scripts.tar.gz'
DESC_PATH = './scripts.tar.gz'

#match special process
match_process = ['mysql', 'redis']

#other process
other_process = []

# run_scripts = ['mule', 'mysql']
run_scripts = []


filters_all = {
  'linux': ['systemd', 'gdm', 'gnome', 'dbus', 'ibus', 'cron', 'Xorg', 'applet', 'pty', '-bash', 'bash']
}



def singleCommand(cmd, stderr=subprocess.STDOUT, shell=True):
  try:
    user = getpass.getuser()
    if user != 'root' and not re.match('\.|source|export', cmd):
      cmd = 'sudo ' + cmd
    res = subprocess.check_output(cmd, stderr=stderr, shell=shell)
    return True, res.rstrip(os.linesep)
  except subprocess.CalledProcessError, e:
    res = '%s, %s' % (e, e.output)
    newPrint('[RUN CMD ERROR]----------------', res)
    return False, res.rstrip(os.linesep)


def newPrint(*content):
  print content



def loadScripts():
  '''
  download & update plugins scripts
  '''
  print "downloading scripts -------------- "
  try:
    urllib.urlretrieve(SCRIPTS_URL, DESC_PATH)
    if not os.path.exists('./xplugins'):
      os.makedirs('./xplugins')
    success, tar_res = singleCommand('tar -zxf ' + DESC_PATH + ' -C ./xplugins')
  except Exception as e:
    print 'load scripts ERROR ',  e


def runScripts():
  '''
  run corres script
  '''
  sys.path.append("./xplugins")
  # import xoracle
  # xoracle.runscript_test()

  # '''
  for sc in run_scripts:
    print 'scrit case sc ------------------------', sc
    #run
    if sc == 'oracle':
      import xoracle
      xoracle.runscript_test()
    elif sc == 'mysql':
      success, mysql_res = singleCommand('python ./xplugins/xmysql.py ' + ipaddr)
      print 'mysql_res ---------------------------', mysql_res
      # import xmysql
      # xmysql.mainProcess()
    elif sc == 'mule':
      success, mule_res = singleCommand('python ./xplugins/xmule.py ' + ipaddr)
      print 'mule_res ---------------------------', mule_res
  # '''


def getOtherProcess(all_process):
  '''
  colect others process
  '''
  return []


def getAllPorcess():
  # success, pids_res = singleCommand('ps -ef')
  # if success:
  #   print len(pids_res.split("\n"))

  pids = psutil.pids()
  run_scripts_tmp = []
  other_process_tmp = []
  # print len(pids)
  for pid in pids:
    other = True
    p = psutil.Process(pid)
    pcmdline = p.cmdline()
    if len(pcmdline) != 0:
      print 'pid cmdline --------------------', pcmdline
      for mp in match_process:
        # if mp in pcmdline[0]:
        if mp in " ".join(pcmdline):
          run_scripts_tmp.append(mp)
          other = False

      if other:
        # other_process_tmp.append(pcmdline)
        other_process_tmp.append(" ".join(pcmdline))

  run_scripts = list(set(run_scripts_tmp))
  print 'run scripts -----------------------------', run_scripts
  print 'len other_process_tmp -----------------------------', len(other_process_tmp)
  print 'other_process_tmp -----------------------------', other_process_tmp
  # quit()

  other_process_tmp = list(set(other_process_tmp))
  other_process = filterProcess(other_process_tmp)
  print 'len other_process -----------------------------', len(other_process)
  print 'other process -----------------------------', other_process


  return []


def filterProcess(other_process_tmp):
  deal_process = other_process_tmp
  #如果平台是 linux
  filters = filters_all['linux']

  '''
  for otherp in other_process_tmp:
    filt = True
    print 'otherp --------------------------', otherp[0]
    # if otherp[0] in filters:
    #   other_process_tmp.remove(otherp)

    for f in filters:
      # if f in otherp[0] or f == otherp[0]:
      if f not in otherp[0] or f != otherp[0]:
        # other_process_tmp.remove(otherp)
        filt = False
        break

    if not filt:
      deal_process.append(otherp)
  # return  other_process_tmp
  '''


  f_list = []
  # other_process_tmp = list(set(other_process_tmp))
  for otherp in other_process_tmp:
    for f in filters:
      # print 'fileer f -------------------------', f
      # print 'otherp  -------------------------', otherp
      # if f in otherp[0] or f == otherp[0].strip():
      if f in otherp or f == otherp.strip():
        deal_process.remove(otherp)
        f_list.append(otherp)
        print 'xxxx  otherp @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', otherp
        break

    # print "--------------------------------------------------------\n\n"

  print 'f_list ----------------------------', f_list
  print 'len f_list ----------------------------', len(f_list)
  return  deal_process


def matchProcess():
  '''
  match the process we need
  '''
  match_process = {
    'oracle': [u'pmon'],
    'mysql':  [u'mysql', u'mysqld'],
    'redis':  [u'redis-server', u'redis-sentinel']
  }
  return match_process


def mainProcess():
  # loadScripts()
  getAllPorcess()
  # runScripts()


if __name__ == "__main__":
  mainProcess()





