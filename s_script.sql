
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
-- transaction_id int,
employee varchar(50),
name_on_card varchar(50),
region_code varchar(3),
allocated_business_unit_code int,
allocated_business_unit_name varchar(50),
allocated_team_name varchar(50),
allocated_team int,
allocated_sub_team_name varchar(50),
allocated_sub_team int,
report_name varchar(50),
paid_date varchar(50),
approval_status varchar(50),
payment_status varchar(50),
expense_type varchar(50),
transaction_date varchar(50),
vendor varchar(50), 
payment_type varchar(50),
expense_amount varchar(50),
reimbursement_currency varchar(3),
fraud_trans_flag varchar(100)
);
-- LOAD DATA LOCAL INFILE '/Users/rfarrow/Documents/Personal/MS SMU/MSDS 7346 Cloud Computing/Project/outfile.csv'
-- INTO TABLE transactions
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"' 
-- LINES TERMINATED BY '\r\n'
-- IGNORE 1 LINES;

select count(*) from transactions;
-- order by transaction_id asc;

-- DROP TABLE IF EXISTS test;
-- CREATE TABLE test ( 
-- column_a varchar(10),
-- column_b varchar(10),
-- column_c varchar(10)
-- );
-- select * from test;

