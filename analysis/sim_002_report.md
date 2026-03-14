# Phishing Analysis Report — sim_002

## Overview
| Field | Details |
|---|---|
| Sample ID | sim_002 |
| Type | Simulated |
| Date Analyzed | 2026-03-14 |
| Verdict | Phishing |
| Severity | High |

## Email Header Analysis
| Field | Value |
|---|---|
| From | support@paypa1-secure-center.com |
| Reply-To | support@paypa1-secure-center.com |
| Return-Path | bounce@spamserver.com |
| SPF | None (no SPF record) |
| DKIM | Not Present |
| DMARC | Not Found |
| Originating IP | 91.108.56.200 |
| Mail Server | spamserver.com |

## Sender Analysis
- `paypa1-secure-center.com` is a typosquat — letter L replaced with number 1
- Real PayPal domain is `paypal.com`
- Return-Path domain `spamserver.com` does not match sender domain
- No SPF record = domain has no email authentication configured at all

## URL / Link Analysis
| URL | VirusTotal | URLScan | Verdict |
|---|---|---|---|
| http://paypa1-secure-center.com/restore?uid=victim_abc | Not checked | Not checked | Malicious |

## IOCs Extracted
| Type | Value | Source |
|---|---|---|
| IP | 91.108.56.200 | Email header |
| DOMAIN | paypa1-secure-center.com | Email header + body |
| DOMAIN | spamserver.com | Return-Path |
| URL | http://paypa1-secure-center.com/restore?uid=victim_abc | Email body |

## Social Engineering Tactics
- Urgency — account suspended in 48 hours
- Fear — funds restricted, balance at risk
- Impersonation of PayPal
- Typosquat domain using 1 instead of l

## MITRE ATT&CK Mapping
| Technique | ID | Description |
|---|---|---|
| Phishing: Spearphishing Link | T1566.002 | Malicious restore link in email body |
| Masquerading | T1036 | Typosquat domain mimics PayPal |
| Credential Harvesting | T1056 | Fake account restore page steals credentials |
| Obtain Capabilities: Domains | T1583.001 | Attacker registered lookalike domain |

## Verdict & Recommended Action
- Verdict: **PHISHING**
- Action: Block domain `paypa1-secure-center.com`, block IP `91.108.56.200`, report to abuse@paypal.com