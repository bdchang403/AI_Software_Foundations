import static com.github.tomakehurst.wiremock.client.WireMock.*;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

/**
 * SideDrawer API Mock Bootstrap using WireMock
 * Use this to verify JSON parsing and RBAC logic against a simulated SideDrawer endpoint.
 */
public class SideDrawerMockBootstrap {
    public void setupWireMock() throws Exception {
        // 1. Setup the mock response for the AI to develop against
        stubFor(get(urlEqualTo("/api/v1/organization/settings"))
            .willReturn(aResponse()
                .withStatus(200)
                .withHeader("Content-Type", "application/json")
                .withBody("{\"branding\": {\"primary_color\": \"#003366\", \"logo_url\": \"https://dev.sidedrawer.com/logo.png\"}}")));

        // 2. Local Java Client pointing to the mock (localhost:8080)
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("http://localhost:8080/api/v1/organization/settings"))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("SideDrawer Simulation: Received Mock JSON: " + response.body());
    }
}