# src/app.py

import streamlit as st
from scrape import run_google_search

st.set_page_config(page_title="GGM Insta Scraper", layout="centered")

st.title("🐙 GGM Insta Scraper")
st.write("Scrape Instagram accounts of U.S. niche product businesses manufacturing overseas.")

user_input = st.text_area(
    "Enter search queries (one per line):",
    value=(
        "site:instagram.com U.S. brand sourced from China\n"
        "site:instagram.com American startup imports from India\n"
        "site:instagram.com overseas manufacturer DTC\n"
        "site:instagram.com small business with Asian supplier"
    ),
    height=140
)

if st.button("Start Scraping"):
    queries = [q.strip() for q in user_input.strip().split('\n') if q.strip()]
    for query in queries:
        st.markdown(f"🔍 **Searching:** `{query}`")
        results = run_google_search(query)
        if results and not results[0].startswith("Error:"):
            for url in results:
                st.markdown(f"- [{url}]({url})")
        else:
            st.error(results[0] if results else "No results found.")
