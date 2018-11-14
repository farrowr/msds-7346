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

	def get(self, Date):
		conn = pymysql.connect("localhost","root","Adin2015","reports")
		cursor = conn.cursor()
		
		try:
			d = Date
			#d = '1-16-17'
			d = d.replace('-','/') + ' 0:00'
			cursor.execute("select * from transactions where fraud_trans_flag is not null and `Transaction Date` = '%s' order by Employee asc;" % d)
			
			row_headers = [x[0] for x in cursor.description] #extract row headers
			data = cursor.fetchall()

			json_data = []
			for result in data:
				json_data.append(dict(zip(row_headers,result)))
				#json_data.append("data")
			#	json_data.append(dict(zip(row_headers,result)))
			#return json.dumps(json_data)
			return jsonify(json_data)

			#if(cursor.rowcount > 0):
			#	return jsonify(data)
			#else:
			#	return "Employee not found", 404

		except Exception as e:
			print(e)

		cursor.close()
		conn.close()
	

api.add_resource(Transaction,"/transaction/<string:Date>")
app.run(debug=True) 