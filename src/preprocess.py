import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path):
    df = pd.read_csv(file_path)
    # Sadece gerekli kolonları seçerek basitleştirme
    selected_columns = ["TransactionAmount", "CustomerAge", "TransactionDuration", "LoginAttempts", "AccountBalance"]
    df = df[selected_columns]
    # Hedef sütunu oluştur: Hedef olarak TransactionAmount'ın belirli bir eşikten büyük olup olmadığını kullanacağız
    df['HighTransaction'] = (df['TransactionAmount'] > 1000).astype(int)
    return df


def preprocess_data(df):
    # Gerekli ön işlem adımları (eksik verilerin temizlenmesi, dönüşümler vs)
    df.dropna(inplace=True)  # Eksik verileri kaldır
    return df


def split_data(df):
    X = df.drop("HighTransaction", axis=1)
    y = df["HighTransaction"]
    return train_test_split(X, y, test_size=0.3, random_state=42)  # Test setini %30 olarak artırarak overfitting'i azaltmaya çalışıyoruz
