def analyze_log(text):
    findings = []
    lines = text.split("\n")
    for i, line in enumerate(lines, start=1):
        if "@" in line:
            findings.append({
                "type": "email",
                "risk": "low",
                "line": i
            })
        if "password" in line.lower():
            findings.append({
                "type": "password",
                "risk": "critical",
                "line": i
            })
        if "api_key" in line.lower():
            findings.append({
                "type": "api_key",
                "risk": "high",
                "line": i
            })
    return {
        "summary": "Log analyzed",
        "findings": findings,
        "risk_score": len(findings),
        "insights": [
            "Sensitive data detected" if findings else "No issues found"
        ]
    }