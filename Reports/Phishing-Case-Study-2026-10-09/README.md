# WhatsApp Suspicious-Link Investigation

**Case ID:** PHISH-2026-10-09-001
**Investigation date:** 2026-10-09
**Classification:** Suspicious — unconfirmed
**Method:** Passive threat intelligence and evidence analysis

## 1. Overview

An unexpected WhatsApp message advertised a supposed
surprise message and included a link to an unfamiliar domain.

The recipient reported not clicking the link. The investigation
used passive analysis rather than visiting the landing page.

Personal identifiers and the original message URL have been
omitted from this public case study.

## 2. Objectives

- Parse the URL into its constituent indicators.
- Examine DNS and domain-registration information.
- Review Certificate Transparency records.
- Check available public reputation information.
- Preserve evidence and verify file integrity.
- Distinguish observed facts from unconfirmed hypotheses.

## 3. Methodology

### URL analysis
Parsed the supplied URL offline to identify its scheme,
hostname, path and query parameters.

### DNS and registration
Reviewed DNS records, nameservers and WHOIS registration
metadata. Cloudflare infrastructure was observed, but this
alone is neither evidence of malicious activity nor proof
of the origin server.

### Certificate Transparency
Retrieved certificate records and analysed them locally.
The query returned 136 records and 10 unique DNS names.
Four records included an additional DNS name outside the
investigated domain. This association does not establish
common ownership or malicious intent.

### Reputation research
Reviewed public domain-reputation services. Results provided
warning signals but were not fully consistent and did not
prove the behaviour of the exact URL.

### Evidence integrity
Calculated SHA-256 hashes for investigation artifacts and
verified that eight files matched their recorded hashes.

## 4. Findings

- The message used surprise-related wording that could
  encourage a recipient to open an unfamiliar link.
- DNS results were consistent with use of Cloudflare
  infrastructure.
- Certificate records showed historical certificate activity.
- Public reputation services raised concerns, with differing
  assessments.
- The URL was not directly opened during this investigation.
- No malicious payload, credential collection or redirect
  behaviour was directly observed.

## 5. Limitations

- The sender's identity was not independently verified.
- The exact landing-page behaviour remains unknown.
- Certificate records do not prove malicious activity.
- Reputation services may contain stale or conflicting data.
- Hash verification confirms consistency with recorded hashes,
  not the accuracy of the underlying observations.
- No attribution to a threat actor was established.

## 6. Risk assessment

**Assessment: Suspicious; malicious behaviour unconfirmed.**

The message's social-engineering cues and external reputation
warnings justified caution. Available evidence was insufficient
to conclude that the exact URL was malicious.

## 7. Recommended response

1. Do not open suspicious unsolicited links.
2. Verify the sender through a separate trusted channel.
3. Preserve the original message and relevant timestamps.
4. Use trusted reporting mechanisms where appropriate.
5. Maintain a dated evidence log and verify file integrity.
6. Avoid publishing private identifiers or unverified claims.

## 8. Skills demonstrated

- URL parsing and indicator extraction
- DNS and WHOIS analysis
- Certificate Transparency research
- Threat-intelligence interpretation
- SHA-256 integrity verification
- Evidence documentation
- Risk assessment and analytical restraint

## 9. Ethical scope

This was a defensive, passive investigation. No attempt was
made to access, exploit or modify the destination website.
