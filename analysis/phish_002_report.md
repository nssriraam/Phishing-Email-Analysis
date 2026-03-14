# Phishing Analysis Report — phish_002

## Overview
| Field | Details |
|---|---|
| Sample ID | phish_002 |
| Type | Real |
| Date Analyzed | 2026-03-14 |
| Verdict | Phishing |
| Severity | Medium |

## Email Header Analysis
| Field | Value |
|---|---|
| From | noreply@hitmantest.club |
| Reply-To | support@hitmantest.club |
| Return-Path | bounce@hitmantest.club |
| SPF | Fail |
| DKIM | Not Present |
| DMARC | Not Found |
| Originating IP | Unknown (masked) |
| Mail Server | Dynadot DNS (dyna-ns.net) |

## Sender Analysis
- Domain `hitmantest.club` is 3 days old (created 2026-03-11)
- Registered via Dynadot Inc — same registrar as phish_001
- `.club` TLD commonly used in disposable phishing domains
- Possible gaming platform impersonation

## URL / Link Analysis
| URL | VirusTotal | URLScan | Verdict |
|---|---|---|---|
| https://hitmantest.club/ | 0/95 Clean | Clean | Suspicious — false negative |

## IOCs Extracted
| Type | Value | Source |
|---|---|---|
| Domain | hitmantest.club | Email header / URL |
| URL | https://hitmantest.club/ | Email body |

## Social Engineering Tactics
- Account verification urgency
- Impersonation of gaming service
- Fear of losing account access

## MITRE ATT&CK Mapping
| Technique | ID | Description |
|---|---|---|
| Phishing: Spearphishing Link | T1566.002 | Malicious URL in email body |
| Masquerading | T1036 | Domain mimics gaming brand |
| Obtain Capabilities: Domains | T1583.001 | Fresh domain registered 3 days prior |

## Verdict & Recommended Action
- Verdict: **PHISHING**
- Action: Block domain `hitmantest.club`, report to abuse@dynadot.com
- Note: Both VirusTotal and URLScan returned clean — demonstrates false negative risk on newly registered domains