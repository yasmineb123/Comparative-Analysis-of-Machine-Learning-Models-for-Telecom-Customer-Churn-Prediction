import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre
st.title("📊 Mon Dashboard Streamlit")

# Charger les données
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Afficher les données
st.subheader("Aperçu des données")
st.write(df)

# KPI simple
st.metric("Total des ventes", df["Sales"].sum())

# Graphique
st.subheader("Comparative Analysis of Machine Learning Models for Telecom Customer Churn Prediction")
fig, ax = plt.subplots()
df.groupby("Category")["Sales"].sum().plot(kind="bar", ax=ax)
st.pyplot(fig)
