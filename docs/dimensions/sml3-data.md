# SML 3 — Data Sovereignty

*Data sovereignty measures customer control parameters over data assets throughout their complete lifecycle.*

---

## Control Objectives & Controls

### SML 3.CO 1: Access Control
**Target State:** Customers retain sole, independent control over access to their data without reliance on the provider.

* **SML 3.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts grant customers the exclusive right to control access to their data.  
  * **Question SML 3.CO 1.C 1.Q 1:** Does the contract guarantee exclusive customer control over data access permissions?

* **SML 3.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Operational processes ensure provider personnel cannot access customer data without explicit approval.  
  * **Question SML 3.CO 1.C 2.Q 1:** Are operational controls in place to prevent provider personnel access without customer authorization?

* **SML 3.CO 1.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Technical mechanisms enforce customer-managed access controls and identity federation.  
  * **Question SML 3.CO 1.C 3.Q 1:** Can customers technically enforce and audit access policies independently?

* **SML 3.CO 1.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Customer-managed cryptographic encryption (BYOK/HYOK) prevents unauthorized provider access to data at rest and in transit.  
  * **Question SML 3.CO 1.C 4.Q 1:** Are customer-managed encryption keys supported to technically isolate data from the provider?

---

### SML 3.CO 2: Portability
**Target State:** Customers can extract and transfer their data at any time without technical or financial lock-in.

* **SML 3.CO 2.C 1** | Level: *Contractual* | Scope: *Client Facing Service* | Service Type: *All*  
  Contracts ensure data access, retrieval, and export rights at any time without undue restriction.  
  * **Question SML 3.CO 2.C 1.Q 1:** Does the contract guarantee full data retrieval rights without export penalties?

* **SML 3.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Processes exist for comprehensive data extraction including metadata and configuration states.  
  * **Question SML 3.CO 2.C 2.Q 1:** Are documented procedures in place for complete data export?

* **SML 3.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Service provides standardized APIs and user interfaces for automated, independent data export.  
  * **Question SML 3.CO 2.C 3.Q 1:** Does the service provide standardized APIs for independent data extraction?

---

### SML 3.CO 3: Usage Control
**Target State:** Customer data usage is strictly confined to agreed purposes and protected against unauthorized provider monetization or model training.

* **SML 3.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts prohibit data usage beyond service delivery requirements.  
  * **Question SML 3.CO 3.C 1.Q 1:** Do contracts explicitly restrict provider data usage to service provision?

* **SML 3.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Governance controls enforce purpose limitation across provider operations.  
  * **Question SML 3.CO 3.C 2.Q 1:** Are governance policies active to enforce data purpose limitations?

* **SML 3.CO 3.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Technical safeguards isolate customer data environments to prevent unauthorized access or secondary usage.  
  * **Question SML 3.CO 3.C 3.Q 1:** Are technical controls active to isolate data and prevent unauthorized secondary usage?

---

### SML 3.CO 4: Integrity
**Target State:** Customer data integrity is protected and verifiable throughout processing and storage.

* **SML 3.CO 4.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Data integrity verification and monitoring processes are maintained.  
  * **Question SML 3.CO 4.C 1.Q 1:** Are data integrity verification processes implemented and monitored?

* **SML 3.CO 4.C 2** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Technical mechanisms enforce cryptographic checksums, immutability, and corruption detection.  
  * **Question SML 3.CO 4.C 2.Q 1:** Does the infrastructure provide technical integrity protection and verification mechanisms?
