from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class RegulatoryUpdate:
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


class RegulatoryUpdateTracker:
    def check_updates(self, update: Dict[str, Any]) -> RegulatoryUpdate:
        regulator = update.get("regulator", "SEC")
        title = update.get("title", "").lower()

        severity = "Medium"
        confidence = 0.70
        risk_score = 60
        action = "Review"

        if "sanctions" in title or regulator == "OFAC":
            severity = "Critical"
            confidence = 0.93
            risk_score = 96
            action = "Immediate Escalation"

        if "recordkeeping" in title or "off-channel" in title:
            severity = "High"
            confidence = 0.90
            risk_score = 85
            action = "Escalate"

        return RegulatoryUpdate(
            event_id="EVT-RT-001",
            source_agent="RegulatoryUpdateTracker",
            domain="Regulatory Intelligence",
            regulator=regulator,
            severity=severity,
            confidence_score=confidence,
            risk_score=risk_score,
            status="Open",
            evidence_refs=["REG-001"],
            recommended_action=action
        )