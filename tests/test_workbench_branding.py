import dogpile


def test_workbench_branding_is_available():
    assert dogpile.WORKBENCH_NAME == "Dogpile Cache Workbench"
    assert dogpile.WORKBENCH_VERSION.endswith("+workbench.1")
    assert dogpile.WORKBENCH_SOURCE_URL.endswith("/dogpile-cache-workbench")
