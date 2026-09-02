# SML 8 — Environmental Sustainability

*Environmental sustainability analyzes energy autonomy, power grid resilience, and long-term environmental risk exposure.*

---

## Control Objectives & Controls

### SML 8.CO 1: Energy Autonomy
**Target State:** Data centers and operations incorporate renewable energy sources and local energy storage resilience.

* **SML 8.CO 1.C 1** | Level: *Contractual* | Scope: *Underlying Service* | Service Type: *All*  
  Contracts specify renewable energy sourcing and energy efficiency benchmarks (PUE).  
  * **Question SML 8.CO 1.C 1.Q 1:** Do contracts specify renewable energy commitments and Power Usage Effectiveness (PUE) targets?

* **SML 8.CO 1.C 2** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Data centers feature redundant grid connections and local renewable energy storage systems.  
  * **Question SML 8.CO 1.C 2.Q 1:** Are data centers equipped with redundant power connections and local energy storage?

---

### SML 8.CO 2: Resource Dependencies
**Target State:** Dependencies on critical natural resources (water cooling, rare earths) are governed and minimized.

* **SML 8.CO 2.C 1** | Level: *Contractual* | Scope: *Underlying Service* | Service Type: *All*  
  Contracts require resource-efficient infrastructure operation (WUE benchmarks).  
  * **Question SML 8.CO 2.C 1.Q 1:** Are Water Usage Effectiveness (WUE) metrics contractually governed?

* **SML 8.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Resource dependency management policies monitor critical material supply chains.  
  * **Question SML 8.CO 2.C 2.Q 1:** Are resource supply chain risks actively monitored and managed?

* **SML 8.CO 2.C 3** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Closed-loop cooling systems minimize external water consumption.  
  * **Question SML 8.CO 2.C 3.Q 1:** Are closed-loop or waterless cooling technologies deployed?

---

### SML 8.CO 3: Environmental Risk Exposure
**Target State:** Infrastructure location selection mitigates climate change and environmental disaster risks.

* **SML 8.CO 3.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Environmental risk assessments govern data center location choices.  
  * **Question SML 8.CO 3.C 1.Q 1:** Are environmental and climate risk assessments conducted for data center locations?

* **SML 8.CO 3.C 2** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Geographic site selection avoids high-risk flood, seismic, or extreme weather zones.  
  * **Question SML 8.CO 3.C 2.Q 1:** Are infrastructure locations selected to minimize natural disaster risks?

---

### SML 8.CO 4: Dependency Transparency
**Target State:** Full customer transparency over sustainability metrics and carbon footprint data.

* **SML 8.CO 4.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Sustainability reporting publishes Scope 1, 2, and 3 emissions data.  
  * **Question SML 8.CO 4.C 1.Q 1:** Are carbon emissions (Scope 1, 2, 3) regularly audited and reported?

* **SML 8.CO 4.C 2** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *All*  
  Service provides customer dashboards tracking workload-specific energy usage and carbon footprint.  
  * **Question SML 8.CO 4.C 2.Q 1:** Does the service provide customer dashboards for tracking carbon metrics?

---

### SML 8.CO 5: Long-term Operational Sustainability
**Target State:** Long-term hardware lifecycle governance and circular economy practices.

* **SML 8.CO 5.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Hardware recycling and circular economy policies manage asset decommissioning.  
  * **Question SML 8.CO 5.C 1.Q 1:** Are certified hardware recycling and circular economy processes enforced?

* **SML 8.CO 5.C 2** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Energy-aware workload scheduling optimizes hardware power consumption dynamically.  
  * **Question SML 8.CO 5.C 2.Q 1:** Is dynamic energy-aware workload scheduling implemented?
