# Phishing Email Analysis Lab

## Overview
A hands-on SOC home lab project focused on analyzing real and simulated phishing emails, extracting IOCs, and mapping attacker techniques to MITRE ATT&CK.

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
| Python | Automated header parsing and IOC extraction |

## Samples Analyzed
| ID | Type | Target Brand | Verdict | Date |
|---|---|---|---|---|
| phish_001 | Real | Allegro (Poland) | Phishing | 2026-03-14 |
| phish_002 | Real | Gaming Platform (hitmantest.club) | Phishing | 2026-03-14 |
| phish_003 | Real | Gaming Platform (hitmantest.club) | Phishing | 2026-03-14 |
| sim_001 | Simulated | Microsoft | Phishing | 2026-03-14 |
| sim_002 | Simulated | PayPal | Phishing | 2026-03-14 |

## Key Findings
- Identified 1-day-old domain impersonating Allegro using `.click` TLD
- URLScan flagged phish_001 as malicious while VirusTotal returned 0/95 — demonstrates false negative risk on newly registered domains
- Cloudflare used to mask real hosting infrastructure across multiple samples
- phish_002 and phish_003 both returned clean on VirusTotal and URLScan despite being verified by PhishTank — further confirms false negative pattern
- Simulated samples demonstrate typosquatting techniques (`micros0ft-verify.com`, `paypa1-secure-center.com`)
- `/as.php` path in phish_003 identified as classic credential harvesting endpoint structure

## MITRE ATT&CK Techniques Covered
| Technique | ID |
|---|---|
| Phishing: Spearphishing Link | T1566.002 |
| Masquerading | T1036 |
| Obtain Capabilities: Domains | T1583.001 |
| Credential Harvesting | T1056 |

## Skills Demonstrated
- Email header analysis (From, Reply-To, Return-Path, SPF, DKIM, DMARC)
- Domain WHOIS investigation and domain age analysis
- IOC extraction and structured documentation
- Multi-tool cross-validation (VirusTotal, URLScan.io, MXToolbox)
- False negative identification across security tools
- Typosquatting and lookalike domain detection
- Python scripting for automated header parsing and IOC extraction
- MITRE ATT&CK mapping
