import streamlit as st
import plost

plost.bar_chart(
    data=datasets,
    bar='date',
    value=['sys', 'dias'],
    group=True)
