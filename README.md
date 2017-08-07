# Roswell rpm build spec

This repository is used as a spec source for building with https://copr.fedorainfracloud.org

## Using rpm from copr

1. If you’re using a version of Linux with dnf:

    dnf copr enable user/project

* you need to have dnf-plugins-core installed

2. If you have older distribution with yum:

    yum copr enable user/project
    
* you need to have `yum-plugin-copr` installed

3. If you are on centos 7 you can download a repo file and place it to `/etc/yum.repos.d/`
