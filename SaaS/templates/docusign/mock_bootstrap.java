// DocuSign Mock API using WireMock
import static com.github.tomakehurst.wiremock.client.WireMock.*;

public class DocuSignMock {
    public void setupMock() {
        stubFor(get(urlEqualTo("/v2.1/accounts/12345/templates"))
            .willReturn(aResponse()
                .withStatus(200)
                .withHeader("Content-Type", "application/json")
                .withBody("{\"envelopeTemplates\": []}")));
    }
}
