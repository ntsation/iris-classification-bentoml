import joblib
from sklearn import datasets
from sklearn import svm

import bentoml

if __name__ == "__main__":
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    clf = svm.SVC()
    clf.fit(X, y)

    with bentoml.models.create("iris_sklearn") as bento_model:
        joblib.dump(clf, bento_model.path_of("model.pkl"))
    print(f"Model saved: {bento_model}")