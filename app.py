import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

model = pickle.load(open('model/extra_tree_classifier.pkl', 'rb'))


def predict_input(parent_protein_id, protein_seq, start_position, end_position, peptide_seq, chou_fasman, emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability):

    array = np.array([[parent_protein_id, protein_seq, start_position, end_position, peptide_seq, chou_fasman,
                       emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability]])
    array = pd.DataFrame(array)
    array[0] = array[0].astype('category').cat.codes
    array[1] = array[1].astype('category').cat.codes
    array[4] = array[4].astype('category').cat.codes

    minmax_scaler = MinMaxScaler()
    input = minmax_scaler.fit_transform((array))
    # prediction = model.predict_proba(input)
    prediction = model.predict(input)
    # print(prediction)
    return int(prediction)


def main():
    html_temp = """
    <div style="padding:10px;">
        <h2>COVID-19/SARS B-cell Epitope Prediction</h2>
        <h3>Mission: Predictable A Virtual Machine Learning Hackathon to Battle Covid-19</h3>
        <h3>A simple web app for epitope prediction used in vaccine development</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image("./data/covid.jpg", caption="Coronavirus image",
             use_column_width=True)

    st.sidebar.subheader("Enter the values")

    protein_id = st.sidebar.text_input("Enter the Protein ID:")

    protein_seq = st.sidebar.text_input("Enter the Protein Sequence:")

    start_position = st.sidebar.slider(
        "Enter the start position:", min_value=1, max_value=3079, value=1, step=1)

    end_position = st.sidebar.slider(
        "Enter the end position:", min_value=6, max_value=3086, value=6, step=1)

    peptide_seq = st.sidebar.text_input("Enter the peptide sequence:")

    chou_fasman = st.sidebar.number_input("Enter the chou fasman value:",
                                          min_value=0.000, max_value=2.000, value=0.500)

    emini = st.sidebar.number_input(
        "Enter the emini value:", min_value=0.0, max_value=27.189)

    kolaskar_tongaonkar = st.sidebar.number_input(
        "Enter the Kolaskar Tongaonkar value:", min_value=0.500, max_value=1.300)

    parker = st.sidebar.number_input(
        "Enter the parker value:", min_value=-10.000, max_value=10.000)

    isoelectric_point = st.sidebar.number_input(
        "Enter the isoelectric point value:", min_value=3.00, max_value=13.00)

    aromaticity = st.sidebar.number_input(
        "Enter the aromaticity value:", min_value=0.00, max_value=0.1000)

    hydrophobicity = st.sidebar.number_input(
        "Enter the hydrophobicity value:", min_value=-2.000, max_value=1.3000)

    stability = st.sidebar.number_input(
        "Enter the stability value:", min_value=5.00, max_value=138.000)

    safe_html = """
        <div style="background-color:#F4D03F;padding:10px;">
            <h2 style="color:white;text-align:center;">You are safe!!</h2>
        </div>
    """

    danger_html = """
        <div style="background-color:#F08080;padding:10px">
            <h2 style="color:black;text-align:center;">You might be in danger!!</h2>
        </div>
    """

    if st.sidebar.button("predict"):
        output = predict_input(protein_id, protein_seq, start_position, end_position, peptide_seq, chou_fasman,
                               emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability)
        st.success(f"The predicted class is {output}")

        if output == 1:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
