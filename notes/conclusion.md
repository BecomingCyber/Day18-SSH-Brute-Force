# 🛡️ Conclusion – SSH Brute Force Detection (Day #18)

## 🧾 Summary

This lab demonstrated the practical use of Splunk to detect SSH brute-force attacks through authentication log analysis. By filtering `Failed password` events and applying regular expressions, I was able to extract critical indicators such as attacker usernames and source IP addresses.

Key Splunk capabilities leveraged in this lab included:

- Regex field extraction using `rex`
- Filtering log data with `sourcetype=linux_secure`
- Aggregating suspicious behavior with `stats` and `sort`
- Detecting targeted login attempts by user and IP

---

## 🔍 Findings

- The user `service_account` was the most targeted with **134** failed login attempts.
- The user `thor` was specifically targeted by the IP address `98.110.184.71`, resulting in **119** failed login attempts.
- This pattern is consistent with brute-force behavior aimed at gaining unauthorized access via SSH.

---

## 🧠 Key Takeaways

- **Authentication logs** are a goldmine for detecting early brute-force activity.
- Splunk’s search and extraction tools allow for rapid SOC triage and threat analysis.
- Repeated login failures from the same IP are strong indicators of malicious automation.

---

## ✅ Recommendations

- Deploy **fail2ban** or another log-based intrusion prevention tool.
- Enforce **key-based authentication** for SSH and disable password login where feasible.
- Set up **Splunk alerts** for multiple failed logins within short time windows to enable real-time detection.

---

## 📘 Reflection

This lab not only strengthened my familiarity with Splunk’s search capabilities but also reinforced best practices in analyzing authentication abuse scenarios. The ability to pivot on usernames, IP addresses, and behavior patterns is vital in any SOC or Blue Team setting.

