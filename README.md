# 🛡️ Day #18 – Splunk: Investigating SSH Brute Force Attacks

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Lab Status](https://img.shields.io/badge/status-complete-success)
![Splunk](https://img.shields.io/badge/tool-Splunk-informational)
![30-Day SOC Challenge](https://img.shields.io/badge/Challenge-30--Day--SOC-blue)

## 🎯 Objective

Detect and investigate SSH brute-force attacks using Splunk by analyzing failed login attempts from Linux authentication logs. Identify suspicious users and attacker IP addresses using SPL queries.

---

## 🖥️ Lab Environment

- **Platform**: Ubuntu Server 22.04+
- **Tool**: Splunk Enterprise / Free Edition
- **Log File**: `linux_auth_logs.json`
- **Sourcetype**: `linux_secure`
- **Index**: `main`
- **Host**: `ubuntu`

---

## 🧪 Lab Setup

1. **Install Splunk on Ubuntu**
2. **Ingest `linux_auth_logs.json`** using:
   - `source="linux_auth_logs.json"`
   - `sourcetype="linux_secure"`
3. **Start Search & Reporting** app in Splunk

---

## 🔍 Investigation Steps

### 🔸 Question 1: Which user attempted the most SSH brute force logins?

```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password"
| rex field=_raw "Failed password for (invalid user )?(?<username>\w+)"
| stats count by username
| sort -count
```
📸
![Most targeted SSH username](./images/q1_user_attempts.png)

### 🔸 Question 2: What is the IP address of user thor?
```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password" "thor"
| rex field=_raw "from (?<ip>\d{1,3}(?:\.\d{1,3}){3})"
| stats count by ip
```
📸
![IP address that targeted thor](./images/q2_thor_ip.png)


🔸 Question 3: How many times did user thor fail to login?
```spl
index=main sourcetype=linux_secure source="linux_auth_logs.json" host="ubuntu"
"Failed password" "thor"
| stats count
```
📸
![Failed login attempts for user thor](./images/q3_thor_failures.png)


## 🧾 Evidence & Artifacts

- 📂 `images/` – Contains snapshots of each query result  
- 📜 `commands_used.md` – Includes all SPL queries  
- 🧠 `findings.md` – Summary of identified attacker behaviors  
- 🛡️ `notes/conclusion.md` – Write-up of security implications  

---

## ✅ Conclusion

This lab demonstrated how repeated SSH login failures can indicate brute-force activity. Using Splunk's powerful search capabilities and regular expressions, I extracted key evidence (usernames, IPs, counts) to support a security incident analysis. This workflow reflects common tasks performed by SOC analysts during authentication abuse investigations.

---

## 🧠 Lessons Learned

- Regular expressions can extract meaningful fields from syslog-style messages.
- Brute-force patterns become obvious when visualized or summarized.
- Identifying IPs early helps block malicious actors via firewalls (UFW, iptables, etc.)

---

## 📘 License

This lab documentation is licensed under the **MIT License**.
