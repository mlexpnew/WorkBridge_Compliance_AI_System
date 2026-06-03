from src.transaction_monitor import TransactionMonitor
from src.communication_scanner import CommunicationScanner
from src.regulatory_tracker import RegulatoryUpdateTracker
from src.report_generator import ReportGenerator
from src.compliance_cases import ComplianceCase


class ComplianceOrchestrator:
    def __init__(self):
        self.tm = TransactionMonitor()
        self.cs = CommunicationScanner()
        self.rt = RegulatoryUpdateTracker()
        self.rg = ReportGenerator()

    def run_demo(self):
        transaction = {
            "transaction_id": "TXN-1001",
            "amount": 250000,
            "country": "Iran"
        }

        message = {
            "message_id": "MSG-2001",
            "text": "Let us discuss this deal on WhatsApp and not tell compliance."
        }

        update = {
            "update_id": "REG-3001",
            "regulator": "OFAC",
            "title": "New sanctions update"
        }

        txn_event = self.tm.analyze(transaction)
        comm_event = self.cs.scan(message)
        reg_event = self.rt.check_updates(update)

        final_case = ComplianceCase(
            case_id="CASE-0001",
            regulator="OFAC",
            severity="Critical",
            risk_score=max(
                txn_event.risk_score,
                comm_event.risk_score,
                reg_event.risk_score
            ),
            status="Open",
            evidence_refs=txn_event.evidence_refs + comm_event.evidence_refs + reg_event.evidence_refs
        )

        if final_case.risk_score >= 80:
            final_case.escalate()

        report = self.rg.generate({
            "case_id": final_case.case_id,
            "source_agent": "Orchestrator",
            "domain": "Cross-domain Compliance",
            "regulator": final_case.regulator,
            "severity": final_case.severity,
            "risk_score": final_case.risk_score,
            "status": final_case.status,
            "recommended_action": "Immediate Escalation" if final_case.status == "Escalated" else "Monitor",
            "evidence_refs": final_case.evidence_refs,
        })

        print(report)


if __name__ == "__main__":
    ComplianceOrchestrator().run_demo()