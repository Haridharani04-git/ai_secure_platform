import streamlit as st
import requests
import json
st.set_page_config(page_title="AI Secure Platform", layout="wide")
st.markdown("""
<style>
.stApp {
    background-color: #FFFFFF;
    color: black;
}
/* Labels fix */
label {
    color: black !important;
    font-weight: 600;
}
/* Text area */
textarea {
    background-color: #F5F5F5 !important;
    color: black !important;
    border-radius: 8px;
}
/* Button */
.stButton > button {
    background-color: #0A66C2;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
}
/* Success box */
.stAlert {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<h1>AI Secure Data Intelligence Platform</h1>", unsafe_allow_html=True)
st.write("Analyze logs and detect sensitive data like emails, passwords and API keys.")
col1, col2 = st.columns(2)
with col1:
    text_input = st.text_area("Enter log text below:")
with col2:
    uploaded_file = st.file_uploader("Upload log file below:", type=["txt", "log"])
if st.button("Analyze"):
    if uploaded_file is None and not text_input:
        st.warning("Please upload log file or enter log text")
    elif uploaded_file is not None and text_input:
        st.warning("Use either file Or text donot enter both")
    else:
        try:
            if uploaded_file:
                response = requests.post(
                    "https://ai-secure-platform.onrender.com/analyze",
                    files={"file": uploaded_file}
                )
            else:
                response = requests.post(
                    "https://ai-secure-platform.onrender.com/analyze",
                    files={"text": (None, text_input)}
                )
            if response.status_code == 200:
                result = response.json()
                st.success("Analysis Complete")
                st.subheader("Results")
                st.write("**Summary:**", result.get("summary"))
                st.write("**Risk Score:**", result.get("risk_score"))
                st.write("**Action:**", result.get("action"))
                st.subheader("Findings")
                for item in result.get("findings", []):
                    st.write(item)
                st.subheader("Insights")
                for insight in result.get("insights", []):
                    st.write("•", insight)
                report = json.dumps(result, indent=4)
                st.download_button(
                    label="⬇ Download Report",
                    data=report,
                    file_name="analysis_report.json",
                    mime="application/json"
                )
                st.subheader("Log Viewer")
                if text_input:
                    st.code(text_input, language="text")
                elif uploaded_file:
                    uploaded_file.seek(0)
                    content = uploaded_file.read().decode("utf-8")
                    st.code(content, language="text")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Exception: {e}")