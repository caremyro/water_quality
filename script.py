import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/water_potability.csv')

#print(df.isnull().sum() / len(df) * 100)


#ph                 14.987790
#Hardness            0.000000
#Solids              0.000000
#Chloramines         0.000000
#Sulfate            23.840049
#Conductivity        0.000000
#Organic_carbon      0.000000
#Trihalomethanes     4.945055
#Turbidity           0.000000
#Potability          0.000000

## Preprocessing

X = df.drop('Potability', axis=1)
y = df['Potability']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ph_median = X_train['ph'].median()
sulfate_median = X_train['Sulfate'].median()
trih_median = X_train['Trihalomethanes'].median()

X_train['ph'] = X_train['ph'].fillna(ph_median)
X_train['Sulfate'] = X_train['Sulfate'].fillna(sulfate_median)
X_train['Trihalomethanes'] = X_train['Trihalomethanes'].fillna(trih_median)

X_test['ph'] = X_test['ph'].fillna(ph_median)
X_test['Sulfate'] = X_test['Sulfate'].fillna(sulfate_median)
X_test['Trihalomethanes'] = X_test['Trihalomethanes'].fillna(trih_median)