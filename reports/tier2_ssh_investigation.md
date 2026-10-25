# Tier 2 SOC Investigation Report: Suspicious SSH Authentication Activity

**Investigation Type:** SSH Authentication Investigation  
**Classification:** Suspicious SSH Authentication Activity  
**Disposition:** Inconclusive, Further Investigation Required  
**Account Investigated:** `service_account`  
**Source IP:** `8.215.234.245`  
**Log Source:** `/var/log/auth.log`  
**Analysis Platform:** Splunk Enterprise  
**Investigation Period:** March 22–23, 2025  
**Environment:** Simulated SSH authentication dataset

---

## 1. Executive Summary

A Tier 2 investigation was conducted into suspicious SSH authentication activity involving `service_account` and source IP `8.215.234.245`.

Analysis of the available authentication records identified 240 events associated with this account and source, including 134 failed and 106 successful password authentications.

The investigation identified repeated authentication failures, successful authentications occurring after failures, and periods of elevated authentication activity.

Registration information obtained through APNIC RDAP identified the source IP as belonging to a network allocation registered to Alibaba Cloud (Singapore) Private Limited.

Although the observed pattern warrants further investigation, the available evidence does not establish credential compromise, unauthorized access, or malicious post-authentication activity.

**Final Disposition:** Inconclusive. Further investigation required.

## 2. Investigation Scope and Evidence Sources

The investigation used a simulated SSH authentication dataset containing 3,000 records.

Available fields included:

- `timestamp`
- `hostname`
- `pid`
- `user`
- `source_ip`
- `port`
- `event`
- `status`
- `log_source`

The dataset contained two authentication event types:

| Event Type | Total Events |
|---|---:|
| Failed password | 1,500 |
| Accepted password | 1,500 |
| **Total** | **3,000** |

The analysis focused on events involving `service_account` and source IP `8.215.234.245`.

The available dataset did not include command execution, process creation, file access, session activity, or account modification records.

## 3. Authentication Activity Analysis

### 3.1 Account-Level Statistics

| Metric | Finding |
|---|---:|
| Total authentication events | 240 |
| Failed authentications | 134 |
| Successful authentications | 106 |
| Failure rate | 55.8% |
| First observed event | March 22, 2025, 02:09:30 |
| Last observed event | March 23, 2025, 15:50:02 |
| First observed failure | March 22, 2025, 02:09:30 |
| First observed success | March 22, 2025, 03:11:15 |

All 240 observed events for `service_account` originated from `8.215.234.245` within the available dataset.

This concentration of activity warrants further examination but does not independently establish malicious intent.

### 3.2 Elevated Authentication Activity

During March 23, 2025, between 02:00 and 03:00, the dataset contained:

| Metric | Finding |
|---|---:|
| Total events | 25 |
| Failed authentications | 16 |
| Successful authentications | 9 |

The combination of failed and successful authentication events during this period supports additional investigation into credential usage, automation behavior, and source authorization.

### 3.3 Authentication Event Sequence

The following sequence was identified on March 23, 2025:

| Timestamp | Event |
|---|---|
| 02:43:36 | Failed password |
| 02:44:42 | Failed password |
| 02:48:07 | Failed password |
| 02:48:48 | Failed password |
| 02:53:28 | Accepted password |

The successful authentication following multiple failures increases investigative concern.

However, the available records do not establish whether the failures and subsequent success originated from the same process, operator, or attempted credential sequence.

## 4. Failed Authentication Timing Analysis

The 16 failed authentications observed between 02:00 and 03:00 on March 23 produced 15 intervals between consecutive failures.

| Timing Metric | Result |
|---|---:|
| Minimum interval | 28 seconds |
| Maximum interval | 751 seconds |
| Average interval | 224.3 seconds |
| Median interval | 165 seconds |

The variation in intervals does not independently establish automated password guessing.

Potential explanations include automated retries, application configuration problems, repeated manual authentication attempts, or unauthorized credential activity.

## 5. Post-Success Authentication Review

The investigation examined authentication records between March 23, 2025, 02:53:28 and 03:23:29.

This period contained:

- 13 authentication events
- 7 successful authentications
- 6 failed authentications

The available events remained limited to SSH password authentication outcomes.

No session activity, commands, process execution, resource access, or account modifications could be established from this dataset.

**Finding:** Successful authentication was observed, but subsequent system activity could not be determined.

## 6. Source IP and Network Registration Analysis

An RDAP lookup of `8.215.234.245` returned the following APNIC registration information:

| Attribute | Finding |
|---|---|
| Source IP | `8.215.234.245` |
| Address classification | Public IPv4 |
| Registered organization | Alibaba Cloud (Singapore) Private Limited |
| Regional Internet Registry | APNIC |
| Registered network | `8.208.0.0/12` |
| Network name | `ASEPL-SG` |
| Network type | Allocated Portable |
| Abuse contact | `abuse@alibaba-inc.com` |
| Autonomous system number | Not established |

**RDAP reference:** https://rdap.apnic.net/ip/8.208.0.0/12

The network registration provides infrastructure context but does not identify the individual or process responsible for the authentication activity.

The registration address does not establish the physical location of the originating system during the investigated events.

No conclusion of malicious intent was made based solely on cloud-provider ownership.

## 7. Account Authorization Assessment

The available evidence does not establish whether `service_account` was authorized to accept SSH connections from `8.215.234.245`.

A legitimate service account may still generate suspicious authentication activity due to outdated credentials, automation errors, or configuration problems.

Similarly, the existence of a legitimate business purpose for an account does not prove that every authentication attempt was authorized.

Further validation requires account ownership information, approved source IP records, expected authentication behavior, and relevant service configuration.

## 8. Investigative Hypotheses

### Hypothesis 1: Unauthorized Password Guessing

Repeated authentication failures followed by successful authentications could be consistent with unauthorized credential guessing.

**Supporting observations:** Multiple failed authentications, subsequent successes, and concentrated account activity.

**Limitations:** No evidence establishes attacker identity, malicious intent, or unauthorized post-login activity.

**Status:** Unconfirmed.

### Hypothesis 2: Legitimate Automation with Credential or Configuration Issues

An authorized application or scheduled process may repeatedly attempt authentication using outdated or incorrectly configured credentials.

**Supporting observations:** Repeated attempts against a service account could be consistent with automated authentication.

**Limitations:** No automation configuration, account inventory, or authorized source list was available for validation.

**Status:** Unconfirmed.

### Hypothesis 3: Separate Authentication Activities Sharing a Source IP

The failed and successful authentication events may represent different processes or users operating through shared infrastructure.

**Supporting observations:** Authentication events share an observed source IP, but the dataset does not identify individual processes or operators.

**Limitations:** Session correlation and additional endpoint telemetry are unavailable.

**Status:** Unconfirmed.

## 9. Evidence Limitations

The investigation was constrained by the available authentication dataset.

The following could not be verified:

1. Whether the source IP was approved for the account.
2. Whether successful authentications were authorized.
3. Whether failed and successful attempts were generated by the same process or individual.
4. Whether successful SSH sessions executed commands.
5. Whether files, applications, or other resources were accessed.
6. Whether account privileges or configurations were changed.
7. Whether persistence or other unauthorized activity occurred.

The absence of post-authentication records in the dataset does not establish that no such activity occurred.

The available timestamps also did not establish a timezone.

## 10. Recommended Additional Investigation

The incident response team should obtain and correlate additional evidence to determine whether the observed activity was authorized.

**Priority 1: Authentication and Session Correlation**

Collect destination authentication and session records to corroborate successful logins and associate them with specific sessions.

**Priority 2: Endpoint and Audit Evidence**

Review available process creation, command execution, file access, and account modification records associated with the authenticated sessions.

**Priority 3: Account and Source Authorization**

Validate `service_account` ownership, expected usage, approved source IPs, authentication methods, and automation configuration.

**Priority 4: Determine Security Impact**

Identify whether authenticated sessions performed actions inconsistent with the account's authorized business purpose.

Any conclusions should be based on correlated evidence rather than authentication counts alone.

## 11. Final Assessment and Disposition

The investigation confirmed repeated failed and successful SSH password authentications involving `service_account` and source IP `8.215.234.245`.

The observed pattern warrants further investigation because the authorization of the activity and the behavior following successful authentication remain unverified.

The available evidence is insufficient to classify the activity as a confirmed compromise, confirmed brute-force attack, or verified false positive.

**Final Classification:** Suspicious SSH Authentication Activity

**Final Disposition:** Inconclusive, Further Investigation Required

**Escalation Recommendation:** Obtain destination session and endpoint/audit evidence, validate account and source authorization, and correlate successful authentications with subsequent system activity.

---

## 12. Portfolio Demonstration

This investigation demonstrates practical experience in:

- Splunk-based SSH authentication log analysis
- Authentication failure and success correlation
- Time-window and authentication-frequency analysis
- Source IP registration investigation using RDAP
- Competing-hypothesis evaluation
- Evidence-based SOC escalation and reporting
- Recognition of telemetry limitations
- Tier 2 investigation documentation

**Related report:** `reports/tier1_ssh_escalation.md`

**Investigation environment:** Simulated dataset used for cybersecurity portfolio development.
