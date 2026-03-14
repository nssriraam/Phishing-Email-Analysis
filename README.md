# Phishing Email Analysis Lab

## Overview
A hands-on SOC home lab project focused on analyzing phishing emails, extracting IOCs, and mapping attacker techniques to MITRE ATT&CK.

## Folder Structure
```
phishing-email-analysis/
├── samples/
│   ├── real/          # Real phishing samples from PhishTank
│   └── simulated/     # Manually crafted .eml files
├── analysis/          # Per-sample analysis reports
├── iocs/              # Master IOC tracker
├── tools/             # Python scripts
└── README.md
```

## Tools Used
| Tool | Purpose |
|---|---|
| PhishTank | Source of real phishing samples |
| MXToolbox WHOIS | Domain age and registrar lookup |
| URLScan.io | URL sandbox and behavioral analysis |
| VirusTotal | Multi-engine URL/IP reputation check |
| AbuseIPDB | IP reputation lookup |

## Samples Analyzed
| ID | Type | Target Brand | Verdict | Date |
|---|---|---|---|---|
| phish_001 | Real | Allegro (Poland) | Phishing | 2026-03-14 |
| phish_002 | Real | Gaming Platform (hitmantest.club) | Phishing | 2026-03-14 |
| phish_003 | Real | Gaming Platform (hitmantest.club) | Phishing | 2026-03-14 |

## Key Findings
- Identified 1-day-old domain impersonating Allegro using `.click` TLD
- URLScan flagged as malicious while VirusTotal returned 0/95 — demonstrates false negative risk
- Cloudflare used to mask real hosting infrastructure

## MITRE ATT&CK Techniques Covered
| Technique | ID |
|---|---|
| Phishing: Spearphishing Link | T1566.002 |
| Masquerading | T1036 |
| Obtain Capabilities: Domains | T1583.001 |

## Skills Demonstrated
- Email header analysis
- Domain WHOIS investigation
- IOC extraction and documentation
- Multi-tool cross-validation
- MITRE ATT&CK mapping
