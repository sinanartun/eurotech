import pickle
import boto3
import json

# S3'ten model dosyasını indirme
s3 = boto3.client('s3')
bucket_name = 'my-aws-bucket'
model_key = 'logistic_regression_model.pkl'

# Modeli yerel dosyaya kaydetme
s3.download_file(bucket_name, model_key, 'model.pkl')

# Modeli yükleme
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Canlı veriler
live_data = {'age': 30, 'gender_male': 1}

# Veriyi uygun formata dönüştürme
features = [live_data['age'], live_data['gender_male']]

# Tahmin etme (prediksiyon)
result = model.predict([features])

# Tahmin sonucunu ekrana yazdırma
print(result)
