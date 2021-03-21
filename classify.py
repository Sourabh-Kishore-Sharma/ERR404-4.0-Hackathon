#!/usr/bin/env python3

import pandas as pd
import re

df = pd.read_csv("Yes Bank Account Statement _new.csv")
description = df["Description "]

regex = ["zomato","swiggy",
         "amazon","google",
         "ola","uber",
         "jio","prepaid",
         "bookmyshow","tunes"
         ]

df["Payment Area"] = None

for i,des in enumerate(df["Description "]):
    for pattern in regex:
        if bool(re.search(pattern,des,re.IGNORECASE)):
            df.at[i,"Payment Area"] = pattern

df["Payment Type"] = None

for i,des in enumerate(df["Description "]):
    type = des[0:3]
    df.at[i,"Payment Type"] = type



print(df["Payment Area"])
print(df["Payment Type"])


#print(len(Payment_Area))
#df["Payment Area"] = Payment_Area

#print(df[["Description ","Payment Area"]])
