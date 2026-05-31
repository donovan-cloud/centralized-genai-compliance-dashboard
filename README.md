# Centralized GenAI Compliance & Guardrail Dashboard

[![Telemetry](https://img.shields.io/badge/Engine-CloudWatch%20Logs-orange.svg)](https://aws.amazon.com/cloudwatch/)
[![Compliance](https://img.shields.io/badge/Audit-PII%20%2F%20Injections-red.svg)](https://aws.amazon.com/bedrock/guardrails/)
[![Language](https://img.shields.io/badge/Report-JSON%20Artifact-blue.svg)](https://www.json.org/)

## 📋 Operational Overview

This repository features a centralized security telemetry aggregator that pulls real-time logs from Bedrock Guardrails, Model Invocation logs, and AWS Security Hub into a unified "Compliance Ledger."

In a multi-app AI environment, security teams need a single source of truth for "How many prompt injections were blocked today?" and "Which applications are triggering PII masking the most?". This automation engine queries the Amazon Bedrock CloudWatch Log Groups, parses the JSON metadata, and compiles an executive dashboard-ready report on the organization's AI security posture.

---

### 🛡️ Core Metrics Aggregated

* **Guardrail Trigger Frequency:** Tracks which specific filters (Toxicity, PII, Prompt Attack) are being hit most often.
* **Token Utilization Audit:** Maps model usage back to specific IAM principals to detect anomalous "shadow AI" activity.
* **Model Latency & Safety Trade-off:** Correlates security filter overhead with model response times to optimize performance.

---

## 📂 Repository Structural Mapping
```text
centralized-genai-compliance-dashboard/
├── README.md                      # Dashboard metrics and reporting logic
├── dashboard_aggregator.py        # Python engine for log parsing
├── requirements.txt               # Dependencies (boto3)
└── compliance_report_sample.json  # Mock output of the centralized ledger
