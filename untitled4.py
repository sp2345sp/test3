# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:43:39 2022

@author: SHIVANG
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


st.title('DreamHomes.com')
