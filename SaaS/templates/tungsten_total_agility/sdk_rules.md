# TTA SDK Function Registry

You MUST use these specific `Agility.Sdk.Model` patterns. Do not invent standard C# methods for state management.

## Update Job Variable
```csharp
// Correct pattern to update a job variable in TTA
var session = new SessionContext { SessionId = sessionId };
var jobService = new JobService();
jobService.UpdateJobVariable(session, jobId, new Variable { Id = "VarName", Value = "NewValue" });
```
