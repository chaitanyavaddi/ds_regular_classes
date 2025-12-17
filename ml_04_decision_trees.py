- What is a Decision Tree?
- A Decision Tree is a supervised machine learning algorithm
that makes predictions by repeatedly splitting data into branches
based on feature conditions, similar to human decision making. 

-- This is like a flowchart that asks questions and makes decisions. 

Why?
- Humans naturally think in rules:
  - If income > X, approve loan
  - If temp > Y, turn on AC
- Decision Trees copy this thinking

  Eg.1 Medical Diagnosis
  - Is fever > 101?
  - Is could present?
  - Is oxygen level < 94%?
  Output: Disease present or not

  Eg. 2: Online Shopping
  - Is user a returning customer?
  - Cart value > Rs.2000?
  - Past purchase frequency?
  Output: Show discount or not

- Structure of a Decision Tree

  Component     Meaning
Root Node       First question
Decision Tree   A condition
Branch          Outcome of condition
Leaf Node       Final prediction
Depth           Levels of tree


How? (How a Decision Tree Learns)
- The tree tries to:
  - Split data so that each group becomes more pure
  - Meaning: mostly one class

It uses metrics like:
  - Gini Impurity
  - Entropy (Information Gain)

This is more Intuition. You dont need heavy math. 

1. Classification Tree (Spam outcome, etc.. )
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
X = df[['Pclass','Age', 'Fare']] #Input / feature
Y = df['Survived'] #Output / label
X = X.fillna(X.median())
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, Y_train)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=X.columns, class_names=["No", "yes"], filled=True)
plt.show()

2. Regression Tree (House price, tip prediction etc..)
# Predict Tip Amount
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv")
X = df[['total_bill', 'size']] #feature
Y = df['tip'] #label
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X, Y)
print(model.predict([[2, 2]]))

  max_depth - max levels of tree
  min_samples_split - Min samples to split
  min_samples_leaf - Min samples in leaf

  The above params will control overfitting
  
Adv.
- Easy to understand
- handles non-linear data
- Works with numeric + categorical data
- Highly interpretable

Dis.
- Overfitting
- Small changes in data -> big changes in tree

Code Eg.

Problem: Predict if a passenger survived




  


