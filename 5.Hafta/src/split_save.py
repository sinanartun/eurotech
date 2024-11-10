import pandas as pd
from sklearn.model_selection import train_test_split

def split_and_save_data(file_path):
    # Veriyi yükle
    df = pd.read_csv(file_path)
    
    # Veriyi %70 eğitim, %30 test olacak şekilde ayır
    train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
    
    # Eğitim ve test verilerini aynı dizine kaydet
    train_path = file_path.replace('.csv', '_train.csv')
    test_path = file_path.replace('.csv', '_test.csv')
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Eğitim verisi kaydedildi: {train_path}")
    print(f"Test verisi kaydedildi: {test_path}")