import csv
import pandas
import numpy
import datetime

print("Starting application...")
start_time = datetime.datetime.now()

df = pandas.read_csv('Transaction List - Small.csv',sep=',',delimiter=None,header='infer')
bu = pandas.read_csv('Business Unit by Cardholder.csv',sep=',',delimiter=None,header='infer')


df["Fraud_Trans_Flag"] = None
validated_employees = []
same_name_employees = []

for index, row in df.iterrows():

	employee = row["Employee"]
	expense_amt = float(row['Expense Amount'].replace(',',''))
	allocated_bu = row["Allocated Business Unit Code"]
	date = row["Transaction Date"] #TODO: confirm column (transaction vs paid)
	vendor = row["Vendor"]
	print(employee)

#Payment Status should never be "Extracted to General Ledger" or "Processing Payment" unless Approval Status is "Approved"
	if not row["Approval Status"] == "Approved":
		if row["Payment Status"] == "Extracted to General Ledger" or row["Payment Status"] == "Processing Payment":
			df.ix[index,"Fraud_Trans_Flag"] = 'F - Illegal Operation'

#Expense charged outside of allocated business unit
	r = bu.loc[bu['Employee Name'] == employee]
	if not r.empty:
		if not r['Business Unit Code'].count() > 1: #TOOD: need to remove clause when employee id is provided; this checks to ensure that only one employee with name exists
			if (r['Business Unit Code']!=allocated_bu).bool() and expense_amt > 500: #previously used .any() due to multiple employee records with same name
				df.ix[index,"Fraud_Trans_Flag"] = 'F - External Business Unit'
		else:
			same_name_employees.append(employee) #to provide of employees that do not have unique names 
	else:
		df.ix[index,"Fraud_Trans_Flag"] = 'F - Employee Business Unit Not Found'

#Payments over $5000 should be flagged as needing a second approval (maybe there could be a second approval field added, and we could check if it was filled)
	if expense_amt >= 5000:
		df.ix[index,"Fraud_Trans_Flag"] = 'F - Over $5000 Limit'

#Two payments in one day to the same store by one person should be flagged for a double check 	
	if employee not in validated_employees:	
		validated_employees.append(employee)

		edf = df.loc[df["Employee"] == employee]
		for eix, er in edf.iterrows():
			if (date == er["Transaction Date"]) and (vendor == er["Vendor"]) and index != eix:
				df.ix[eix,"Fraud_Trans_Flag"] = 'F - Same Day Payment'

#exports list of employees that do not have unique names 
#mylist = same_name_employees
#file = open('mylist.csv','w')
#i = 0
#while (i<len(mylist)):   
#    file.write(str(mylist[i])+"\n")
#    i = i + 1
#file.close()

df.to_csv("outfile.csv")

end_time = datetime.datetime.now()
print("Ending application...")

elapsed_time = end_time - start_time
print("Total elapsed time: " + str(elapsed_time.seconds/60) + " (mins)")


#ofile = open('output.csv',"wb")
#writer = csv.writer(ofile,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)


#with open('Transaction List - Small.csv','rb') as ifile:
	#reader = csv.reader(ifile)
	#for row in reader:
		#writer.writerow(row)

#ifile.close()
#ofile.close()



