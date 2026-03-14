# Phishing Analysis Report — sim_001

## Overview
| Field | Details |
|---|---|
| Sample ID | sim_001 |
| Type | Simulated |
| Date Analyzed | 2026-03-14 |
| Verdict | Phishing |
| Severity | High |

## Email Header Analysis
| Field | Value |
|---|---|
| From | security-alert@micros0ft-verify.com |
| Reply-To | noreply@micros0ft-verify.com |
| Return-Path | bounce@malicious-relay.ru |
| SPF | Fail |
| DKIM | Not Present |
| DMARC | Not Found |
| Originating IP | 185.220.101.45 |
| Mail Server | malicious-relay.ru |

## Sender Analysis
- `micros0ft-verify.com` is a typosquat — letter O replaced with zero (0)
- Real Microsoft domain is `microsoft.com`
- Return-Path uses `.ru` Russian domain — mismatch with sender