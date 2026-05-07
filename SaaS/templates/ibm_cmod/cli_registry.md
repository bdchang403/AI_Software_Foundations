# CMOD ODWEK Java Registry

When interacting with CMOD programmatically, Copilot MUST use the official ODWEK (OnDemand Web Enablement Kit) Java API `ODServer`. Do not generate Bash scripts if a Java API solution is requested.

## ODServer Connection Pattern
```java
// Copilot MUST ALWAYS ensure connection is properly initialized and logged off.
ODServer odServer = new ODServer();
try {
    odServer.initialize("CMODIntegrationApp");
    odServer.logon(instanceName, username, password);
    
    // Process logic here
    
} finally {
    odServer.logoff();
    odServer.terminate();
}
```

## Document Search Pattern
```java
// Standard pattern for folder searching in ODWEK
ODFolder folder = odServer.openFolder("Invoices");
folder.setSearchValue("Account Number", "1234567890");
Vector<ODHit> hits = folder.search();
```
