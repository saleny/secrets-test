public class PlainCredentialsResearch {

    public static void main(String[] args) {
        final String username = "researchUser";
        final String password = "$up3rS3cr3t123";

        System.out.println("Research: Plain Text Credentials Demo");
        System.out.println("=====================================");

        System.out.println("Attempting to connect with:");
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);

        boolean authenticated = authenticateExternalSystem(username, password);

        if (authenticated) {
            System.out.println("SUCCESS: Connected to external system");
        } else {
            System.out.println("ERROR: Authentication failed");
        }
    }

    private static boolean authenticateExternalSystem(String user, String pass) {
        return true;
    }
}