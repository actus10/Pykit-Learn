from pk.models import *
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.mixture import GMM
from nose.tools import raises

def test_alg_creation():
    alg = Algorithm(DecisionTreeClassifier())
    assert alg.clf_name == 'DecisionTreeClassifier'

def test_fit_supervised_algorithm_with_dt():
    iris = load_iris()
    X, y = iris.data, iris.target

    alg = SupervisedAlgorithm(DecisionTreeClassifier())
    assert alg.fitted == False
    assert alg.params['tree_'] is None

    alg.fit(X,y)
    assert alg.fitted == True
    assert alg.params['tree_'] is not None

@raises(Exception)
def test_predict_untrained():
    alg = UnsupervisedAlgorithm(GMM())
    alg.predict([0])


