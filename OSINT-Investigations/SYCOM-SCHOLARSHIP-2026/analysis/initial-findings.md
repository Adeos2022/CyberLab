# SYCOM Scholarship OSINT
## Initial Technical Findings

Investigation date: 17 October 2026

### Target
sycom.academy/entry-level/

### Application endpoint
sycomail-dev-web.azurewebsites.net/p/sycom-scholar-2026

### DNS
CNAME:
waws-prod-ln1-181.sip.azurewebsites.windows.net

Regional infrastructure:
waws-prod-ln1-181-24ce.uksouth.cloudapp.azure.com

IPv4:
51.104.28.90

### HTTP
Protocol: HTTP/2
Status: 200
Framework: Next.js
Authentication indicators: Clerk
Authentication status: signed-out
Authentication reason: dev-browser-missing

### TLS
Issuer: Microsoft TLS G2 RSA CA OCSP 10
Subject: *.azurewebsites.net
Validity: 7 October 2026 - 23 April 2027

### Preliminary conclusion
The application is hosted on Microsoft Azure infrastructure.
The application responds successfully over HTTPS.
Application ownership and data protection arrangements
remain to be independently verified.

No malicious activity established by these observations.
