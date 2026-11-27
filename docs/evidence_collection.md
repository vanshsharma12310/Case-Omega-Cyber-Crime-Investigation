
# Evidence Collection and Acquisition

## 1. Introduction

Evidence collection is an important part of digital forensic investigation. In Case Omega, digital evidence is collected to investigate a simulated ransomware attack on a fictional healthcare network.

## 2. Evidence Sources

The following digital evidence sources were identified:

1. Compromised hospital server.
2. Infected workstations.
3. System event logs.
4. Network and firewall logs.
5. USB storage devices.
6. Browser history.
7. User login records.
8. Cloud access logs.

## 3. Evidence Acquisition Tools

The following tools are considered for the investigation:

- FTK Imager
- Linux dd utility
- SHA-256 hashing utility
- Python
- Windows Event Viewer

## 4. Simulated Disk Image Acquisition

A simulated server evidence file is used for this academic project.

In a real investigation, FTK Imager or dd can be used to create a forensic disk image of an authorized compromised server.

The acquisition process includes:

1. Identify the source device.
2. Record device details.
3. Use an approved forensic acquisition tool.
4. Create a forensic image.
5. Preserve the original image.
6. Generate a SHA-256 hash.
7. Verify the acquired image.
8. Document the acquisition process.

## 5. SHA-256 Hash Verification

SHA-256 is a cryptographic hashing algorithm used to verify the integrity of digital evidence.

Example Linux command:

sha256sum evidence_image.dd

The generated hash is recorded in the evidence hash register.

If the hash values before and after transfer match, the file has remained unchanged during that comparison.

## 6. Evidence Preservation

- Original evidence must not be modified.
- Working copies should be used for analysis.
- Evidence should be stored securely.
- Every transfer must be documented.
- Access should be restricted to authorized personnel.

## 7. Conclusion

Evidence acquisition and hash verification help maintain the integrity and reliability of digital forensic evidence.

Note: This project uses simulated evidence and does not contain an actual hospital server disk image.
