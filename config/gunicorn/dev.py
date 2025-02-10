
wsgi_app = 'config.wsgi:application'
bind = "0.0.0.0:8002"
workers = 1

worker_class = "sync"

loglevel = "debug"

# accesslog = "/var/log/gunicorn/access.log"
# errorlog = "/var/log/gunicorn/error.log"

reload = False

proc_name = "dar_llc_backend_gunicorn"
