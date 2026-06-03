from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class CommunicationFinding:
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


class CommunicationScanner:
    def scan(self, message: Dict[str, Any]) -> CommunicationFinding:
        text = message.get("text", "").lower()

        severity = "Low"
        confidence = 0.50
        risk_score = 30
        regulator = "SEC"
        action = "Monitor"

        if "whatsapp" in text or "telegram" in text or "signal" in text:
            severity = "High"
            confidence = 0.88
            risk_score = 82
            action = "Escalate"

        if "insider" in text or "don't tell compliance" in text:
            severity = "Critical"
            confidence = 0.96
            risk_score = 97
            action = "Immediate Escalation"

        return CommunicationFinding(
            event_id="EVT-CS-001",
            source_agent="CommunicationScanner",
            domain="Communications",
            regulator=regulator,
            severity=severity,
            confidence_score=confidence,
            risk_score=risk_score,
            status="Open",
            evidence_refs=["MSG-001"],
            recommended_action=action
        )