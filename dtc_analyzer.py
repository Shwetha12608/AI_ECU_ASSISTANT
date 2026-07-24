# dtc_analyzer.py

from dtc_database import DTC_DATABASE


def get_dtc_info(dtc_code):

    dtc_code = dtc_code.upper()

    if dtc_code in DTC_DATABASE:
        return DTC_DATABASE[dtc_code]

    return {
        "description": "Unknown DTC",
        "system": "Unknown",
        "severity": "Unknown",
        "possible_causes": [
            "Code not found in database"
        ],
        "symptoms": [],
        "recommendation": [
            "Refer manufacturer service manual"
        ]
    }