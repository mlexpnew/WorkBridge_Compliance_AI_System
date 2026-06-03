# Agent Interaction Sequence Diagram

```text
Transaction Monitor
        │
        │ Detect Suspicious Trade
        ▼
Agent Orchestrator
        │
        ├────────────► Communication Scanner
        │              Check related emails,
        │              chats and call transcripts
        │
        │◄──────────── Findings Returned
        │
        ├────────────► Regulatory Update Tracker
        │              Check latest SEC/FCA/
        │              FINRA/OFAC rules
        │
        │◄──────────── Regulatory Impact
        │
        ▼
Conflict Resolution Engine
        │
        ├── Low Risk
        │      ▼
        │   Close Case
        │
        └── High Risk
               ▼
       Human Review
               │
               ▼
       Report Generator
               │
               ▼
       Audit Repository
               │
               ▼
       Regulatory Report
```
