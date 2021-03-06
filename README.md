# grafana

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/grafana.svg)](https://github.com/codeyourinfra/grafana/releases/latest) [![Build status](https://travis-ci.org/codeyourinfra/grafana.svg?branch=master)](https://travis-ci.org/codeyourinfra/grafana) [![Ansible Role](https://img.shields.io/ansible/role/29402.svg)](https://galaxy.ansible.com/codeyourinfra/grafana) [![Ansible Role downloads](https://img.shields.io/ansible/role/d/29402.svg)](https://galaxy.ansible.com/codeyourinfra/grafana)

Ansible role to install [Grafana](https://grafana.com).

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.grafana
```

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/grafana). During the build, the role is tested by using [Molecule](https://molecule.readthedocs.io).

## Test yourself

Inside your [Python virtual environment](https://docs.python.org/3/tutorial/venv.html), run:

`pip install -r requirements.txt`

And then:

`molecule test`

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
