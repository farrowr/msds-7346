//console.log('Hello, World');

const app = document.getElementById('root');	
const container = document.createElement('div');
container.setAttribute('class','container');
app.appendChild(container);

const report = document.createElement('table');
report.setAttribute('class','report');
// create a request variable and assign http request object


var request = new XMLHttpRequest();
// open a new connection using GET request on the URL endpoint (API)
var date = localStorage.getItem('expenseReportDateKey');
if(date == null || date == ''){

} else {
	request.open('GET','http://127.0.0.1:5000/transaction/' + date,true);
	request.send();	
	//console.log(this.response)
}
request.onload = function(){
	//alert(localStorage.getItem('expenseReportDateKey'))
	if(localStorage.getItem('expenseReportDateKey') != null && localStorage.getItem('expenseReportDateKey') != ''){
		document.getElementById("date").value = localStorage.getItem('expenseReportDateKey');
	} else {
		document.getElementById("date").value = 'mm/dd/yy';
	}
	//console.log(this.response);
	//accessing JSON here
	if(this.response == null){
		exit();
	}

	const header = document.createElement('tr');
	const header_transactiondate = document.createElement('th');
	header_transactiondate.textContent = 'Employee';
	const header_employee = document.createElement('th');
	header_employee.textContent = 'Employee';
	const header_expensetype = document.createElement('th');
	header_expensetype.textContent = 'Expense Type';
	const header_expenseamt = document.createElement('th');
	header_expenseamt.textContent = 'Expense Amount';
	const header_fraudtransflag = document.createElement('th');
	header_fraudtransflag.textContent = 'Fraudulent Transaction Flag';

	header.appendChild(header_transactiondate)
	header.appendChild(header_employee);
	header.appendChild(header_expensetype);
	header.appendChild(header_expenseamt);
	header.appendChild(header_fraudtransflag);
	report.appendChild(header);

	var data = JSON.parse(this.response);

	data.forEach(transaction =>{
		//console.log(transaction.Employee)
		
		const record = document.createElement('tr');
		record.setAttribute('class','record');
		
		const transaction_date = document.createElement('td');
		transaction_date.textContent = transaction['Transaction Date'];
		const employee = document.createElement('td');
		employee.textContent = transaction.Employee;
		const expense_type = document.createElement('td');
		expense_type.textContent = transaction['Expense Type'];
		const expense_amt = document.createElement('td');
		expense_amt.textContent = transaction['Expense Amount'];
		expense_amt.setAttribute('style','text-align: center;');
		const fraud_trans_flag = document.createElement('td');
		fraud_trans_flag.textContent = transaction.Fraud_Trans_Flag;
		
 	 	record.appendChild(transaction_date);
 	 	record.appendChild(employee);
 	 	record.appendChild(expense_type);
 	 	record.appendChild(expense_amt);
 	 	record.appendChild(fraud_trans_flag);

 	 	report.appendChild(record);
	});

	container.appendChild(report);
	document.getElementById("date").focus();
}

function myFunction() {
    
 	var date = document.getElementById("date").value;
 	date = date.replace('/','-')
 	localStorage.setItem("expenseReportDateKey", date);
 	location.reload()

 	//request.onload();
 	//request.open('GET','http://127.0.0.1:5000/transaction/' + date,true);
	//request.send();	
	//console.log(this.response)
}

