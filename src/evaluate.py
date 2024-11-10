import h2o
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, X_test, y_test):
    # Test verilerini H2OFrame'e dönüştür
    test_data = h2o.H2OFrame(pd.concat([X_test, y_test], axis=1))
    test_data[y_test.name] = test_data[y_test.name].asfactor()

    # Modeli test verileri üzerinde değerlendirin
    performance = model.leader.model_performance(test_data)
    print(performance)

    # Test verisi üzerindeki tahminler
    predictions = model.leader.predict(test_data).as_data_frame()
    print(predictions)

    # Tahminlerin değerlendirilmesi
    y_pred = predictions['predict'].astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    print("Accuracy Score:", accuracy)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return accuracy, report