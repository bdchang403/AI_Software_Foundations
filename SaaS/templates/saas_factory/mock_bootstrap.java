import static org.mockito.Mockito.*;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;

/**
 * Generic SaaS Factory Mock Bootstrap
 * Use this as a starting point to mock ANY SaaS SDK or REST API.
 */
public class GenericSaaSMLock {
    public void simulateSaaSLogic() throws Exception {
        // Option A: Mocking an SDK Class (Mockito)
        // SomeSaaSSDK api = mock(SomeSaaSSDK.class);
        // when(api.getStatus()).thenReturn("SUCCESS");

        // Option B: Mocking an HTTP Response (Java 11 HttpClient)
        HttpResponse<String> mockResponse = mock(HttpResponse.class);
        when(mockResponse.body()).thenReturn("{\"status\": \"operational\"}");
        when(mockResponse.statusCode()).thenReturn(200);

        System.out.println("Generic Simulation: Mock Response Body: " + mockResponse.body());
    }
}
