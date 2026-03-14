# Phishing Analysis Report — phish_001

## Overview
| Field | Details |
|---|---|
| Sample ID | phish_001 |
| Type | Real |
| Date Analyzed | 2026-03-14 |
| Verdict | Phishing |
| Severity | High |

## Email Header Analysis
| Field | Value |
|---|---|
| From | noreply@allegrolokalnie.765904.click |
| Reply-To | support@allegrolokalnie.765904.click |
| Return-Path | bounce@allegrolokalnie.765904.click |
| SPF | Fail |
| DKIM | Not Present |
| DMARC | Not Found |
| Originating IP | 188.114.96.3 |
| Mail Server | Cloudflare (CLOUDFLARENET) |

## Sender Analysis
- Real Allegro domain is `allegro.pl` — sender uses `765904.click` (lookalike via subdomain)
- Domain age: 1 day old (created 2026-03-13)
- Registrar: Global Domain Group LLC via Dynadot
- Lookalike technique: prepends `allegrolokalnie` to a random numeric `.click` domain

## URL / Link Analysis
| URL | VirusTotal | URLScan | Verdict |
|---|---|---|---|
| https://allegrolokalnie.765904.click/nintendo-switch-2-caly-zestaw-/50088 | 0/95 | Potentially Malicious | Malicious |

## IOCs Extracted
| Type | Value | Source |
|---|---|---|
| IP | 188.114.96.3 | URLScan.io |
| Domain | 765904.click | Email header / URL |
| Domain | allegrolokalnie.765904.click | Email body |
| URL | https://allegrolokalnie.765904.click/nintendo-switch-2-caly-zestaw-/50088 | Email body |

## Social Engineering Tactics
- Prize/reward lure (fake Nintendo Switch 2 giveaway)
- Impersonation of Allegro (major Polish e-commerce brand)
- Urgency implied by "collect your prize" call to action

## MITRE ATT&CK Mapping
| Technique | ID | Description |
|---|---|---|
| Phishing: Spearphishing Link | T1566.002 | Malicious URL embedded in email body |
| Masquerading | T1036 | Domain mimics legitimate Allegro brand |
| Obtain Capabilities: Domains | T1583.001 | Attacker registered fresh domain 1 day before attack |

## Verdict & Recommended Action
- Verdict: **PHISHING**
- Action: Block domain `765904.click` and all subdomains, report to abuse@dynadot.com, alert users about fake prize emails