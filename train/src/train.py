from sklearn.ensemble import GradientBoostingClassifier
from sklearn import datasets
from sklearn.externals import joblib

def main():
    clf = GradientBoostingClassifier()

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    clf.fit(X, y)

    joblib.dump(clf, 'model/iris.joblib')

if __name__ == '__main__':
    main()

