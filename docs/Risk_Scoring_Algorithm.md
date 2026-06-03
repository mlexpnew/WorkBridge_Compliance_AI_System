# 15. Risk Scoring Algorithm

## 15.1 Objective

The Risk Scoring Engine determines the overall compliance risk associated with an event detected by one or more agents.

The objective is to prioritize investigations and ensure consistent escalation decisions.

---

## 15.2 Scoring Factors

The system evaluates four major dimensions:

### Severity Score (40%)

Measures potential regulatory impact.

| Severity | Score |
| -------- | ----- |
| Low      | 25    |
| Medium   | 50    |
| High     | 75    |
| Critical | 100   |

---

### Confidence Score (30%)

Measures certainty of the agent's finding.

| Confidence | Score |
| ---------- | ----- |
| 0-25%      | 25    |
| 26-50%     | 50    |
| 51-75%     | 75    |
| 76-100%    | 100   |

---

### Evidence Strength (20%)

Measures quality of supporting evidence.

| Evidence Type | Score |
| ------------- | ----- |
| Weak          | 25    |
| Moderate      | 50    |
| Strong        | 75    |
| Verified      | 100   |

---

### Regulatory Impact (10%)

Measures exposure to regulators.

| Impact                | Score |
| --------------------- | ----- |
| Internal Policy       | 25    |
| Minor Reporting Issue | 50    |
| Regulatory Breach     | 75    |
| Enforcement Risk      | 100   |

---

## 15.3 Final Risk Formula

Risk Score =

(0.40 × Severity Score)

*

(0.30 × Confidence Score)

*

(0.20 × Evidence Strength)

*

(0.10 × Regulatory Impact)

---

## 15.4 Escalation Thresholds

| Risk Score | Action              |
| ---------- | ------------------- |
| 0–39       | Monitor             |
| 40–59      | Review              |
| 60–79      | Escalate            |
| 80–100     | Critical Escalation |

---

## 15.5 Example

Case:

* Severity = Critical (100)
* Confidence = 90 (100)
* Evidence = Strong (75)
* Regulatory Impact = Enforcement Risk (100)

Calculation:

Risk Score =

(0.40 × 100)

*

(0.30 × 100)

*

(0.20 × 75)

*

(0.10 × 100)

= 95

Outcome:

Critical Escalation
