import time

while True:
    try:
        time.sleep(1)  # do something here
        print '.',

    except KeyboardInterrupt:
        print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
        try:
            response = raw_input()
            if response == 'quit':
                break
            print 'Resuming...'
        except KeyboardInterrupt:
            print 'Resuming...'
            continue

'''
import errno

try:
    # do something
    result = conn.recv(bufsize)
except socket.error as (code, msg):
    if code != errno.EINTR:
        raise
'''