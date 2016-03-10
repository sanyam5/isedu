import SVM
from Utilities import *
from sklearn.model_selection import KFold
import numpy as np

# Parameters
k = 10  # folds for cross validation
names = smart_dict()  # Dictionary for names of manual features, initialized by reflective

# Dataset
X_content = [[]]  # Content Features
X_manual = [[]]  # Manual Features
y = []  # Educativeness


# Task 1 uses content features to predict Educativeness
# Requires: X_content, y
def task_1_results():
    kf = KFold(n_folds=k)
    accuracies = []
    for train_index, test_index in kf.split(y):
        X_train = X_content[train_index]
        X_test = X_content[test_index]
        y_train = y[train_index]
        y_test = y[test_index]
        SVM.learn_svm(X_train, y_train, "task_1_model")
        accuracies.append(SVM.test_svm_accuracy(X_test, y_test, "task_1_model"))
    print "Accuracy for task_1:", np.mean(accuracies), "+-", np.std(accuracies)
    return accuracies


# Task 2 uses manual features to predict Educativeness
# Requires: X_manual, y
def task_2_results():
    kf = KFold(n_folds=k)
    accuracies = []
    for train_index, test_index in kf.split(y):
        X_train = X_manual[train_index]
        X_test = X_manual[test_index]
        y_train = y[train_index]
        y_test = y[test_index]
        SVM.learn_svm(X_train, y_train, "task_2_model")
        accuracies.append(SVM.test_svm_accuracy(X_test, y_test, "task_2_model"))
    print "Accuracy for task_2:", np.mean(accuracies), "+-", np.std(accuracies)
    return accuracies


# Task 3 uses content features to predict manual features
# Requires: X_content, X_manual
def task_3_results():
    kf = KFold(n_folds=k)
    num_manual_features = len(X_manual[0])
    accuracies = []
    for i in range(num_manual_features):
        accuracies.append([])
    X_manual_np = np.asarray(X_manual)
    for train_index, test_index in kf.split(X_content):
        X_train = X_content[train_index]
        X_test = X_content[test_index]
        for i in range(num_manual_features):
            y_train = X_manual_np[train_index, i]
            y_test = X_manual_np[test_index, i]
            SVM.learn_svm(X_train, list(y_train), "task_3_model")
            accuracies[i].append(SVM.test_svm_accuracy(X_test, list(y_test), "task_3_model"))

    for i in range(num_manual_features):
        print "Accuracy for task_3 (" + names[i] + "):", np.mean(accuracies[i]), "+-", np.std(accuracies[i])

    return accuracies

# Task 4 uses content features to predict manual features
# Requires: X_content, X_manual, y
def task_4_results():
    kf = KFold(n_folds=k)
    num_manual_features = len(X_manual[0])
    accuracies = []
    for i in range(num_manual_features):
        accuracies.append([])
    X_manual_np = np.asarray(X_manual)
    for train_index, test_index in kf.split(X_content):
        X_train = X_content[train_index]
        X_test = X_content[test_index]
        for i in range(num_manual_features):
            y_train = X_manual_np[train_index, i]
            y_test = X_manual_np[test_index, i]
            SVM.learn_svm(X_train, list(y_train), "task_4_model")
            accuracies[i].append(SVM.test_svm_accuracy(X_test, list(y_test), "task_4_model"))

    for i in range(num_manual_features):
        print "Accuracy for task_4 (" + names[i] + "):", np.mean(accuracies[i]), "+-", np.std(accuracies[i])

    return accuracies


# Custom code to initialize X and y
