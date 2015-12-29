# Simpatize Webservice

[![Build Status](https://snap-ci.com/simpatize/simpatize_webservice/branch/master/build_image)](https://snap-ci.com/simpatize/simpatize_webservice/branch/master)
## Description
TO-DO
## Tech Stack
* python-3.4
* django-rest
## Setup develop environment
### Dependencies
* Virtualbox (https://www.virtualbox.org/wiki/Downloads)
* Vagrant (https://www.vagrantup.com/downloads.html)
* Ansible (https://docs.ansible.com/ansible/intro_installation.html)
### Install
* Clone this repository
```sh
$ git clone https://github.com/simpatize/simpatize_webservice.git && cd simpatize_webservice
```
* Start the virtual machine
```sh
$ vagrant up
```
* Provision the machine
```sh
vagrant provision
```
* Log in the development box
```sh
vagrant ssh
```
* DataBase infos: user, table and password are 'vagrant'

*OPTIONAL*: If you are using Mac and never ran virtualbox in your system, you will need to repair your disk (Open 'Disk Utility', select the disk and click on 'Repair Disk Permissions'). See more details on: https://forums.virtualbox.org/viewtopic.php?f=8&t=48224