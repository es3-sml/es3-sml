# SML 6 — Technology Sovereignty

*Technology sovereignty evaluates open standards, cross-platform interoperability, and independence from proprietary technology locks.*

---

## Control Objectives & Controls

### SML 6.CO 1: Infrastructure Location and Control
**Target State:** Physical and virtual infrastructure assets are located and controlled strictly within approved jurisdictions (AJL).

* **SML 6.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts restrict physical data center and server locations to AJL regions.  
  * **Question SML 6.CO 1.C 1.Q 1:** Are infrastructure asset locations contractually restricted to AJL regions?

* **SML 6.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Governance policies mandate AJL compliance for infrastructure selection and expansion.  
  * **Question SML 6.CO 1.C 2.Q 1:** Do infrastructure selection policies mandate compliance with approved jurisdiction lists?

* **SML 6.CO 1.C 3** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Primary, backup, failover, and replication environments reside strictly within AJL locations.  
  * **Question SML 6.CO 1.C 3.Q 1:** Are all primary, failover, and backup data centers located within AJL boundaries?

---

### SML 6.CO 2: Use of Open Standards
**Target State:** Prevent vendor lock-in through the deployment of non-proprietary, open standards across APIs, data formats, and protocols.

* **SML 6.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts commit the provider to using open standards and non-proprietary specifications.  
  * **Question SML 6.CO 2.C 1.Q 1:** Do contracts explicitly commit the provider to open standards usage?

* **SML 6.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Architectural guidelines prioritize open-source software and open protocols.  
  * **Question SML 6.CO 2.C 2.Q 1:** Do architecture guidelines mandate open-source and open-standard prioritization?

* **SML 6.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Service APIs and data formats follow open standards (e.g., REST, OpenAPI, POSIX, SQL).  
  * **Question SML 6.CO 2.C 3.Q 1:** Are service interfaces and data formats implemented using open standards?

* **SML 6.CO 2.C 4** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying infrastructure relies on open technology stacks avoiding proprietary runtime locks.  
  * **Question SML 6.CO 2.C 4.Q 1:** Does the underlying platform rely on open technologies rather than proprietary mechanisms?

---

### SML 6.CO 3: Portability and Interoperability
**Target State:** Applications and workloads can be seamlessly migrated across multi-cloud and hybrid environments.

* **SML 6.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts guarantee interoperability and migration support.  
  * **Question SML 6.CO 3.C 1.Q 1:** Do contracts guarantee workload portability and migration assistance rights?

* **SML 6.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Migration guides and standard deployment blueprints are provided.  
  * **Question SML 6.CO 3.C 2.Q 1:** Are workload migration guides and deployment blueprints made available?

* **SML 6.CO 3.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Standardized container formats (OCI) and open configuration templates (Helm, Terraform) are supported.  
  * **Question SML 6.CO 3.C 3.Q 1:** Are standardized container formats and orchestration blueprints supported?

* **SML 6.CO 3.C 4** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Service supports integration with external systems via open APIs.  
  * **Question SML 6.CO 3.C 4.Q 1:** Does the service provide open APIs for external system integration?

* **SML 6.CO 3.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services allow cross-cloud workload deployment without platform-specific code modification.  
  * **Question SML 6.CO 3.C 5.Q 1:** Can workloads be redeployed on alternative cloud platforms without vendor-specific code modifications?

---

### SML 6.CO 4: Technology Control and Transparency
**Target State:** Complete transparency over tech stack architecture and source code auditability.

* **SML 6.CO 4.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts grant source code audit rights or escrow arrangements for critical software.  
  * **Question SML 6.CO 4.C 1.Q 1:** Are source code audit or escrow rights contractually established?

* **SML 6.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Detailed technical architecture documentation is accessible to customers.  
  * **Question SML 6.CO 4.C 2.Q 1:** Is complete technical architecture documentation provided to customers?

* **SML 6.CO 4.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  System behavior and API executions are verifiable through audit logs.  
  * **Question SML 6.CO 4.C 3.Q 1:** Are technical audit logs generated to independently verify system execution?
