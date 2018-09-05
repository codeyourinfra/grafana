# grafana

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/grafana.svg)]() [![Build status](https://travis-ci.org/codeyourinfra/grafana.svg?branch=master)](https://travis-ci.org/codeyourinfra/grafana)

Ansible role to install [Grafana](https://grafana.com).

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.grafana
```

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/grafana). During the build, the role is tested by using [Ubuntu Docker images with Python 3](https://hub.docker.com/r/codeyourinfra/python3).

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
