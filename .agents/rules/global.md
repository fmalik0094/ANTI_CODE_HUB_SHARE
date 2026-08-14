# GLOBAL PRECEDENCE CONSTRAINTS
*   **Rule Hierarchy:** Absolute constraint resolution: DENY > ASK > ALLOW. Workspace configurations or local scripts can only restrict, never expand, this safety baseline.
*   **Implicit Policies:** Write access implies Read access. Deny Read access immediately enforces Deny Write access.
*   **Terminal Execution:** Policy set to REQUEST REVIEW. Unvetted terminal commands are explicitly blocked.
*   **Agent Identity:** Every session must claim one role from `.agents/AGENT_REGISTRY.md` and use a unique Execution ID.
*   **Audit Trail:** Commands, mutations, validations, results, and handoffs must be recorded in `.state/EXECUTION_LOG.md`; secrets and restricted source content are prohibited.
*   **Terminal Timeout & Process Termination:** Fast terminal operations must request maximum synchronous wait (`WaitMsBeforeAsync: 10000`) to complete in-turn without spawning lingering async tasks. Scripts spawning external binaries must enforce explicit process termination in `finally:` blocks.
*   **Terminal Execution Closure:** All terminal executions must complete with explicit status closure and verification logging before concluding.
