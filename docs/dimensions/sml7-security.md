# SML 7 — Security and Compliance Sovereignty

*Security and compliance sovereignty evaluates access control mechanisms, security visibility, and technical isolation of sensitive operations.*

---

## Control Objectives & Controls

### SML 7.CO 1: Identity and Access Management
**Target State:** Identity federation, zero-trust access control, and privileged role separation are enforced.

* **SML 7.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts mandate identity governance standards and access isolation commitments.  
  * **Question SML 7.CO 1.C 1.Q 1:** Do contracts mandate strict identity governance and access isolation standards?

* **SML 7.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Identity and access management policies follow least-privilege principles.  
  * **Question SML 7.CO 1.C 2.Q 1:** Are IAM policies based on least-privilege principles documented and enforced?

* **SML 7.CO 1.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  MFA, Single Sign-On (SSO via SAML/OIDC), and Role-Based Access Control (RBAC) are supported.  
  * **Question SML 7.CO 1.C 3.Q 1:** Are SAML/OIDC identity federation and MFA technically enforced?

* **SML 7.CO 1.C 4** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Infrastructure provides hardware-enforced tenant isolation and zero-trust network segmentation.  
  * **Question SML 7.CO 1.C 4.Q 1:** Does the underlying infrastructure provide hardware-enforced tenant isolation?

---

### SML 7.CO 2: Security Visibility and Control
**Target State:** Complete customer visibility into security event logs, configurations, and threat alerts.

* **SML 7.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts guarantee customer access to real-time security audit logs.  
  * **Question SML 7.CO 2.C 1.Q 1:** Does the contract guarantee customer access to security log streams?

* **SML 7.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Security monitoring, SIEM integration, and vulnerability response processes are active.  
  * **Question SML 7.CO 2.C 2.Q 1:** Are security monitoring and vulnerability response processes maintained?

* **SML 7.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Service provides SIEM-compatible log streaming and real-time security event alerts.  
  * **Question SML 7.CO 2.C 3.Q 1:** Does the service export real-time SIEM-compatible security event logs?

---

### SML 7.CO 3: Sensitive Operations and Isolation
**Target State:** High-security and sensitive administrative workloads are executed in isolated, confidential environments.

* **SML 7.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define security isolation guarantees for sensitive customer operations.  
  * **Question SML 7.CO 3.C 1.Q 1:** Do contracts specify technical isolation guarantees for sensitive workloads?

* **SML 7.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Operational procedures enforce strict segregation of duties for sensitive administrative tasks.  
  * **Question SML 7.CO 3.C 2.Q 1:** Are segregation of duties policies enforced for high-security operations?

* **SML 7.CO 3.C 3** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Confidential computing (memory encryption, enclave protection) isolates sensitive data during execution.  
  * **Question SML 7.CO 3.C 3.Q 1:** Is confidential computing hardware deployed to protect data in memory during processing?
