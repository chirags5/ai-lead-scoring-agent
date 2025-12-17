# AI Lead Scoring Agent

This project is an AI-assisted lead identification and scoring system designed to help business development teams prioritize high-intent prospects in the biotech and life sciences domain.

The system simulates an intelligent web agent that identifies profiles, enriches them with contextual signals, and assigns a probability-based lead score.

---

## 🚀 Features

- Lead identification using professional and scientific attributes
- Data enrichment (role, company funding, location, research activity)
- Weighted lead scoring (0–100+)
- Automatic ranking of prospects
- Interactive dashboard built with Streamlit
- Exportable and searchable table view

---

## 🧠 Scoring Logic (Propensity Engine)

Each lead is scored using business-driven signals:

| Signal            | Description                                              |
| ----------------- | -------------------------------------------------------- |
| Role Fit          | Leadership roles in toxicology, safety, hepatic research |
| Company Funding   | Series A/B companies score higher                        |
| Location Hub      | Biotech hubs (Boston, Cambridge, Basel, etc.)            |
| Scientific Intent | Recent publications in relevant domains                  |
| Technographic Fit | Usage of similar technologies                            |

The final score is a weighted sum of these signals.

> Note: This rule-based engine is intentionally designed as a first-stage AI system and can later be replaced by a machine learning model once labeled conversion data becomes available.

---

## 🛠 Tech Stack

- Python
- Pandas
- Streamlit
- CSV-based structured data (mocked for demo)

---

## 📊 Dashboard Preview

The Streamlit dashboard displays:

- Ranked leads by score
- Search and filtering
- Clear distinction between low and high probability prospects

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
