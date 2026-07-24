import fitz

def parse_validation_report(uploaded_file):
    if uploaded_file is None:
        return None

    try:
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        result = {
            "status": "PASS",
            "summary": "No issues detected",
            "text": text
        }

        text_lower = text.lower()

        if "fail" in text_lower:
            result["status"] = "FAIL"
            result["summary"] = "Validation report contains failures."

        elif "warning" in text_lower:
            result["status"] = "WARNING"
            result["summary"] = "Validation report contains warnings."

        return result

    except Exception as e:
        return {
            "status": "ERROR",
            "summary": str(e),
            "text": ""
        }