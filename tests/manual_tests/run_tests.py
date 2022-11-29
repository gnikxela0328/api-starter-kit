from tests import Tests

print("Signup: Beginning Test")
Tests.test_signup()
print()

print("Authenticate: Beginning Test")
Tests.test_successful_authenticate()
print()

print("Failed Authenticate: Beginning Test")
Tests.test_failed_authenticate()
print()

print("Update Credentials: Beginning Test")
Tests.test_update_credentials()
print()