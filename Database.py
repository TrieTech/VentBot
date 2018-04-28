import sqlite3
import DataNormalizer as dn


sql_transaction = []

connection = sqlite3.connect('{}.db')

c = connection.cursor()

# Columns: phone, type, subject, body
# Data Format:
# dataRow = {phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}
# Access element when key is known: dataRow["PhoneKey"]
# Access elements in dataRow without known key:
# for data in dataRow:
#   dataRow[data]
def create_table():
    c.execute("""CREATE TABLE RECIPIENT (text_id INT PRIMARY KEY, phone TEXT, type TEXT, subject TEXT, ,body TEXT)""")
    return




def insert_row():
    c.execute("INSERT INTO RECIPIENT ")
    
# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
# Iterate: 
#   for dataRow in normalizedData:
#       for data in dataRow:
#           Processing here
def create(normalizedData):
	create_table()
	ins_query = ""



	for i in normalizedData:
			# i[dn.PHONE_KEY]
		phone = str(i[dn.PHONE_KEY])
		t_ype = str(i[dn.TYPE_KEY])
		sub = str(i[dn.SUBJECT_KEY])
		bod = str(i[dn.BODY_VALUE])
		c.execute("INSERT INTO RECIPIENT VALUES (" + phone + ", " + t_ype + ", " + sub + ", " +  bod + ")")
	return
    
def run():
    return

# Run the program
run()