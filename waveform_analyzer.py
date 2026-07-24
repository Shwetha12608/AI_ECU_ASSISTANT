import pandas as pd

def analyze_waveform(uploaded_file):

    if uploaded_file is None:
        return None

    try:

        df = pd.read_csv(uploaded_file)

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return {
                "status": "ERROR",
                "message": "No numeric columns found",
                "data": None
            }

        voltage = numeric.iloc[:,0]

        return {
            "status":"SUCCESS",
            "minimum":round(voltage.min(),2),
            "maximum":round(voltage.max(),2),
            "average":round(voltage.mean(),2),
            "data":voltage
        }

    except Exception as e:

        return {
            "status":"ERROR",
            "message":str(e),
            "data":None
        }