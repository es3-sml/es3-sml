---
hide:
  - toc
class: widescreen-page # <-- Weist der Seite im HTML direkt eine Klasse zu!
---

# 🛡️ Sovereignty Maturity Level (SML) Assessment Tool

This interactive tool allows you to perform a complete self-assessment of your digital sovereignty based on the official **SML Framework (v1.1)** with all 162 controls.

## 📊 Interactive Assessment Dashboard

The tool runs completely inside your browser using **WebAssembly (stlite/Pyodide)**. No data is sent to an external server—your entries, evidence, and compliance results remain entirely private within your browser session.

<div class="sml-container" style="display: block !important; min-height: 650px; height: 82vh; width: 100%; border: 1px solid #e0e0e0; border-radius: 8px;">
  <iframe class="sml-iframe" src="../sml-tool.html" style="width: 100%; height: 100%; border: none; display: block !important;"></iframe>
</div>

---

## 📘 Quick Start Guide

### Step 1: Preparation
* Gather all relevant documentation for the service being evaluated (e.g., contracts, SLAs, encryption concepts, corporate structure, architecture diagrams).
* Identify key subject matter experts (Security, Legal, Data Privacy, Strategy, AI Engineers) within your organization.

### Step 2: Assess Dimension by Dimension
* Use the sidebar navigation within the tool to go through the **9 SML dimensions** (SML 1 to SML 9).
* Check **`Fulfilled (Yes)`** if a control is fully met.
* **Document your findings**: Fill out the **`Evidence`** free-text field with precise details (such as document titles, internal SOPs, or roles). *Unsubstantiated "Yes" answers hold no compliance value during audits!*

### Step 3: Save & Resume Progress
* **Export**: At any point, navigate to the **`Data Management`** panel in the sidebar, fill in your audit metadata (Scope, Service Type, Version), and click **`Export Assessment (JSON)`** to download your progress in plain text.
* **Resume**: Next time you open the docs, use **`Load Assessment (JSON)`** to upload your saved file. All answers, evidence texts, and metadata will be restored instantly with zero UI latency.

### Step 4: Evaluate Gaps
* Analyze the **Radar Chart** on the **`Dashboard Overview`** to identify gaps.
* Check the **`Overall open requirements for the next maturity level`** card.
* To elevate your maturity level, satisfy all outstanding mandatory controls marked with a badge of the next level (e.g., `🌱 Initial`).
