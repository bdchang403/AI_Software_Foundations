# DocuSign SDK Constraints Registry

You MUST use the official `docusign-esign-java` SDK. Do NOT use raw HTTP requests or the legacy SOAP API.

## JWT Authentication Flow
```java
// Copilot MUST use this exact JWT Grant flow boilerplate for authentication in Java:
ApiClient apiClient = new ApiClient("https://demo.docusign.net/restapi");
byte[] privateKeyBytes = Files.readAllBytes(Paths.get("private.key"));
List<String> scopes = Arrays.asList("signature", "impersonation");

OAuth.OAuthToken oAuthToken = apiClient.requestJWTUserToken(
    System.getenv("CLIENT_ID"),
    System.getenv("USER_ID"),
    scopes,
    privateKeyBytes,
    3600
);

apiClient.addDefaultHeader("Authorization", "Bearer " + oAuthToken.getAccessToken());
```
