from mysql import connector
from mysql.connector import Error
from mysql.connector import errorcode


def connect_db():
	"""Fonction permettant de se connecter à la base de donnée"""
	try:
		conn = connector.connect(
			host='localhost',
			user='root',
			password=''
		)
		cursor = conn.cursor()
		return conn, cursor
	except connector.Error as error:
		print("probleme de connection {}".format(error))


def close_db(conn):
	"""Fonction permettant de fermer la base de donnée"""
	conn.commit()
	conn.close()