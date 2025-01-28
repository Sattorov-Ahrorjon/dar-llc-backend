
bind = "127.0.0.1:8000"
workers = 4

worker_connections = 1000

worker_class = "sync"

loglevel = "debug"

accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"

reload = False

proc_name = "dar_llc_backend_gunicorn"
