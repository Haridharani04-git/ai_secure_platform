import streamlit as st
import requests
st.title("AI Secure Data Intelligence Platform")
st.write("Upload a log file to analyze sensitive data")
text_input = st.text_area("Else you can type log text here")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "log"])
if st.button("Analyze"):
    if uploaded_file is None and not text_input:
        st.warning("Please upload a file or enter text")
    elif uploaded_file is not None and text_input:
        st.warning("Please use either file upload OR text input")
    else:
        try:
            if uploaded_file is not None:
                files = {
                    "file": (uploaded_file.name, uploaded_file, "text/plain")
                }
                response = requests.post(
                    "https://ai-secure-platform.onrender.com/analyze",
                    files=files
                )
            else:
                response = requests.post(
                    "https://ai-secure-platform.onrender.com/analyze",
                    files={"text": (None, text_input)}
                )
            if response.status_code == 200:
                result = response.json()

                st.subheader("Results")
                st.write("Summary:", result.get("summary"))
                st.write("Risk Score:", result.get("risk_score"))
                st.subheader("Findings")
                for item in result.get("findings", []):
                    st.write(item)
                st.subheader("Insights")
                for insight in result.get("insights", []):
                    st.write("-", insight)
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Exception: {e}")