# SML 4 — Operational Sovereignty

*Operational sovereignty evaluates operational independence, administrative access controls, business continuity, and change management.*

---

## Control Objectives & Controls

### SML 4.CO 1: Operational Control
**Target State:** Operational roles, responsibilities, and decision-making over service execution are clearly defined and controlled.

* **SML 4.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define operational roles and allocation of control between customer and provider.  
  * **Question SML 4.CO 1.C 1.Q 1:** Does the contract clearly define operational roles and control allocation?

* **SML 4.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented governance structures define operational responsibilities.  
  * **Question SML 4.CO 1.C 2.Q 1:** Are operational governance structures documented and maintained?

* **SML 4.CO 1.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Service provides customers visibility and influence over operational parameters.  
  * **Question SML 4.CO 1.C 3.Q 1:** Can customers monitor and influence operational parameters?

* **SML 4.CO 1.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Critical operational actions require customer approval and cannot be executed unilaterally by the provider.  
  * **Question SML 4.CO 1.C 4.Q 1:** Are critical operational actions restricted from unilateral provider execution?

* **SML 4.CO 1.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Underlying services support separation of operational responsibilities.  
  * **Question SML 4.CO 1.C 5.Q 1:** Does the underlying infrastructure support operational separation of duties?

---

### SML 4.CO 2: Administrative Access
**Target State:** Privileged administrative access is strictly controlled, auditable, and subject to customer approval.

* **SML 4.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts govern provider administrative access terms and approval requirements.  
  * **Question SML 4.CO 2.C 1.Q 1:** Are provider administrative access terms contractually governed?

* **SML 4.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Processes govern approval, logging, and monitoring of administrative access.  
  * **Question SML 4.CO 2.C 2.Q 1:** Are administrative access requests logged, monitored, and formally approved?

* **SML 4.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Technical mechanisms enforce multi-factor authentication, just-in-time access, and audit logging.  
  * **Question SML 4.CO 2.C 3.Q 1:** Are technical just-in-time access controls and MFA enforced for administrative tasks?

* **SML 4.CO 2.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Administrative actions require dual control or customer consent.  
  * **Question SML 4.CO 2.C 4.Q 1:** Are administrative actions restricted to prevent unilateral provider execution?

* **SML 4.CO 2.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services provide role-based access control and privileged access separation.  
  * **Question SML 4.CO 2.C 5.Q 1:** Does the infrastructure enforce role-based administrative access separation?

---

### SML 4.CO 3: Service Operations
**Target State:** Day-to-day operations are executed according to transparent, defined procedures without discretionary provider deviation.

* **SML 4.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define operational standards and service performance expectations.  
  * **Question SML 4.CO 3.C 1.Q 1:** Are operational service standards contractually defined?

* **SML 4.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Standard operating procedures govern routine maintenance and operations.  
  * **Question SML 4.CO 3.C 2.Q 1:** Are routine operations governed by documented standard operating procedures?

* **SML 4.CO 3.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Customers can monitor operational status in real time.  
  * **Question SML 4.CO 3.C 3.Q 1:** Can customers monitor operational service status in real time?

* **SML 4.CO 3.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Operational activities follow technical policy constraints preventing discretionary provider actions.  
  * **Question SML 4.CO 3.C 4.Q 1:** Are operational activities technically bound to defined execution rules?

---

### SML 4.CO 4: Incident and Recovery
**Target State:** Incident response, failover, and disaster recovery processes guarantee operational resilience and customer visibility.

* **SML 4.CO 4.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts mandate incident notification timelines and recovery commitments.  
  * **Question SML 4.CO 4.C 1.Q 1:** Do contracts specify binding incident notification timelines and recovery SLAs?

* **SML 4.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Incident response and business continuity plans are documented and regularly tested.  
  * **Question SML 4.CO 4.C 2.Q 1:** Are incident response and continuity plans documented and tested?

* **SML 4.CO 4.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Customers can track incident status and recovery progress.  
  * **Question SML 4.CO 4.C 3.Q 1:** Can customers monitor incident status and recovery execution?

* **SML 4.CO 4.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Recovery activities follow automated procedures without sole reliance on provider discretion.  
  * **Question SML 4.CO 4.C 4.Q 1:** Are recovery procedures automated and defined rather than discretionary?

* **SML 4.CO 4.C 5** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Customers can initiate data restoration or recovery processes independently.  
  * **Question SML 4.CO 4.C 5.Q 1:** Can customers initiate recovery and restoration independently?

* **SML 4.CO 4.C 6** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services provide backup, disaster recovery, and failover capabilities.  
  * **Question SML 4.CO 4.C 6.Q 1:** Does underlying infrastructure provide independent backup and failover capabilities?

---

### SML 4.CO 5: Change and Service Evolution
**Target State:** Service updates, patches, and architecture changes are controlled and transparent.

* **SML 4.CO 5.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define change management procedures and approval roles.  
  * **Question SML 4.CO 5.C 1.Q 1:** Are change management roles and notification terms contractually defined?

* **SML 4.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Change governance processes manage planning, testing, and deployment.  
  * **Question SML 4.CO 5.C 2.Q 1:** Are formal change control and testing processes maintained?

* **SML 4.CO 5.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Customers receive advance change notifications and configuration choices.  
  * **Question SML 4.CO 5.C 3.Q 1:** Are customers notified of upcoming service changes with configuration controls?

* **SML 4.CO 5.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Unilateral breaking changes by the provider are technically prevented.  
  * **Question SML 4.CO 5.C 4.Q 1:** Are unilateral breaking service changes prevented by technical release controls?
