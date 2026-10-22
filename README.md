# 🛡️ MCP Enterprise Access Troubleshooter

A Proof of Concept (POC) demonstrating how to use the **Model Context Protocol (MCP)** to securely orchestrate cross-platform Identity and Access Management (IAM) troubleshooting.

This local MCP server allows an AI Assistant (like Claude Desktop) to autonomously diagnose access issues across **Microsoft Entra ID**, **SAP S/4HANA**, and **SAP GRC**, without giving the LLM direct system credentials.

## 🚀 How it Works
The AI is given a strict set of read-only tools via standard standard I/O (stdio). 
When asked: *"Why can't j.doe@company.com access Finance?"*, the AI:
1. Queries the Entra ID mock database for group sync.
2. Queries the SAP mock database for PFCG roles.
3. Queries the SAP GRC mock database for stuck tickets.

## ⚙️ Installation (Mac / Claude Desktop)

1. Clone this repository:
   ```bash
   git clone [https://github.com/nlilabinfo-netizen/mcp-sap-entra-troubleshooter.git](https://github.com/nlilabinfo-netizen/mcp-sap-entra-troubleshooter.git)
   cd mcp-sap-entra-troubleshooter
   pip install -r requirements.txt
