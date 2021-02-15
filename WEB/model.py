import pandas as pd
import pickle
data=pd.read_csv("fbmodel_data.csv")
from fbprophet import Prophet
model=Prophet()
model.fit(data)
pickle.dump(model,open('model.pkl','wb'))