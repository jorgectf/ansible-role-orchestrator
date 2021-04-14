"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "directory",
    [
        {"path": "/var/cyhy/orchestrator", "mode": "0o755"},
        {"path": "/var/cyhy/orchestrator/output", "mode": "0o755"},
    ],
)
def test_directories(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    if "mode" in directory:
        assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize("f", ["/var/cyhy/orchestrator/docker-compose.yml"])
def test_command(host, f):
    """Test that appropriate files exist."""
    assert host.file(f).exists
    assert host.file(f).is_file
