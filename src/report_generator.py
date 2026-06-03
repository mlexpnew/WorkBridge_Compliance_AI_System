class ReportGenerator:
    def generate(self, case_data):
        return f"""
COMPLIANCE CASE REPORT
======================

Case ID: {case_data.get("case_id", "CASE-UNKNOWN")}
Source Agent: {case_data.get("source_agent", "N/A")}
Domain: {case_data.get("domain", "N/A")}
Regulator: {case_data.get("regulator", "N/A")}
Severity: {case_data.get("severity", "N/A")}
Risk Score: {case_data.get("risk_score", "N/A")}
Action: {case_data.get("recommended_action", "N/A")}

Evidence:
- {", ".join(case_data.get("evidence_refs", []))}

Summary:
The system detected a potential compliance issue and generated this report for audit and review.
""".strip()