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

        btn_op = py.locateCenterOnScreen('btndrive.png')
        py.click(btn_op.x, btn_op.y)
        time.sleep(2)
        click_icon_drive = py.locateCenterOnScreen('click_driv.png')
        py.click(click_icon_drive.x, click_icon_drive.y)
        

        clica_ale = py.locateCenterOnScreen('clickale.png')
        py.moveTo(clica_ale.x, clica_ale.y)
        py.click(clica_ale.x,clica_ale.y)

        py.press('tab')
        py.press('tab')

        py.write('Lista 2 - ENG ECO')
        py.press('down')
        py.press('down')
        py.press('enter')

        time.sleep(2.5)


        mes = py.locateCenterOnScreen('proc_MS.png')
        py.click(mes.x, mes.y)

        proc_nome = py.locateCenterOnScreen('proc_nome.png')
        py.click(proc_nome.x, proc_nome.y)

        py.press('down')

        df = pd.read_csv(py2,header=None, names=['Tipo','Quantidade','Custo KG','Valor gasto','Custo unitario'], sep=(';'))

        for lin in df.index:
            prod = df.loc[lin,'Tipo']
            py.write(prod)
            py.press('down')

        py.click(proc_nome.x, proc_nome.y)
        py.press('down')
        py.press('tab')
        
        for lin in df.index:
            cust = round(df.loc[lin,'Custo unitario'],2)
            py.write(cust)
            py.press('down')

        
        
