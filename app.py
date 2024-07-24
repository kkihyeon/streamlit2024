import streamlit as st
import random 

def show() :
    st.header('주사위 게임', divider='rainbow')
    clicked = st.button('주사위던지기', type='primary')
    clear = st.button('주사위지우기')
    if clicked :
        n = random.randint(1, 6)
        st.image(f'./img/{n}.png')
    if clear:
        del st.image()

show()