import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_grafana_is_installed(host):
    cmd = host.run("apt-get update && "
                   "apt-get install -y curl && "
                   "apt-get clean")
    assert cmd.rc == 0
    cmd = host.run("curl -s localhost:3000/login | grep span")
    assert cmd.rc == 0
    pattern = re.compile("v[\\d.]+")
    assert pattern.search(cmd.stdout) != None
