import SVM_Tests
from Utilities import *

SVM_Tests.names = {0:"Relevance",1:"Classification_Example",2:"Classification_Definition",3:"Classification_Illustrations",4:"Classification_QA",5:"Classification_Other",6:"Source_ClassWebpage",7:"Source_Encyclopedia",8:"Source_Blog",9:"Source_Forums",10:"Source_Book",11:"Source_Presentation",12:"Source_Publication",13:"Source_HowTo",14:"Source_Manual",15:"Source_Other"}

# Custom code to initialize X and y
with open('X.json','r') as f:
    SVM_Tests.X_content = np.asarray(json.load(f))

with open('X_manual.json','r') as f:
    SVM_Tests.X_manual = np.asarray(json.load(f))

with open('y.json','r') as f:
    SVM_Tests.y = np.asarray(json.load(f))

# SVM_Tests.task_1_results()
SVM_Tests.task_2_results()
# SVM_Tests.task_3_results()
SVM_Tests.task_4_results()