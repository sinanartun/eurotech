import h2o
from h2o.automl import H2OAutoML
import pandas as pd
import pickle


def train_model(X_train, y_train, balance_classes=True, class_sampling_factors=None):
    # H2O sunucusunu başlat
    h2o.init()

    # Eğitim verilerini H2OFrame'e dönüştür
    train_data = h2o.H2OFrame(pd.concat([X_train, y_train], axis=1))
    train_data[y_train.name] = train_data[y_train.name].asfactor()  # Hedef sütunu kategorik yap

    # AutoML modelini tanımla ve eğit (aşırı öğrenmeyi engellemek için model karmaşıklığını ve eğitim süresini sınırlayalım)
    aml = H2OAutoML(max_runtime_secs=180, seed=42, stopping_metric='logloss', stopping_rounds=5, max_models=5, balance_classes=balance_classes, class_sampling_factors=class_sampling_factors)
    aml.train(y=y_train.name, training_frame=train_data)

    return aml

def save_model(model, model_path):
    model_path = h2o.save_model(model=model.leader, path=model_path, force=True)
    print(f"Model saved to {model_path}")