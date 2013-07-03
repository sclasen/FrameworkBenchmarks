import subprocess
import sys
import time
import os

def start(args=None):
    subprocess.check_call("rvm jruby 1.7.4 do bundle install", shell=True, cwd="sprack")
    subprocess.Popen("rvm jruby 1.7.4 do ./start", cwd="sprack", shell=True)
    time.sleep(5)
    return 0

def stop():
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if 'sprack' in line:
      try:
        pid = int(line.split(None, 2)[1])
        os.kill(pid, 9)
      except OSError:
        pass

  return 0
