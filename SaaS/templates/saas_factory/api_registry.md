# [SaaS Name] Tool & SDK Registry

You MUST use these specific patterns when interacting with the [SaaS Name] platform via Java. Do not invent unauthorized API endpoints.

## Authentication Boilerplate
```java
// Use this exact pattern for authentication via Java HttpClient. Do not use Basic Auth.
HttpClient client = HttpClient.newHttpClient();
HttpRequest authRequest = HttpRequest.newBuilder()
    .uri(URI.create("https://api.saas-platform.com/oauth/token"))
    .header("Content-Type", "application/x-www-form-urlencoded")
    .POST(HttpRequest.BodyPublishers.ofString(
        "grant_type=client_credentials&client_id=" + System.getenv("CLIENT_ID") + 
        "&client_secret=" + System.getenv("CLIENT_SECRET")
    ))
    .build();

HttpResponse<String> response = client.send(authRequest, HttpResponse.BodyHandlers.ofString());
```
