from src.preprocess import load_data, preprocess_data, split_data
from src.split_save import split_and_save_data
from src.dynamic_weight import dynamic_class_weight_training


def main():
    # Veri Yükleme
    data_path = (r"bank_transactions_data_2.csv")
    
    # Veriyi Ayırma ve Kayıt Etme
    split_and_save_data(data_path)

    # Eğitim verisini yükle
    train_data_path = data_path.replace('.csv', '_train.csv')
    df = load_data(train_data_path)

    # Veri Ön İşleme
    df = preprocess_data(df)

    # Veri Ayırma
    X_train, X_test, y_train, y_test = split_data(df)

    # Dinamik Class Weight ile Model Eğitimi
    best_model = dynamic_class_weight_training(X_train, y_train, X_test, y_test)
    print("En iyi model eğitildi ve seçildi.")


if __name__ == "__main__":
    main()