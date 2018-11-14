console.log('Hello, World');

const app = document.getElementById('root');
	
const container = document.createElement('div');
container.setAttribute('class','container');
app.appendChild(container);

const report = document.createElement('table');
report.setAttribute('class','report');

// create a request variable and assign http request object
var request = new XMLHttpRequest();

// open a new connection using GET request on the URL endpoint (API)
request.open('GET','http://127.0.0.1:5000/transaction/1-16-17',true);

request.onload = function(){

	//console.log('in onload');
	//accessing JSON here
	
	const header = document.createElement('tr');
	const header_employee = document.createElement('th');
	header_employee.textContent = 'Employee';
	const header_expensetype = document.createElement('th');
	header_expensetype.textContent = 'Expense Type';
	const header_expenseamt = document.createElement('th');
	header_expenseamt.textContent = 'Expense Amount';
	const header_fraudtransflag = document.createElement('th');
	header_fraudtransflag.textContent = 'Fraudulent Transaction Flag';


	header.appendChild(header_employee);
	header.appendChild(header_expensetype);
	header.appendChild(header_expenseamt);
	header.appendChild(header_fraudtransflag);
	report.appendChild(header);

	var data = JSON.parse(this.response);
	data.forEach(transaction =>{
		console.log(transaction.Employee)
		
		const record = document.createElement('tr');
		record.setAttribute('class','record');
		

		const employee = document.createElement('td');
		employee.textContent = transaction.Employee;
		const expense_type = document.createElement('td');
		expense_type.textContent = transaction['Expense Type'];
		const expense_amt = document.createElement('td');
		expense_amt.textContent = transaction['Expense Amount'];
		const fraud_trans_flag = document.createElement('td');
		fraud_trans_flag.textContent = transaction.Fraud_Trans_Flag;
		
 	 	record.appendChild(employee);
 	 	record.appendChild(expense_type);
 	 	record.appendChild(expense_amt);
 	 	record.appendChild(fraud_trans_flag);

 	 	report.appendChild(record);
	});

	container.appendChild(report);
}

request.send();
