import sys
sys.path.append("scripts/")
from scripts.training.test import TestModel
from sklearn.metrics import classification_report

test = TestModel(model = "runs:/caa8665f134d489298fb359f0c33bf5e/model",
                 model_name="efficientnet",
                 batch_size=32,)

y_one_hot, predictions_int = test.test()
print("===========================================================")
print("==============Clasification Report - EfficientNet==========")
print("\n")
print(classification_report(y_one_hot, predictions_int))
print("\n")
print("===========================================================")


test = TestModel(model = "runs:/c90e8a06b2a14ec3ac67910a348fe628/model",
                 model_name="resnet",
                 batch_size=32,)

y_one_hot, predictions_int = test.test()
print("===========================================================")
print("==============Clasification Report - ResNet==========")
print("\n")
print(classification_report(y_one_hot, predictions_int))
print("\n")
print("===========================================================")

test = TestModel(model = "runs:/bee34101e19846f2a4c256bd09c3a83a/model",
                 model_name="mobilenet",
                 batch_size=32,)

y_one_hot, predictions_int = test.test()
print("===========================================================")
print("==============Clasification Report - MobileNet==========")
print("\n")
print(classification_report(y_one_hot, predictions_int))
print("\n")
print("===========================================================")
