# SML 9 — Artificial Intelligence (AI) Sovereignty

*AI sovereignty evaluates organizational oversight, system clarity, dataset protection, model lineage, and human control over AI solutions.*

---

## Control Objectives & Controls

### SML 9.CO 1: AI Governance
**Target State:** Governance structures define clear accountability, ethical oversight, and risk management for AI systems.

* **SML 9.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts define legal accountability for AI model output, safety, and compliance with AI regulations.  
  * **Question SML 9.CO 1.C 1.Q 1:** Do contracts clearly assign responsibility and accountability for AI system outputs?

* **SML 9.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  AI ethics committees and risk management frameworks govern model development and deployment.  
  * **Question SML 9.CO 1.C 2.Q 1:** Are AI governance bodies and risk management frameworks operational?

* **SML 9.CO 1.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Technical guardrails enforce safety constraints and prevent unauthorized AI model behavior.  
  * **Question SML 9.CO 1.C 3.Q 1:** Are technical safety guardrails implemented to constrain AI execution?

---

### SML 9.CO 2: AI Transparency
**Target State:** Complete visibility over model architecture, weights origin, and training parameters.

* **SML 9.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts require full disclosure of underlying AI models, fine-tuning methods, and third-party APIs.  
  * **Question SML 9.CO 2.C 1.Q 1:** Does the contract mandate full transparency regarding model architecture and APIs?

* **SML 9.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Model System Cards publish detailed technical specs, known limitations, and bias assessments.  
  * **Question SML 9.CO 2.C 2.Q 1:** Are comprehensive Model Cards published for all deployed AI models?

* **SML 9.CO 2.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Service provides model version tracking and prompt/response audit logging.  
  * **Question SML 9.CO 2.C 3.Q 1:** Are model versions and inference interactions logged for auditability?

---

### SML 9.CO 3: Explainability & Human Oversight
**Target State:** High-stakes AI decisions are explainable, traceable, and subject to human intervention.

* **SML 9.CO 3.C 1** | Level: *Contractual* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Contracts guarantee human-in-the-loop review rights for critical AI-driven decisions.  
  * **Question SML 9.CO 3.C 1.Q 1:** Do contracts grant customers the right to mandate human review over AI outputs?

* **SML 9.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Operational guidelines establish human oversight procedures for automated model decisions.  
  * **Question SML 9.CO 3.C 2.Q 1:** Are operational human-in-the-loop oversight procedures active?

* **SML 9.CO 3.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Feature attribution tools and explainability metrics (SHAP, LIME) are integrated into the interface.  
  * **Question SML 9.CO 3.C 3.Q 1:** Are explainability tools integrated to illuminate model decision factors?

---

### SML 9.CO 4: External AI Dependencies
**Target State:** Dependencies on third-party AI APIs or proprietary foundational models are monitored and substitutable.

* **SML 9.CO 4.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts require disclosure of external AI API calls and model hosting locations.  
  * **Question SML 9.CO 4.C 1.Q 1:** Are external AI model API calls and processing regions contractually disclosed?

* **SML 9.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Fallback plans define alternative open-weights models if primary AI providers become unavailable.  
  * **Question SML 9.CO 4.C 2.Q 1:** Are fallback open-weights models documented to replace external AI APIs?

* **SML 9.CO 4.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Model-agnostic abstraction layers allow swapping underlying LLM or ML backends.  
  * **Question SML 9.CO 4.C 3.Q 1:** Is the service built on a model-agnostic abstraction layer enabling easy model swapping?

---

### SML 9.CO 5: AI Lifecycle Management
**Target State:** Complete control over model training, fine-tuning, versioning, and decommissioning.

* **SML 9.CO 5.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts govern model update schedules and deprecation timelines.  
  * **Question SML 9.CO 5.C 1.Q 1:** Are model deprecation and update timelines contractually defined?

* **SML 9.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  MLOps processes manage dataset versioning, model retraining, and evaluation benchmarks.  
  * **Question SML 9.CO 5.C 2.Q 1:** Are MLOps procedures established for versioning and evaluation?

* **SML 9.CO 5.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Customers can pin specific model versions to prevent unexpected output drift.  
  * **Question SML 9.CO 5.C 3.Q 1:** Can customers pin model versions to maintain output consistency?

* **SML 9.CO 5.C 4** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Defined processes govern model retraining and update validation.  
  * **Question SML 9.CO 5.C 4.Q 1:** Are formal processes defined for model retraining and updating?

---

### SML 9.CO 6: Control over AI Assets
**Target State:** Customer ownership over fine-tuned weights, embeddings, prompts, and custom model artifacts.

* **SML 9.CO 6.C 1** | Level: *Contractual* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Contracts explicitly state that customer fine-tuned weights, adapters (LoRA), and embeddings remain customer property.  
  * **Question SML 9.CO 6.C 1.Q 1:** Do contracts guarantee customer ownership over fine-tuned weights and embeddings?

* **SML 9.CO 6.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Processes ensure secure export or complete deletion of custom model artifacts upon termination.  
  * **Question SML 9.CO 6.C 2.Q 1:** Are procedures active for exporting or deleting custom model artifacts?

* **SML 9.CO 6.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Technical mechanisms allow downloading custom model adapters and embeddings in open formats (e.g., Safetensors).  
  * **Question SML 9.CO 6.C 3.Q 1:** Can custom model adapters and weights be exported in open formats?

---

### SML 9.CO 7: External Access to Training Data
**Target State:** Technical isolation preventing provider reuse or storage of customer input prompts or output data for AI training.

* **SML 9.CO 7.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts strictly prohibit the provider from using customer prompts, inputs, or outputs for foundation model training.  
  * **Question SML 9.CO 7.C 1.Q 1:** Do contracts prohibit provider model training on customer prompts and outputs?

* **SML 9.CO 7.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Data sanitization policies prevent customer data leakages into public AI repositories.  
  * **Question SML 9.CO 7.C 2.Q 1:** Are operational sanitization policies active to block data leakages?

* **SML 9.CO 7.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Zero-data-retention (ZDR) API enforcement prevents persistent storage of inference data by the provider.  
  * **Question SML 9.CO 7.C 3.Q 1:** Is Zero Data Retention (ZDR) technically enforced at the API layer?

---

### SML 9.CO 8: Training Data Governance
**Target State:** Full transparency, copyright integrity, and legal compliance regarding pre-training datasets.

* **SML 9.CO 8.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *AI Service*  
  Contracts guarantee that pre-training datasets comply with copyright and data protection laws.  
  * **Question SML 9.CO 8.C 1.Q 1:** Do contracts warrant copyright and GDPR compliance of training datasets?

* **SML 9.CO 8.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Data provenance tracking documents dataset sources, licensing, and filtering methodologies.  
  * **Question SML 9.CO 8.C 2.Q 1:** Is dataset provenance, licensing, and filtering fully documented?

* **SML 9.CO 8.C 3** | Level: *Technical* | Scope: *Client Facing Service* | Service Type: *AI Service*  
  Data filtering mechanisms purge toxic, personal, or non-compliant content prior to training.  
  * **Question SML 9.CO 8.C 3.Q 1:** Are automated dataset filtering algorithms active to purge non-compliant content?
