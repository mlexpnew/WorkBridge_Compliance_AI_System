from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ComplianceEvent:
    event_id: str
    source_agent: str
    domain: str
    regulator: str
    severity: str
    confidence_score: float
    risk_score: int
    status: str
    evidence_refs: List[str]
    recommended_action: str


class TransactionMonitor:
    def analyze(self, transaction: Dict[str, Any]) -> ComplianceEvent:

        amount = float(transaction.get("amount", 0))
        country = transaction.get("country", "").lower()

        severity = "Low"
        confidence = 0.50
        risk_score = 30
        regulator = "FINRA"
        action = "Monitor"

        if amount > 100000:
            severity = "High"
            confidence = 0.85
            risk_score = 80
            action = "Escalate"

        if country in ["iran", "north korea", "russia", "cuba", "syria"]:
            severity = "Critical"
            confidence = 0.95
            risk_score = 95
            regulator = "OFAC"
            action = "Immediate Escalation"

        return ComplianceEvent(
            event_id="EVT-TM-001",
            source_agent="TransactionMonitor",
            domain="Trading",
            regulator=regulator,
            severity=severity,
            confidence_score=confidence,
            risk_score=risk_score,
            status="Open",
            evidence_refs=["TXN-001"],
            recommended_action=action
        )