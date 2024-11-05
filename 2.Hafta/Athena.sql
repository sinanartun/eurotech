CREATE EXTERNAL TABLE IF NOT EXISTS customer_data (
    CustomerID int,
    Genre string,
    Age int,
    `Annual_Income_(k$)` int,
    `Spending_Score` int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://my-aws-bucket/'
TBLPROPERTIES ('skip.header.line.count'='1');
