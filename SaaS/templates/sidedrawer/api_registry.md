# SideDrawer API Payload Registry

When writing Java scripts/services to call the SideDrawer API, Copilot MUST format the payload this way using Jackson. Do not guess the structure.

## Create Drawer (POST /v1/drawers)
```java
// Use Jackson ObjectMapper to construct the payload dynamically
ObjectMapper mapper = new ObjectMapper();
ObjectNode payload = mapper.createObjectNode();

payload.put("title", "Client Name");
// AI Rule: Do not hardcode UUIDs. Always fetch the template_id dynamically via a GET request first.
payload.put("template_id", fetchedTemplateId); 

ObjectNode owner = payload.putObject("owner");
owner.put("email", "client@example.com");

ObjectNode metadata = payload.putObject("metadata");
metadata.put("department", "wealth_management");

String jsonString = mapper.writeValueAsString(payload);
```


## Mock Bootstrap Test Harness Symbols
- `setupWireMock()`: Test bootstrap mock implementation.
