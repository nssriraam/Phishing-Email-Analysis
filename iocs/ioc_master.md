# IOC Master List — Phishing Email Analysis Lab

## Legend
| Type | Description |
|---|---|
| IP | IP Address |
| URL | Full malicious URL |
| DOMAIN | Malicious domain |

---

## phish_001 — Allegro Fake Prize (2026-03-14)

| Type | Value | Verdict | Source Tool | Notes |
|---|---|---|---|---|
| IP | 188.114.96.3 | Malicious | URLScan.io | Cloudflare-hosted, Ascension Island |
| DOMAIN | 765904.click | Malicious | WHOIS | 1 day old, registered via Dynadot |
| DOMAIN | allegrolokalnie.765904.click | Malicious | URLScan.io | Impersonates Allegro Poland |
| URL | https://allegrolokalnie.765904.click/nintendo-switch-2-caly-zestaw-/50088 | Malicious | URLScan.io | Fake Nintendo Switch prize page |

---

## phish_002 — Hitman Gaming Impersonation (2026-03-14)

| Type | Value | Verdict | Source Tool | Notes |
|---|---|---|---|---|
| DOMAIN | hitmantest.club | Malicious | WHOIS + PhishTank | 3 days old, Dynadot registrar |
| URL | https://hitmantest.club/ | Malicious | PhishTank | Verified phish, false negative on VT + URLScan |

---

## phish_003 — Hitman Credential Harvesting Page (2026-03-14)

| Type | Value | Verdict | Source Tool | Notes |
|---|---|---|---|---|
| DOMAIN | hitmantest.club | Malicious | WHOIS + PhishTank | Same domain as phish_002 |
| URL | https://hitmantest.club/as.php | Malicious | PhishTank | /as.php = credential harvesting endpoint |

---

## sim_001 — Simulated Microsoft Typosquat (2026-03-14)

| Type | Value | Verdict | Source Tool | Notes |
|---|---|---|---|---|
| IP | 185.220.101.45 | Malicious | Manual Analysis | Raw IP in link, no domain |
| DOMAIN | micros0ft-verify.com | Malicious | Manual Analysis | Typosquat — O replaced with 0 |
| DOMAIN | malicious-relay.ru | Malicious | Manual Analysis | Russian relay, Return-Path mismatch |
| URL | http://185.220.101.45/microsoft/login?track=victim123 | Malicious | Manual Analysis | Fake Microsoft login page |

---

## sim_002 — Simulated PayPal Typosquat (2026-03-14)

| Type | Value | Verdict | Source Tool | Notes |
|---|---|---|---|---|
| IP | 91.108.56.200 | Malicious | Manual Analysis | Originating IP from email header |
| DOMAIN | paypa1-secure-center.com | Malicious | Manual Analysis | Typosquat — l replaced with 1 |
| DOMAIN | spamserver.com | Malicious | Manual Analysis | Return-Path mismatch |
| URL | http://paypa1-secure-center.com/restore?uid=victim_abc | Malicious | Manual Analysis | Fake PayPal restore page |