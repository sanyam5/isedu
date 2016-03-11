from sklearn import metrics
from sklearn import svm
from sklearn.externals import joblib
import Utilities


def learn_svm(X, y, filename="learnt"):
    clf = svm.SVC(kernel='rbf', verbose=False)
    Utilities.logger.debug('Learning Model ' + filename)
    clf.fit(X, y)
    Utilities.logger.debug('Learnt Model')
    joblib.dump(clf, "models/" + filename + '.pkl')
    Utilities.logger.debug('Saved Model')


def load_svm(filename="learnt"):
    Utilities.logger.debug('Loading Model ' + filename)
    loaded = joblib.load("models/" + filename + '.pkl')
    Utilities.logger.debug('Loaded Model')
    return loaded

def test_svm_accuracy(X,y, filename="learnt"):
    model = load_svm(filename)
    results = model.predict(X)
    return metrics.accuracy_score(y,results)
