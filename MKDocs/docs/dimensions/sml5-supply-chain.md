# SML 5 — Supply Chain Sovereignty

*Supply chain sovereignty evaluates geographic composition, component tracking (SBOM), and subprocessor risk management.*

---

## Control Objectives & Controls

### SML 5.CO 1: Subprocessor Transparency
**Target State:** Complete visibility over all third-party sub-providers and processing locations involved in service delivery.

* **SML 5.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts require full disclosure and prior customer approval for subprocessor additions or changes.  
  * **Question SML 5.CO 1.C 1.Q 1:** Does the contract require advance notice and customer approval for subprocessor changes?

* **SML 5.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Updated lists of subprocessors, roles, and processing locations are publicly accessible or provided to customers.  
  * **Question SML 5.CO 1.C 2.Q 1:** Is an up-to-date directory of subprocessors and locations maintained and accessible?

* **SML 5.CO 1.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Subprocessor monitoring and audit processes are conducted regularly.  
  * **Question SML 5.CO 1.C 3.Q 1:** Are subprocessors systematically audited and monitored?

---

### SML 5.CO 2: Component & Software Bill of Materials (SBOM) Transparency
**Target State:** Transparency over software components, open-source libraries, and hardware assets powering the service.

* **SML 5.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts guarantee transparency regarding major software dependencies and components.  
  * **Question SML 5.CO 2.C 1.Q 1:** Are component transparency commitments included in contracts?

* **SML 5.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  A Software Bill of Materials (SBOM) is maintained and updated across the service lifecycle.  
  * **Question SML 5.CO 2.C 2.Q 1:** Is an updated Software Bill of Materials (SBOM) maintained for the service?

* **SML 5.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Automated component vulnerability tracking and version verification are active.  
  * **Question SML 5.CO 2.C 3.Q 1:** Are automated tools used to track component provenance and security vulnerabilities?

---

### SML 5.CO 3: Supplier Governance and Risk Management
**Target State:** Third-party vendor risks are governed, assessed, and systematically mitigated.

* **SML 5.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts impose binding security, legal, and operational compliance requirements on suppliers.  
  * **Question SML 5.CO 3.C 1.Q 1:** Do supplier contracts mandate strict compliance with sovereignty standards?

* **SML 5.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Vendor risk assessment frameworks evaluate concentration risks and geopolitical dependencies.  
  * **Question SML 5.CO 3.C 2.Q 1:** Are supplier concentration and geopolitical risks systematically evaluated?

* **SML 5.CO 3.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Continuous supplier compliance monitoring and periodic re-evaluations are conducted.  
  * **Question SML 5.CO 3.C 3.Q 1:** Are suppliers subject to continuous risk and compliance monitoring?

---

### SML 5.CO 4: Dependency Mitigation and Substitution
**Target State:** Critical supplier dependencies can be substituted or mitigated without operational failure.

* **SML 5.CO 4.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts ensure supplier exit assistance and transition support rights.  
  * **Question SML 5.CO 4.C 1.Q 1:** Do supplier contracts include exit transition assistance clauses?

* **SML 5.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Alternative supplier options or fallback strategies are documented for critical components.  
  * **Question SML 5.CO 4.C 2.Q 1:** Are fallback supplier options documented for single-point-of-failure components?

* **SML 5.CO 4.C 3** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Infrastructure modularity enables substitution of underlying service modules.  
  * **Question SML 5.CO 4.C 3.Q 1:** Is the underlying technical stack modularized to allow component substitution?

---

### SML 5.CO 5: Requirement Flow-Down
**Target State:** Sovereignty and control requirements are passed down and legally enforced across all supply chain tiers.

* **SML 5.CO 5.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts require sub-tier providers to comply with mandatory customer sovereignty rules.  
  * **Question SML 5.CO 5.C 1.Q 1:** Are customer sovereignty rules contractually passed down to sub-suppliers?

* **SML 5.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Processes verify that sub-suppliers uphold flow-down commitments.  
  * **Question SML 5.CO 5.C 2.Q 1:** Are operational processes active to verify sub-supplier flow-down compliance?

* **SML 5.CO 5.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Supplier non-compliance is identified, remediated, or triggers contract termination.  
  * **Question SML 5.CO 5.C 3.Q 1:** Are supplier non-compliance events formally managed and remediated?
