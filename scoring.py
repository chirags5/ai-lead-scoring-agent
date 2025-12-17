import pandas as pd


def compute_lead_score(row):
    score = 0

    # Role fit
    if any(keyword in row["title"].lower() for keyword in [
        "director", "head", "vp", "principal"
    ]):
        score += 30

    # Funding intent
    if row["company_funding"] in ["Series A", "Series B"]:
        score += 20

    # Hub location
    if row["hub_location"] == "Yes":
        score += 10

    # Scientific intent
    if row["published_recent_paper"] == "Yes":
        score += 40

    # Tech alignment
    if row["uses_similar_tech"] == "Yes":
        score += 15

    return score


def score_leads(df):
    df["lead_score"] = df.apply(compute_lead_score, axis=1)
    return df.sort_values("lead_score", ascending=False)
