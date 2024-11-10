from src.model import train_model, save_model
from src.evaluate import evaluate_model
import numpy as np
import os


def dynamic_class_weight_training(X_train, y_train, X_test, y_test, results_path="results.txt", models_dir="models"):
    # Model dosyalarının kaydedileceği klasörü oluştur
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    best_model = None
    best_f1_score = 0
    acceptable_f1_range = (0.75, 0.85)  # Uygun gördüğümüz f1-score aralığı
    class_weights = np.linspace(0.5, 5.0, 10)  # 0.5 ile 5.0 arasında 10 farklı class weight faktörü denenecek
    attempts = 0  # Eğitim deneme sayısı

    for weight in class_weights:
        print(f"Class weight faktörü: {weight}")
        model = train_model(X_train, y_train, balance_classes=True, class_sampling_factors=[1.0, weight])
        accuracy, report = evaluate_model(model, X_test, y_test)

        f1_score_1 = report['1']['f1-score']  # Sınıf 1 için f1-score
        print(f"Sınıf 1 için F1-Score: {f1_score_1}")

        # Save the model in pickle format
        model_path = os.path.join(models_dir, f"model_weight_{weight:.2f}.pkl")
        save_model(model, model_path)
        print(f"Model kaydedildi: {model_path}")

        # Sonuçları dosyaya yaz
        with open(results_path, "a") as file:
            file.write(f"Class weight: {weight} # Accuracy: {accuracy} # F1-Score (Class 1): {f1_score_1} # Model Path: {model_path}\n")

        # Eğer f1-score uygun aralıkta ise dur
        if acceptable_f1_range[0] <= f1_score_1 <= acceptable_f1_range[1]:
            print(f"Uygun F1-Score elde edildi: {f1_score_1}, Class weight faktörü: {weight}")
            best_model = model
            break

        # Daha iyi bir f1-score elde edilirse en iyi modeli güncelle
        if f1_score_1 > best_f1_score:
            best_f1_score = f1_score_1
            best_model = model

        attempts += 1
        # Eğer 5 denemeden sonra istenilen sonuca ulaşılamadıysa, döngüğyü durdur ve farklı yaklaşımlar dene
        if attempts >= 5:
            print("5 deneme yapıldı, uygun sonuç elde edilemedi. Farklı class weight faktörleri deneniyor.")
            class_weights = np.linspace(5.5, 10.0, 5)  # Yeni bir class weight aralığı denenecek
            attempts = 0  # Deneme sayısını sıfırla

    return best_model