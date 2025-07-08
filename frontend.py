import streamlit as st
import requests

API_URL = "http://localhost:8000/get_purport/" # Local FastAPI endpoint

st.title("📜 Srimad Bhagavatam Purport Summarizer")

# User input
verse = st.text_input("Enter SB verse (e.g., 2.2.2):")
summarize = st.checkbox("Summarize purport", value=True)

# Submit button
if st.button("Get Purport"):
    if not verse:
        st.warning("Please enter a verse reference.")
    else:
        with st.spinner("Fetching purport..."):
            try:
                response = requests.post(API_URL, json={"verse": verse, "summarize": summarize})
                if response.status_code == 200:
                    data = response.json()
                    st.success("Purport fetched successfully!")
                    st.markdown(f"**Verse:** {data['verse']}")
                    if summarize:
                        st.markdown("## Summary:")
                        st.write(data["summary"])
                    else:
                        st.markdown("### 📖 Full Purport:")
                        st.write(data["purport"])
                else:
                    st.error(f"Error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Exception occurred: {e}")
