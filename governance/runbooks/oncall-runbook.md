# Data Platform On-call Runbook

## Alerts
- Freshness breach (>2h delay)
- Pipeline failures > 3 consecutive runs
- Data quality high severity failures

## Triage Steps
1. Check ADF monitor for failed activity and error code.
2. Verify Databricks job run and cluster logs.
3. Check Azure SQL blocking/wait stats if serving issue.
4. Escalate to domain owner if source Oracle issue.

## Standard Actions
- Re-run selective pipeline with table list parameter.
- Reprocess failed partition date in Databricks.
- Roll back to previous known good notebook/job version.

## Communication Template
"Incident <ID> started at <UTC>. Impact: <Dashboard/Domain>. Current status: <Investigating/Mitigating/Resolved>. Next update in 30 mins."
