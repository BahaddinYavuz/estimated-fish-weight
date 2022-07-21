import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor



def weight_estimate(Species, Length ,Height, Width):
    data = pd.read_csv("C:/Users/w10/flask_demo/Fish.csv")
    
    data["Length"] = (data["Length1"]+data["Length2"]+data["Length3"])/3
    data["Length"] = data["Length"].astype(int)
    data.drop(['Length1', 'Length2',"Length3"], axis=1, inplace=True)

    y = data["Weight"]
    x = data.drop(["Weight"],axis =1)
    
    finaldata = pd.get_dummies(x, columns=['Species'])
    
    NN = RandomForestRegressor(random_state = 0)
    NN.fit(finaldata , y)
    
    dict = {'Species': Species, 'Length': Length, 'Height': Height, "Width" : Width}

    df3 = x.append(dict, ignore_index = True)
    test = pd.get_dummies(df3, columns=['Species'])


    return NN.predict(test.tail(1))

"""print(weight_estimate("Bream", 29, 12.44, 5.13))"""
