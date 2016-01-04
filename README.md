# simpatize-webservice

[![Build Status](https://snap-ci.com/simpatize/simpatize_webservice/branch/master/build_image)](https://snap-ci.com/simpatize/simpatize_webservice/branch/master)

*** Tech Stack ***
Language: Python 3.4
Framework: Django 1.8, Django-Rest 3.3
Data Base: Postgres 9.4
Provisioned: Ansible
Manager: Paver 1.2
CI: Snap
*******************

1. Clone this repository (`git clone https://github.com/simpatize/simpatize_webservice.git`)
2. Install vagrant (https://www.vagrantup.com/downloads.html)
3. Install ansible (https://docs.ansible.com/ansible/intro_installation.html)
4. Install virtualbox (https://www.virtualbox.org/wiki/Downloads)
5. *OPTIONAL*: If you are using Mac and never ran virtualbox in your system, you will need to repair your disk (Open 'Disk Utility', select the disk and click on 'Repair Disk Permissions'). See more details on: https://forums.virtualbox.org/viewtopic.php?f=8&t=48224
6. Execute `vagrant up` from simpatize_webservice folder for start vagrant machine
7. Execute `vagrant provision` from simpatize_webservice folder for provisioning
8. Execute `vagrant ssh` to log in the development box
9. DataBase infos: user, table and password are 'vagrant'
