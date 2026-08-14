# GLOBAL PRECEDENCE CONSTRAINTS
*   **Rule Hierarchy:** Absolute constraint resolution: DENY > ASK > ALLOW. Workspace configurations or local scripts can only restrict, never expand, this safety baseline.
*   **Implicit Policies:** Write access implies Read access. Deny Read access immediately enforces Deny Write access.
*   **Terminal Execution:** Policy set to REQUEST REVIEW. Unvetted terminal commands are explicitly blocked.
