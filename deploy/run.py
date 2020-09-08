import os
import subprocess
import time

DELAY = 30


def check_events():
    if os.path.exists('.events/deploy-event'):
        print('The truth is out there.')
        p = subprocess.Popen(['/usr/local/bin/git', 'pull'],
            cwd='/Users/scott/repos/scott2b/fastdeploy')
        p = subprocess.Popen(['/usr/local/bin/docker-compose', 'restart'],
            cwd='/Users/scott/repos/scott2b/fastdeploy')
        os.remove('.events/deploy-event')
    else:
        print('I want to believe')


if __name__=='__main__':
    while True:
        check_events()
        time.sleep(DELAY)
