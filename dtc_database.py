# dtc_database.py

DTC_DATABASE = {

    "P0117": {
        "description": "Engine Coolant Temperature Circuit Low Input",
        "system": "Engine",
        "severity": "High",
        "possible_causes": [
            "Coolant temperature sensor short to ground",
            "Damaged wiring harness",
            "Loose connector",
            "Faulty Engine Coolant Temperature (ECT) sensor",
            "ECU input pin failure"
        ],
        "symptoms": [
            "Check Engine Light ON",
            "Poor fuel economy",
            "Cooling fan runs continuously",
            "Hard starting"
        ],
        "recommendation": [
            "Inspect sensor connector",
            "Measure sensor resistance",
            "Check wiring continuity",
            "Replace ECT sensor if defective"
        ]
    },

    "P0300": {
        "description": "Random/Multiple Cylinder Misfire Detected",
        "system": "Engine",
        "severity": "Critical",
        "possible_causes": [
            "Faulty spark plugs",
            "Ignition coil failure",
            "Fuel injector problem",
            "Vacuum leak"
        ],
        "symptoms": [
            "Engine vibration",
            "Poor acceleration",
            "Engine stalls"
        ],
        "recommendation": [
            "Inspect spark plugs",
            "Check ignition coils",
            "Inspect injectors"
        ]
    },

    "P0101": {
        "description": "Mass Air Flow Sensor Performance",
        "system": "Air Intake",
        "severity": "Medium",
        "possible_causes": [
            "Dirty MAF sensor",
            "Air intake leak",
            "Faulty sensor"
        ],
        "symptoms": [
            "Poor acceleration",
            "High fuel consumption"
        ],
        "recommendation": [
            "Clean MAF sensor",
            "Inspect intake hose",
            "Replace sensor"
        ]
    }

}