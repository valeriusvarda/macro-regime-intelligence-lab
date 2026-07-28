from importlib.metadata import version

import macro_regime_intelligence_lab as package


DISTRIBUTION_NAME = "macro-regime-intelligence-lab"
IMPORT_PACKAGE_NAME = "macro_regime_intelligence_lab"

EXPECTED_DISTRIBUTION_VERSION = "0.1.0"


def test_distribution_version_contract() -> None:
    assert version(DISTRIBUTION_NAME) == EXPECTED_DISTRIBUTION_VERSION


def test_import_package_identity() -> None:
    assert package.__name__ == IMPORT_PACKAGE_NAME
