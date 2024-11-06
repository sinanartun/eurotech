import json
import boto3
import pymysql
import os
import csv

def lambda_handler(event, context):
    # S3'ten CSV dosyasını indirme
    s3_client = boto3.client('s3')
    bucket_name = 'estate-data-bucket'
    file_name = 'Housing.csv'
    local_path = '/tmp/' + file_name
    s3_client.download_file(bucket_name, file_name, local_path)

    # Veritabanı bağlantısı
    connection = pymysql.connect(host=os.environ['DB_HOST'],
                                 user=os.environ['DB_USER'],
                                 password=os.environ['DB_PASSWORD'],
                                 db=os.environ['DB_NAME'],
                                 port=int(os.environ['DB_PORT']),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # CSV dosyasını aç ve her bir satırı oku
            with open(local_path, mode='r', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)  # Başlık satırını atla
                for row in reader:
                    if len(row) == 13:  # Eğer beklenen sütun sayısı 13 ise
                        sql = """
                        INSERT INTO properties (price, area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                                                hotwaterheating, airconditioning, parking, prefarea, furnishingstatus)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(sql, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))
            connection.commit()
        return {
            'statusCode': 200,
            'body': json.dumps("Data processed successfully")
        }
    finally:
        connection.close()
