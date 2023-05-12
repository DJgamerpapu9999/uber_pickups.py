import streamlit as st
import pandas as pd
import numpy as np

st.title('Proyecto multigrado')

st.subheader("Bienvenido a nuestro proyecto, te recordamos que :blue[no somos profesionales], porfavor consulta un medico especializado.")
st.subheader("Porfavor ingrese :green[1] si es :green[verdadero] o :red[0] si es :red[falso].")
contador=0
edad = st.slider('Introduce tu edad:', 0, 100, 0)
st.write("Tu edad es de: ", edad, 'años.')
edad=int(edad)
if edad<=25:
    contador+=1


st.subheader("Drogas")
with st.expander("------"):
    a=st.caption("¿Consumes drogas?: ")
    if st.button('Si'):
        contador=contador+1
        a=st.caption("¿Has consumido más de una vez? ")
        if st.button(' Si'):
            contador=contador+1
            a=st.caption("¿Consumes más de una vez al mes? ")
            if st.button('Si '):
                contador=contador+1
    a=st.caption("¿Consumes alucinógenos? ")
    if st.button('Si  '):
        contador=contador+1
        a=st.caption("¿Has consumido más de una vez? ")
        if st.button('  Si'):
            contador=contador+1
            a=st.caption("¿Consumes más de una vez al mes? ")
            if st.button('  Si'):
                contador=contador+1
    a=st.caption("¿Consumes alcohol o otras drogas de efecto retardante?")
    if st.button('  Si '):
        contador=contador+1
        a=st.caption("¿Consumes frecuentemente? ")
        if st.button('  Si  '):
            contador=contador+1


st.subheader("Enfermedades")
with st.expander("-----"):
    options = st.multiselect(
    'Selecciones si alguien en su familia presenta alguna de estas enfermedades',
    ['Alucinaciones', 'Locura', 'Alzheimer', 'Esquizofrenia'],['Alzheimer'])


if options==0:
    st.caption(contador)
else:
    contador+=1


if contador>22:
    st.subheader("error")
elif contador>=15:
    st.subheader("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
elif contador>=10:
    st.subheader("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
elif contador>=5:
    st.subheader("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
else:
    st.subheader("Ten cuidado, es probable que a largo plazo tengas un problema mental.")

st.caption(contador)
if st.button(' Fin '):
    st.caption("----------")