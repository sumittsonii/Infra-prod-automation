#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="github-automation-470314"
gcloud config set project "$PROJECT_ID"
gcloud services enable monitoring.googleapis.com
gcloud monitoring policies create --policy-from-file="/mnt/data/20250904_103119_cicd_pro_pack/repo_files/monitoring/policy_uptime.json"
gcloud monitoring policies create --policy-from-file="/mnt/data/20250904_103119_cicd_pro_pack/repo_files/monitoring/policy_latency.json"
gcloud monitoring policies create --policy-from-file="/mnt/data/20250904_103119_cicd_pro_pack/repo_files/monitoring/policy_5xx_rate.json"
echo "Done. Add notification channels in Cloud Monitoring UI or via API."
