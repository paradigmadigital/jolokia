Jolokia
=========

Install jolokia, a war binary that provides a REST api to interact with the JVM memory and a Python script (pyjolokia) that when executed returns the RAM used by the JVM and how many it can use.

Role Variables
--------------

* `deploy_dir`: Path where to deploy the jar file.
* `jolokia_version`: Which jolokia version you want to install. [Default: 1.3.6]
* `jolokia_url`: Url to download the jar. [Default: set to the url]

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: jolokia }

License
-------

GPL3
