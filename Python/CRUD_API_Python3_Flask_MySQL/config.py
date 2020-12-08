from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
app.config['MYSQL_DATABASE_USER'] = 'flaskapiuser'
app.config['MYSQL_DATABASE_PASSWORD'] = '12WWdsff!er3SSd8Yz3KK!c?aerwfsvVa22'
app.config['MYSQL_DATABASE_DB'] = 'FlaskP3Api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
mysql.init_app(app)
