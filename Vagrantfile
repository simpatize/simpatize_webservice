# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define :simpatize do |simpatize|
    simpatize.vm.box = 'ubuntu/trusty64'
    simpatize.vm.network 'forwarded_port', guest: 8000, host: 8080
    simpatize.vm.network 'forwarded_port', guest: 5432, host: 5432
    simpatize.vm.provision 'ansible' do |ansible|
      ansible.sudo = true
      ansible.playbook = 'provisioning/playbook.yml'
    end

    simpatize.vm.provider 'virtualbox' do |v|
      v.memory = 2048
    end
  end
end
