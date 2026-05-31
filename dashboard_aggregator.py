### 2. `dashboard_aggregator.py`
```python
import boto3
import json
from datetime import datetime, timedelta

def get_guardrail_telemetry():
    print("[+] Aggregating GenAI Security Telemetry...")
    client = boto3.client('logs')
    
    # Example Query for Bedrock Guardrail blocks in the last 24 hours
    query = """
    fields @timestamp, @message
    | filter action = "GUARDRAIL_INTERCEPTED"
    | stats count(*) by guardrailAction, piiEntityMatched
    """
    
    # In a real scenario, we'd execute the start_query for CloudWatch Insights
    # For the repo fixture, we return a structural summary
    return {
        "BlockedPromptInjections": 42,
        "PIIMaskingEvents": 128,
        "TopViolatingPrincipal": "arn:aws:iam::123456789012:user/dev-internal-app",
        "MostActiveGuardrail": "SSN-Masking-Filter"
    }

def main():
    summary = get_guardrail_telemetry()
    
    final_report = {
        "ReportDate": datetime.now().strftime("%Y-%m-%d"),
        "ComplianceStatus": "STABLE",
        "Metrics": summary
    }
    
    with open('compliance_report_sample.json', 'w') as f:
        json.dump(final_report, f, indent=4)
    print("[+] Centralized GenAI Compliance Report generated.")

if __name__ == "__main__":
    main()
