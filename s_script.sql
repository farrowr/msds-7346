
DROP DATABASE IF EXISTS reports;
CREATE DATABASE reports;



SET SQL_SAFE_UPDATES = 0;
-- show variables like '%INFILE%';
-- SET GLOBAL local_infile = 1;
-- SHOW VARIABLES WHERE Variable_name = 'hostname';
-- SHOW VARIABLES WHERE Variable_name = 'port';

use reports;

DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions ( 
transaction_id int,
Employee varchar(50),
`Name on Card` varchar(50),
`Region Code` varchar(3),
`Allocated Business Unit Code` int,
`Allocated Business Unit Name` varchar(50),
`Allocated Team Name` varchar(50),
`Allocated Team` int,
`Allocated Sub-Team Name` varchar(50),
`Allocated Sub-Team` int,
`Report Name` varchar(50),
`Paid Date` varchar(50),
`Approval Status` varchar(50),
`Payment Status` varchar(50),
`Expense Type` varchar(50),
`Transaction Date` varchar(50),
`Vendor` varchar(50), 
`Payment Type` varchar(50),
`Expense Amount` varchar(50),
`Reimbursement Currency` varchar(3),
fraud_trans_flag varchar(100)
);
LOAD DATA LOCAL INFILE '/Users/rfarrow/Documents/Personal/MS SMU/MSDS 7346 Cloud Computing/Project/outfile.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

select * from transactions;
-- order by transaction_id asc;

-- DROP TABLE IF EXISTS test;
-- CREATE TABLE test ( 
-- column_a varchar(10),
-- column_b varchar(10),
-- column_c varchar(10)
-- );
-- select * from test;

