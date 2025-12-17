import streamlit as st
import pandas as pd
from scoring import score_leads

st.set_page_config(page_title="AI Lead Scoring", layout="wide")

st.title("AI Lead Scoring Dashboard")
st.caption("AI-powered prioritization of biotech decision-makers")

df = pd.read_csv("data/leads.csv")
scored_df = score_leads(df)

# 🔍 Search
# 🔍 Search
search_query = st.text_input("Search (name, title, company, location)")

# 📍 Location Filter
locations = ["All"] + sorted(scored_df["location"].unique().tolist())
selected_location = st.selectbox("Filter by Location", locations)

# 🎯 Minimum Score Filter
min_score = st.slider("Minimum Lead Score", 0, 120, 0)


if selected_location != "All":
    scored_df = scored_df[scored_df["location"] == selected_location]

scored_df = scored_df[scored_df["lead_score"] >= min_score]

if search_query:
    scored_df = scored_df[
        scored_df.apply(
            lambda row: search_query.lower() in row.astype(str).str.lower().to_string(),
            axis=1
        )
    ]


st.subheader("Ranked Leads")
st.dataframe(scored_df)

st.download_button(
    label="Download Ranked Leads (CSV)",
    data=scored_df.to_csv(index=False),
    file_name="ranked_leads.csv",
    mime="text/csv"
)
