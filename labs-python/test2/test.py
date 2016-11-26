import sys
import os
import hashlib
import json
import time

init_time = time.clock()

try:
    fd = open('output.json', 'w')
except Exception as E:
    print 'generic exception raised'
    print str(E)

def hash_md5(file):
    m = hashlib.md5()
    try:
        fd = open(file, 'rb').read()
    except Exception as E:
        print 'generic exception raised'
        print str(E)
        m.update('')
    else:
        m.update(open(file, 'rb').read())

    return m.hexdigest()

def hash_sha256(file):
    m = hashlib.sha256()
    m.update(open(file, 'rb').read())
    return m.hexdigest()

if len(sys.argv) > 1:
    #print os.path.realpath(sys.argv[1])
    dir =  os.path.dirname(sys.argv[1])

    big_json = {}
    for root, dirs, files in os.walk(dir):
        print 'root: ', root, type(root)
        print 'dirs: ', dirs, type(dirs)
        for file in files:
            small_json = {}
            print file
            print '\t', hash_md5(os.path.join(root, file))
            print '\t', hash_sha256(os.path.join(root, file))
            small_json['md5'] = hash_md5(os.path.join(root, file))
            small_json['sha256'] = hash_sha256(os.path.join(root, file))
            small_json['nume_fisier'] = file
            big_json[file] = small_json

    fd.write( json.dumps(big_json, sort_keys=True, indent=4, separators=(',', ':')) )
    fd.close()

print 'time elapsed: ', time.clock() - init_time