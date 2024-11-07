mkdir python

pip install pymysql -t python/

zip -r pymysql_layer.zip python/

aws s3 cp pymysql_layer.zip s3://estate-data-bucket
