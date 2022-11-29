
class TestUtil():
    def check_status(actual, expected):
        try:
            assert actual == expected
        except:
            print("Bad status code")
            print("Returned status code: " + str(actual))

    def check_message(actual, expected):
        try:
            assert actual == expected
        except:
            print("Bad response")
            print("Returned response: " + str(actual))

    def check_any(actual, key):
        try:
            assert any(actual)
        except:
            print("Bad response")
            print("Returned None for: " + str(key))