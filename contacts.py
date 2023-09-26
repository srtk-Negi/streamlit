import streamlit as st
import pandas as pd


def app():
    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
    st.dataframe(df.style.highlight_max(axis=0))


if __name__ == "__main__":
    app()
