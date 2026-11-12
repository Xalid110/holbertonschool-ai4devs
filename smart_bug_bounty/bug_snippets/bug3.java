import java.util.List;

public class UserRoleChecker {

    public static boolean hasAdminAccess(List<String> roles, String requiredRole) {
        if (roles.isEmpty() || requiredRole == null) {
            return false;
        }

        for (String role : roles) {
            if (role == requiredRole) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        List<String> userRoles = List.of("editor", new String("admin"));
        System.out.println("Is Admin: " + hasAdminAccess(userRoles, "admin"));
    }
}
