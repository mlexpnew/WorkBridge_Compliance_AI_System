from src.orchestrator import ComplianceOrchestrator


def test_demo_runs():
    orchestrator = ComplianceOrchestrator()
    orchestrator.run_demo()
    assert True