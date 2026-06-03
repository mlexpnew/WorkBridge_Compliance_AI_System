from src.transaction_monitor import TransactionMonitor
from src.communication_scanner import CommunicationScanner
from src.regulatory_tracker import RegulatoryUpdateTracker


def test_transaction_monitor():
    agent = TransactionMonitor()

    result = agent.analyze({
        "amount": 250000,
        "country": "Iran"
    })

    assert result.severity == "Critical"


def test_communication_scanner():
    agent = CommunicationScanner()

    result = agent.scan({
        "text": "Let's discuss this on WhatsApp."
    })

    assert result.severity == "High"


def test_regulatory_tracker():
    agent = RegulatoryUpdateTracker()

    result = agent.check_updates({
        "regulator": "OFAC",
        "title": "New sanctions update"
    })

    assert result.severity == "Critical"