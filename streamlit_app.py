import streamlit as st
import plost
import pandas as pd

datasets = [['Date','2022-09-30','2022/09/30','2022/09/30'],['sys',149,139,127],['dias',109,97,91]]
df = pd.DataFrame(data, columns=['Date', 'sys', 'dias])
df['Date']= pd.to_datetime(df['Date'])

plost.bar_chart(
    data=df,
    bar='date',
    value=['sys', 'dias'],
    group=True)
