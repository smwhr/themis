import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        # or 'sqlite:///' + os.path.join(basedir, 'themis.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://xw8wpa2pz0fqqy9u1slv:pscale_pw_kdLNzViU3nzHir1A7qowzVl9YdZRqZ1nmKYyhXzFXyO@eu-central.connect.psdb.cloud/themis?ssl={"rejectUnauthorized":true}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# import MySQLdb
# db = MySQLdb.connect(
#   host     = "eu-central.connect.psdb.cloud",
#   user     = "xw8wpa2pz0fqqy9u1slv",
#   passwd   = "pscale_pw_kdLNzViU3nzHir1A7qowzVl9YdZRqZ1nmKYyhXzFXyO",
#   db       = "themis",
#   ssl_mode = "VERIFY_IDENTITY",
#   ssl      = {
#       "ca": "/etc/ssl/cert.pem"
#   })
