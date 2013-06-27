
import subprocess
import sys
import setup_util

def start(args):

  try:
    subprocess.check_call("rvm jruby-1.7.4 do bundle install --gemfile=Gemfile", shell=True, cwd="sinatra-sprack")
    subprocess.check_call("rvm jruby-1.7.4 do JAVA_OPTS='-Xmx5g -Xmn3g -Djruby.compile.invokedynamic=true -XX:+UseParallelOldGC' bundle exec sprack", shell=True)
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop():
  try:
    subprocess.check_call("killall java")
    subprocess.check_call("rm Gemfile", shell=True, cwd="sinatra-sprack")
    subprocess.check_call("rm Gemfile.lock", shell=True, cwd="sinatra-sprack")
    return 0
  except subprocess.CalledProcessError:
    return 1
