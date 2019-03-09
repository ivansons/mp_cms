# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "mp-cms-dev"
  config.vm.define "mp_cms_dev" do |mp_cms_dev_vagrant|
  end
  config.vm.network "private_network", ip: "192.168.140.140"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "mp_cms_dev"
    vb.memory = "2048"
    vb.cpus = "2"
    vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
    vb.customize ["modifyvm", :id, "--audio", "none"]
  end
  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
  config.vm.synced_folder ".", "/mp_cms", type: "nfs"
  config.vm.provision "shell", privileged: false, path: "vagrant/provision.sh"
end
