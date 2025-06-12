import streamlit as st
import pandas as pd

# Load glossary Excel file
df = pd.read_excel("Glossary.xlsx")

# Page title
st.title("🌍 Environmental Glossary Term Explorer")
st.write("Bilingual glossary for environmental terms in English and German.")

# Language selection
language = st.radio("Choose input language / Sprache wählen:", ["English", "Deutsch"])

# Filter terms by language
if language == "English":
    terms = df['En_Term'].dropna().unique()
    en_terms = [" Type / Select the Term: "] + sorted(df['En_Term'].unique())
    selected_en_term = st.selectbox("English Term", en_terms, index=0)
    selected_term = selected_en_term
    match = df[df['En_Term'] == selected_term]
else:
    terms = df['DE_Term'].dropna().unique()
    de_terms = [" Tippen / Wählen Sie den Begriff: "] + sorted(df['DE_Term'].unique())
    selected_de_term = st.selectbox("Deutscher Begriff", de_terms, index=0)
    selected_term = selected_de_term
    match = df[df['DE_Term'] == selected_term]



# Show definitions and translations
if not match.empty:
    row = match.iloc[0]
    
    if language == "English":
        st.subheader("📖 Definition (English)")
        st.write(row['En_Definition'])
        
        st.subheader("📘 German Translation")
        st.write(f"**{row['DE_Term']}**")
        st.write(row['DE_Definition'])
        
    else:
        st.subheader("📖 Definition (Deutsch)")
        st.write(row['DE_Definition'])
        
        st.subheader("📘 Englische Übersetzung")
        st.write(f"**{row['En_Term']}**")
        st.write(row['En_Definition'])
    
    # Show source
    st.markdown(f"**🔗 Source:** {row['Source']}")
