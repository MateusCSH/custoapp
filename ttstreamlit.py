import streamlit as st 
import pandas as pd 
import pyautogui as py
import time


st.set_page_config(
                   page_title='Bora',
                   layout='wide')

py2 = st.file_uploader('Select seu arquivo',type='csv')

if py2 is not None:
    but = st.button('Click',type='primary')

    if but:
        py.PAUSE = 2
        py.press('win')
        py.write('chrome')
        py.press('enter')

    else:
      st.info('Erro')
 

        
        
