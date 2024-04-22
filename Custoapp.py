import streamlit as st
import pandas as pd


us = st.file_uploader('Selecione o arquivo',type='csv')
temp = st.file_uploader('Selecione o arquivo tempero', type='csv')


if temp is not None:
    #df = pd.read_csv(us, header=None,names=['Produto','Quantidade','Valor KG','Custo unitario'])
    tempero = pd.read_csv(temp, header=None, names=['Tipo','Quantidade','Custo KG','Valor gasto','Custo unitario'], sep=(';'))

    dd = round(tempero['Custo unitario'].sum(),2)
    col1, col2 = st.columns(2)
    name = st.sidebar.selectbox('Selecione o tipo:',
                                  options=sorted(tempero['Tipo'].unique()),                                  
                                   placeholder = 'Selecione o arquivo')
    
    df_selec = tempero.query(
        'Tipo == @name'
        )
    df_selec.squeeze()
    
    prod = df_selec['Tipo'].squeeze()
    col1, col2, col3 = st.columns(3)
    val = round(df_selec['Custo KG'],2).squeeze()
    unit = round(df_selec['Custo unitario'],2).squeeze()

    with col1: 
        st.subheader(f'Produto: :orange[{prod}]') 
    with col2:
        st.subheader(f'Preço: :green[R${val}]')
    with col3:
        st.subheader(f'Preço unitário: :green[R${unit}]')


    inf, markup = st.tabs(['Informação','MARK-UP'])

    with inf:
        st.header(prod)

    with markup:
        
        mk = round(9.03/((100-22.41-15.82-15)/100),2)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f'Mark-up: :green[R${mk}]') 
        with col2:
            st.subheader(f'Variável tempero: :green[R$ {dd}]') 
             