from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# you have divide your model into learning as well as test stuff

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
iris.data
