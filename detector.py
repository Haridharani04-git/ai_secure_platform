import re

def analyze_log(text):
    findings = []

    lines = text.split("\n")

    for i, line in enumerate(lines):

        # Email detection
        if re.search(r"\S+@\S+", line):
            findings.append({
                "type": "email",
                "risk": "low",
                "line": i+1
            })

        # Password detection
        if "password" in line.lower():
            findings.append({
                "type": "password",
                "risk": "critical",
                "line": i+1
            })

        # API key detection
        if "api_key" in line.lower():
            findings.append({
                "type": "api_key",
                "risk": "high",
                "line": i+1
            })
    insights = []

    for f in findings:
        if f["type"] == "password":
            insights.append("Sensitive password exposed")
        if f["type"] == "api_key":
            insights.append("API key exposed in logs")

    insights = list(set(insights))
    return {
        "summary": "Log analyzed",
        "findings": findings,
        "risk_score": len(findings),
        "insights": insights
    }