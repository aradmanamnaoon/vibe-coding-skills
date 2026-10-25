# Example: audit a completion claim

A user says: "Finish the login feature, test it, and push it."

The `completion-claims-auditor` should turn that into evidence-bearing claims such as:

| Claim | Strong evidence |
|---|---|
| login implemented | route/handler/session code plus focused tests |
| invalid credentials denied | negative integration test |
| browser flow works | observed end-to-end login/logout flow if browser harness is available |
| tests pass | actual test command output |
| pushed | remote branch SHA equals intended local commit |

Code presence alone is insufficient evidence for the runtime claims, and a local commit is insufficient evidence for the push claim.

