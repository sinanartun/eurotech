import streamlit as st
from textblob import TextBlob
import mysql.connector
import os

# Veritabanı bağlantısı için gerekli bilgiler
DATABASE_HOST = os.getenv('DATABASE_HOST', 'database-1.cn2g4202a6sb.eu-central-1.rds.amazonaws.com')
DATABASE_USER = os.getenv('DATABASE_USER', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'haydegudelum6-')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'yorumlar')

# Veritabanı bağlantısı oluştur
try:
    connection = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    st.write("Veritabanına bağlantı başarılı!")
except mysql.connector.Error as err:
    st.write(f"Veritabanı bağlantısında hata: {err}")
    connection = None

# Streamlit Arayüz Başlığı
st.title("Amazon Ürün Yorum Analizi")
st.write("Ürüne dair düşüncelerinizi bizimle paylaşın!")

# Kullanıcıdan yorum alıyoruz
user_comment = st.text_area("Yorumunuzu buraya yazın:")

# Gönder butonuna tıklandığında yorum analizi yapılıyor
if st.button("Gönder"):
    if user_comment:
        # Yorumun duygu analizini yapıyoruz
        analysis = TextBlob(user_comment)
        polarity = analysis.sentiment.polarity

        # Yorumun pozitif mi, negatif mi, yoksa nötr mü olduğunu belirliyoruz
        if polarity > 0:
            sentiment = "mutlu"
        elif polarity < 0:
            sentiment = "memnun değil"
        else:
            sentiment = "nötr"

        # Kullanıcıya sonucu gösteriyoruz
        st.write(f"Yorumunuzun duygu analizi sonucu: {sentiment}")

        # Veritabanına kaydetme (sadece nötr ve olumsuz yorumlar)
        if sentiment in ["memnun değil", "nötr"] and connection is not None:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO comments (comment, sentiment) VALUES (%s, %s)"
                cursor.execute(insert_query, (user_comment, sentiment))
                connection.commit()
                st.write("Yorumunuz veritabanına kaydedildi.")
            except mysql.connector.Error as err:
                st.write(f"Veritabanına kaydetme sırasında bir hata oluştu: {err}")
            finally:
                cursor.close()
    else:
        st.write("Lütfen bir yorum yazın.")

# Bağlantıyı kapatma
if connection is not None:
    connection.close()
