# 17. Compliance Event Schema

## Purpose

The Compliance Event Schema defines the standard communication format used by all agents in the Multi-Agent Compliance Monitoring Platform.

This ensures interoperability, traceability, and auditability across the system.

---

# ComplianceEvent Object

```json
{
  "event_id": "EVT-2026-0001",
  "case_id": "CASE-2026-1001",
  "source_agent": "TransactionMonitor",
  "domain": "Trading",
  "regulator": "SEC",
  "severity": "Critical",
  "confidence_score": 0.94,
  "risk_score": 92,
  "status": "Open",
  "timestamp": "2026-06-03T14:00:00Z",
  "evidence_refs": [
    "TRADE_12345",
    "EMAIL_98765"
  ],
  "recommended_action": "Escalate",
  "assigned_reviewer": "ComplianceOfficer",
  "audit_trace_id": "TRACE-123456"
}
```

---

# Field Definitions

| Field              | Description                           |
| ------------------ | ------------------------------------- |
| event_id           | Unique event identifier               |
| case_id            | Compliance investigation case         |
| source_agent       | Agent generating the event            |
| domain             | Trading, Lending, Communications, AML |
| regulator          | SEC, FCA, FINRA, OFAC                 |
| severity           | Low, Medium, High, Critical           |
| confidence_score   | Agent confidence                      |
| risk_score         | Final risk score                      |
| status             | Open, Closed, Escalated               |
| timestamp          | Event creation time                   |
| evidence_refs      | Supporting evidence                   |
| recommended_action | Agent recommendation                  |
| assigned_reviewer  | Human reviewer                        |
| audit_trace_id     | Traceability identifier               |

---

# Event Lifecycle

1. Event Created
2. Agent Enrichment
3. Conflict Resolution
4. Human Review
5. Report Generation
6. Case Closure
7. Audit Archive

---

# Benefits

* Standardized communication
* Easier auditing
* Better observability
* Simplified integration
* Consistent reporting

```
```
