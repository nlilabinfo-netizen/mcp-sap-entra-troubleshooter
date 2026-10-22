from mcp.server.fastmcp import FastMCP
import json

# Initialize the MCP Server
mcp = FastMCP("EnterpriseAccessTroubleshooter")

# ==========================================
# 1. MOCK ENTERPRISE DATA (Replace with real APIs in production)
# ==========================================
MOCK_ENTRA_DB = {
    "j.doe@company.com": {
        "active": True,
        "groups": ["All_Employees", "Finance_Team"],
        "last_sync": "2026-10-15T08:00:00Z"
    }
}

MOCK_SAP_DB = {
    "JDOE": {
        "system": "S4P",
        "client": "100",
        "roles": ["Z_BASIC_ACCESS"], # Missing Z_FIORI_FINANCE
        "locked": False
    }
}

MOCK_GRC_DB = {
    "8849": {
        "user": "JDOE",
        "requested_roles": ["Z_FIORI_FINANCE"],
        "status": "PENDING_MANAGER_APPROVAL",
        "submitted_date": "2026-10-14"
    }
}

# ==========================================
# 2. MCP TOOLS (Exposed to the LLM)
# ==========================================
@mcp.tool()
def get_entra_user_status(email: str) -> str:
    """Check Microsoft Entra ID for user group memberships and sync status."""
    user = MOCK_ENTRA_DB.get(email)
    if not user:
        return json.dumps({"error": f"User {email} not found in Entra ID."})
    return json.dumps(user, indent=2)

@mcp.tool()
def get_sap_user_roles(sap_username: str) -> str:
    """Check SAP (S4P) for a user's currently provisioned PFCG roles."""
    user_data = MOCK_SAP_DB.get(sap_username.upper())
    if not user_data:
        return json.dumps({"error": f"User {sap_username} not found in SAP."})
    return json.dumps(user_data, indent=2)

@mcp.tool()
def get_grc_request_status(ticket_id: str) -> str:
    """Check SAP GRC Access Control for the status of an access request."""
    ticket = MOCK_GRC_DB.get(ticket_id)
    if not ticket:
        return json.dumps({"error": f"GRC Ticket {ticket_id} not found."})
    return json.dumps(ticket, indent=2)

if __name__ == "__main__":
    mcp.run(transport='stdio')
