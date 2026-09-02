# Catalogue Schema & Evaluation Methodology

---

## 1. The Hierarchical Data Model

Assessments follow a strict logical sequence to ensure complete auditability:

```
[Dimension]
   └── [Control Objective]
          └── [Control]
                 └── [Question]
                        └── [Evidence]
```

* **Dimension:** The thematic domain (e.g., SML 3 Data Sovereignty).
* **Control Objective:** Technology-neutral target state within a dimension.
* **Control:** Actionable, implementable measure categorized across implementation levels, scopes, and service types.
* **Question:** Binary audit question requiring a clear Yes/No verification.
* **Evidence:** Mandatory proof (contracts, audit logs, architecture diagrams, certifications) substantiating the answer.

---

## 2. Implementation Levels

Every control is assigned to exactly one implementation level:

1. **Contractual Level:** Binding legal agreements, Service Level Agreements (SLAs), terms of service, and subprocessor clauses.
2. **Governance & Operations Level:** Documented policies, organizational procedures, roles, responsibilities, and incident management processes.
3. **Technical Level:** System architectures, API implementations, encryption mechanisms, access control configurations, and hardware isolation.

---

## 3. Control Scopes & Inheritance

To eliminate redundant audits in complex multi-provider cloud stacks, controls are evaluated across three distinct scopes:

| Scope | Abbreviation | Description |
|---|---|---|
| **Client-Facing Service** | `CFS` | The end-user or customer-facing service interface and functionality. |
| **Service Provider** | `SP` | The organizational and legal entity delivering the overall service. |
| **Underlying Service** | `US` | The foundational cloud infrastructure (IaaS/PaaS) supporting the client-facing service. |

!!! tip "Inheritance Principle"
    Infrastructure-level controls (such as physical data center security or power grid resilience assessed under `US`) can be **inherited** by higher-level services (`CFS`), eliminating duplicate audits across supply chains.

---

## 4. Sovereignty Maturity Levels (SML)

IT services are rated across four standardized maturity levels:

* **SML 1 - Initial:** Non-standardized; high external dependencies, undocumented processes, and limited verification.
* **SML 2 - Managed:** Basic dependency management; documented contingency plans and basic contractual safeguards.
* **SML 3 - Advanced:** Structured autonomy; active dependency mitigation, open standards usage, and customer control mechanisms.
* **SML 4 - Future-Proof:** Fully optimized; complete digital autonomy operating on open-source, highly substitutable infrastructures within approved jurisdictions.

---

## 5. Approved Jurisdictions List (AJL)

Legal and jurisdictional controls reference the **Approved Jurisdictions List (AJL)**. The AJL defines trusted geographic regions (typically EU/EEA member states and approved sovereign territories) where data processing, governance, and operational execution provide enforceability and immunity against unauthorized extraterritorial access.
