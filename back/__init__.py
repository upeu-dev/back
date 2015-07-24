import config

if config.DB['ENGINE'] == 'django.db.backends.mysql':
    import pymysql
    pymysql.install_as_MySQLdb()
