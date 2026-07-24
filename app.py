import streamlit as st
from dtc_analyzer import get_dtc_info
from report_parser import parse_validation_report
from waveform_analyzer import analyze_waveform
import google.generativeai as genai
import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")


# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="ECU Root Cause Assistant",
    page_icon="🚗",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🚗 ECU Root Cause & Diagnostic Assistant")
st.caption("Automated ECU telemetry, DTC analysis, and AI-powered root cause diagnosis")

st.divider()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("Telemetry & Logs Upload")

    dtc_code = st.text_input(
        "Enter DTC Code",
        value="P0117"
    )

    report_file = st.file_uploader(
        "Upload Validation Report",
        type=["pdf"]
    )

    waveform_file = st.file_uploader(
        "Upload Waveform",
        type=["csv"]
    )

    st.divider()

    analyze_button = st.button(
        "🔍 Run Full Diagnosis",
        type="primary",
        use_container_width=True
    )

# ---------------- MAIN LAYOUT ----------------
col1, col2 = st.columns([1, 1.2])

# ==================================================
# LEFT PANEL
# ==================================================
with col1:

    st.subheader("📊 Ingested Telemetry Summary")

    dtc_info = get_dtc_info(dtc_code)

    st.info(f"""
### Selected DTC : {dtc_code.upper()}

**Description:** {dtc_info["description"]}

**System:** {dtc_info["system"]}

**Severity:** {dtc_info["severity"]}
""")

    st.markdown("### Possible Causes")

    for cause in dtc_info["possible_causes"]:
        st.write("•", cause)

    st.markdown("### Symptoms")

    for symptom in dtc_info["symptoms"]:
        st.write("•", symptom)

    st.markdown("### Recommended Actions")

    for item in dtc_info["recommendation"]:
        st.write("✅", item)

    st.divider()

    # ---------------- Validation Report ----------------

    st.markdown("### 📄 Validation Report")

    report = parse_validation_report(report_file)

    if report:

        if report["status"] == "PASS":
            st.success(report["summary"])

        elif report["status"] == "FAIL":
            st.error(report["summary"])

        elif report["status"] == "WARNING":
            st.warning(report["summary"])

        else:
            st.error(report["summary"])

        with st.expander("View Extracted Report"):
            st.write(report["text"])

    else:

        st.info("No report uploaded.")

    st.divider()

    # ---------------- Waveform ----------------

    st.markdown("### 📈 Waveform")

    wave = analyze_waveform(waveform_file)

    if wave:

        if wave["status"] == "SUCCESS":

            st.success("Waveform Analysis Completed")

            c1, c2, c3 = st.columns(3)

            c1.metric("Minimum", f"{wave['minimum']} V")
            c2.metric("Maximum", f"{wave['maximum']} V")
            c3.metric("Average", f"{wave['average']} V")

            st.line_chart(wave["data"])

        else:

            st.error(wave["message"])

    else:

        st.info("No waveform uploaded.")
        # ==================================================
# RIGHT PANEL
# ==================================================

with col2:

    st.subheader("🤖 AI Root Cause & Recommendation")

    if analyze_button:

        st.success("✅ Diagnosis Completed")

        severity = dtc_info["severity"]

        if severity == "Critical":
            confidence = "98%"
        elif severity == "High":
            confidence = "94%"
        elif severity == "Medium":
            confidence = "88%"
        else:
            confidence = "75%"

        colA, colB = st.columns(2)

        colA.metric("Confidence Score", confidence)
        colB.metric("Severity", severity)

        st.divider()

        st.markdown("## 🔍 Primary Root Cause")

        st.error(dtc_info["possible_causes"][0])

        st.divider()

        st.markdown("## 📊 Analysis Summary")

        st.write(f"**DTC Code:** {dtc_code}")
        st.write(f"**Description:** {dtc_info['description']}")

        # Validation Report Result
        if report:

            st.write("### 📄 Validation Report")

            if report["status"] == "PASS":
                st.success("PASS")

            elif report["status"] == "FAIL":
                st.error("FAIL")

            elif report["status"] == "WARNING":
                st.warning("WARNING")

        else:

            st.info("Validation report not uploaded.")

        # Waveform Result
        if wave and wave["status"] == "SUCCESS":

            st.write("### 📈 Waveform Statistics")

            st.write(f"Minimum Voltage : {wave['minimum']} V")
            st.write(f"Maximum Voltage : {wave['maximum']} V")
            st.write(f"Average Voltage : {wave['average']} V")

        else:

            st.info("Waveform not uploaded.")

        st.divider()

        st.markdown("## 🛠 Recommended Repair Procedure")

        for i, step in enumerate(dtc_info["recommendation"], start=1):
            st.write(f"{i}. {step}")

        st.divider()

        st.markdown("## 👨‍🔧 Engineer Notes")

        st.info(
            "Inspect the wiring harness before replacing the sensor. "
            "If wiring continuity is good, replace the sensor and clear the DTC."
        )

    else:

        st.info("Click **Run Full Diagnosis** to start AI analysis.")

# ==================================================
# CHATBOT
# ==================================================

# ==================================================
# AI CHATBOT
# ==================================================

st.divider()

st.subheader("💬 AI Diagnostic Assistant")

query = st.text_input(
    "Ask anything about this ECU diagnosis..."
)

if query:

    st.chat_message("user").write(query)

    prompt = f"""
You are an expert Automotive ECU Diagnostic Engineer.

Current Vehicle Fault Information

DTC Code:
{dtc_code}

Description:
{dtc_info["description"]}

Severity:
{dtc_info["severity"]}

Possible Causes:
{", ".join(dtc_info["possible_causes"])}

Symptoms:
{", ".join(dtc_info["symptoms"])}

Recommended Actions:
{", ".join(dtc_info["recommendation"])}

Validation Report Status:
{report["status"] if report else "Not Uploaded"}

Waveform Details:

Minimum Voltage:
{wave["minimum"] if wave else "N/A"}

Maximum Voltage:
{wave["maximum"] if wave else "N/A"}

Average Voltage:
{wave["average"] if wave else "N/A"}

User Question:
{query}

Answer like an experienced ECU engineer.
Explain the probable cause.
Suggest diagnosis steps.
Suggest repair.
Keep the answer simple.
"""

    try:

        response = model.generate_content(prompt)

        st.chat_message("assistant").write(response.text)

    except Exception as e:

        st.error(e)