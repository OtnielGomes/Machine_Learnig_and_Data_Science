import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from yellowbrick.classifier import ConfusionMatrix
### Pré_processamento ###
with open('census_data.pkl', mode='rb') as f:
    X_census_training, y_census_training,\
        X_census_test, y_census_test = pickle.load(f)

### Treinamento ###
arvore_census = DecisionTreeClassifier(criterion='entropy', random_state=0)
arvore_census.fit(X_census_training, y_census_training)

### Previsoes ###
prediction = arvore_census.predict(X_census_test)
accuracy_prediction = accuracy_score(y_census_test, prediction)

### Pós_processamento ###


def main():
    print(accuracy_prediction)
    print()
    cm = ConfusionMatrix(arvore_census)
    cm.fit(X_census_training, y_census_training)
    cm.score(X_census_test, y_census_test)
    cm.show()
    print(classification_report(y_census_test, prediction))


if __name__ == '__main__':
    main()


