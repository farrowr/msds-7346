import sqlalchemy as sqlal
import pandas as pd
import numpy as np
####################
#MySQLdb is the interface to MySQL database. As mentioned by other posts, 
#MySQLdb doesn't support Python 3.x. I used PyMySQL as the replacement. 
#You need to install it first:
#pip install PyMySQL #need to install this in terminal
##############
import pymysql
pymysql.install_as_MySQLdb()

#df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
#print(df)
#exit()

df = pd.read_csv('outfile.csv',sep=',',delimiter=None,header='infer')

database_username = 'root'
database_password = 'Adin2015'
database_ip		  = 'localhost:3306'
database_name 	  = 'reports'

database_connection = sqlal.create_engine('mysql://root:Adin2015@localhost:3306/reports')
#database_connection = sqlal.create_engine('mysql://{0}:{1}@{2}/{3}'.
#	format(database_username,database_password,database_ip,database_name))
df.to_sql(con=database_connection,name='transactions',if_exists='replace') #TODO replace

