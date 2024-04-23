import streamlit as st 
import pandas as pd 
import pyautogui as py
import time


st.set_page_config(
                   page_title='AUTOMATION_CEM',
                   layout='wide')

py2 = st.file_uploader('Select seu arquivo',type='csv')
''
if py2 is not None:
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        but_M4S3 = st.button('M4S3',type='primary')

    with col2:
        but_M4S4 = st.button('M4S4',type='primary')

    if but_M4S3:
        py.PAUSE = 2
        py.press('win')
        py.write('chrome')
        py.press('enter')

        btn_op = py.locateCenterOnScreen('btndrive.png')
        py.click(btn_op.x, btn_op.y)
        time.sleep(2)
        click_icon_drive = py.locateCenterOnScreen('click_driv.png')
        py.click(click_icon_drive.x, click_icon_drive.y)
        
        time.sleep(2)
        clica_ale = py.locateCenterOnScreen('clickale.png')
        py.moveTo(clica_ale.x, clica_ale.y)
        py.click(clica_ale.x,clica_ale.y)
        
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

        py.PAUSE = 0.5

        df = pd.read_csv(py2,header=None, names=['Nome','Horas','Motivo'], sep=(','))
        # Transforma número para string.    
        df['Horas'] = df['Horas'].astype(str)

        for lin in df.index:
            name = df.loc[lin,'Nome']
            py.write(name)
            py.press('down')

        py.click(proc_nome.x, proc_nome.y)
        py.press('down')
        py.press('tab')
        
        for lin in df.index:
            horas = df.loc[lin,'Horas']
            py.write(horas)
            py.press('down')


        py.click(proc_nome.x, proc_nome.y)
        py.press('down')
        py.press('tab')
        py.press('tab')

        for lin in df.index:
            motivo = df.loc[lin,'Motivo']
            py.write(motivo)
            py.press('down')


    if but_M4S4:
        
        py.press('win')
        py.write('chrome')         
             
