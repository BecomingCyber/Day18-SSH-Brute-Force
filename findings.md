# 🧠 Findings – SSH Brute Force Investigation (Day #18)

## 🔍 Overview

This document summarizes the key observations derived from analyzing the `linux_auth_logs.json` file using Splunk. The goal was to identify brute-force SSH login attempts by inspecting failed login patterns and suspicious IP addresses.

---

## 👤 Most Targeted Username

**Username**: `service_account`  
**Failed Attempts**: `134`  
This user received the highest number of brute-force login attempts, indicating it was a primary target for the attacker.

---

## 🌐 Suspicious IP Associated with User `thor`

**IP Address**: `98.110.184.71`  
**Number of Failed Logins**: `119`  
This IP consistently attempted to access the system using the user `thor`, indicating a targeted brute-force campaign.

---

## 📊 Behavior Summary

| Suspicious IP     | Targeted User     | Attempt Count |
|-------------------|-------------------|----------------|
| 98.110.184.71     | `thor`            | 119            |
| [REDACTED/OTHER]  | `service_account` | 134            |

> Note: You can expand this table with other attackers/IPs if needed.

---

## 🛡️ Risk Assessment

- **Attack Type**: SSH Brute Force
- **Impact Level**: Medium to High
- **Indicators of Compromise**: Repeated failed SSH login attempts from single IPs, often targeting the same usernames

---

## 🧾 Evidence Reference

- `images/q1_user_attempts.png`
- `images/q2_thor_ip.png`
- `- 📸 [q3_thor_failures.png](images/q3_thor_failures.png) – Total failed login count for user `thor`
`

---

## 🧠 Insights

- Attackers often target service or default accounts like `service_account`.
- Brute-force login attempts are typically noisy and can be detected by repeated failure patterns.
- IP `98.110.184.71` attempted login to a specific user (`thor`) 119 times, confirming a targeted attack.

---

## ✅ Recommendation

- Implement **fail2ban** or a similar tool to automatically block repeated SSH failures.
- Disable SSH password authentication and enforce **key-based login**.
- Use Splunk alerts or dashboards to continuously monitor and respond to brute-force behavior.

