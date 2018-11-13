from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pymysql

app = Flask(__name__)
api = Api(app)

transactions = [
	{
		"Employee":"Rick",
		"Name on Card":"",
		"Region Code":"TBD",
		"Allocated Business Unit Code":00000,
		"Allocated Business Unit Name":"Dallas",
		"Allocated Team Name":"Sogeti",
		"Allocated Team":"666",
		"Allocated Sub-Team Name":"",
		"Allocated Sub-Team":"",
		"Report Name":"Flask Test",
		"Paid Date":"",
		"Approval Status":"",
		"Payment Status":"",
		"Expense Type":"",
		"Transaction Date":"",
		"Vendor":"",
		"Payment Type":"",
		"Expense Amount":"",
		"Reimbursement Currency":"",
		"Fraud_Trans_Flag":"F-Illegal Operation"
	}
]

class Transaction(Resource):

	def get(self, Employee):
		conn = pymysql.connect("localhost","root","Adin2015","reports")
		cursor = conn.cursor()
		
		try:
			#test with Popola, Denise D
			cursor.execute("select * from transactions where Employee like '%s';" % Employee)
			data = cursor.fetchall() 
			if(cursor.rowcount > 0):
				return jsonify(data)
			else:
				return "Employee not found", 404

		except Exception as e:
			print(e)

		cursor.close()
		conn.close()
	

api.add_resource(Transaction,"/transaction/<string:Employee>")
app.run(debug=True) 