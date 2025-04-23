# 📜 SPL Commands Used – SSH Brute Force Lab (Day #18)

This file contains all the SPL (Search Processing Language) queries executed in Splunk to investigate the SSH brute-force attack in the `linux_auth_logs.json` log file.

---

## 🔍 1. Identify the Most Targeted User (Brute-force Attempts)

```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password"
| rex field=_raw "Failed password for (invalid user )?(?<username>\w+)"
| stats count by username
| sort -count
```
Purpose: Extracts usernames and counts how many failed SSH login attempts were made against each. Helps identify the most targeted user.

## 🔍 2. Find IP Address Attempting to Access User thor
```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password" "thor"
| rex field=_raw "from (?<ip>\d{1,3}(?:\.\d{1,3}){3})"
| stats count by ip
```
Purpose: Filters log entries that show failed logins for user thor, extracts attacker IP addresses, and summarizes them.

## 🔍 3. Count Failed Login Attempts for thor
```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password" "thor"
| stats count
```
Purpose: Provides the total number of failed login attempts for the thor account.

## 🛠️ Notes
- Ensure correct index, sourcetype, host, and source are set to match your ingestion config.

- These queries assume the log file follows standard SSH syslog formatting within a JSON wrapper.