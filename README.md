# Roswell rpm build spec

[![Fedora Copr](https://copr.fedorainfracloud.org/coprs/elts/roswell/package/roswell/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/elts/roswell/package/roswell/)

This repository is used as a spec source for building with Fedora Copr.

## Repositories available:

* Fedora 26
* Fedora 25
* CentOS 7

## Using rpm from copr

#### If you’re using a version of Linux with dnf:

    dnf copr enable elts/roswell
    dnf install roswell

you need to have `dnf-plugins-core` installed

#### If you have older distribution with yum:

    yum copr enable elts/roswell
    yum install roswell

you need to have `yum-plugin-copr` installed

#### If you are on CentOS 7:

Download a repo file from project [homepage](https://copr.fedorainfracloud.org/coprs/elts/roswell/), and place it to `/etc/yum.repos.d/` 

    yum install roswell
