// TTA SDK Mocking Example using Moq
using Moq;
using Agility.Sdk.Model;
using Agility.Sdk.Interfaces;

public class TTAMockTest {
    public void TestJobCreation() {
        var mockJobService = new Mock<IJobService>();
        mockJobService.Setup(s => s.CreateJob(it.IsAny<SessionContext>(), it.IsAny<JobIdentity>()))
                      .Returns(new JobIdentity { Id = "MOCK_JOB_123" });
        
        // Verify your logic against the mock
    }
}
