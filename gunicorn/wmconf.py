import multiprocessing

workers = multiprocessing.cpu_count() + 1
bind = '127.0.0.1:8900'
daemon = True
pidfile = '/tmp/wm.pids'
accesslog= '/tmp/wmaccess.log'
errorlog= '/tmp/wmerror.log'
loglevel= 'debug'
