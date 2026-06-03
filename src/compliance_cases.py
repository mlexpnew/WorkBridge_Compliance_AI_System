from dataclasses import dataclass
from typing import List


@dataclass
class ComplianceCase:
    case_id: str
    regulator: str
    severity: str
    risk_score: int
    status: str
    evidence_refs: List[str]

    def escalate(self):
        self.status = "Escalated"

    def close(self):
        self.status = "Closed"