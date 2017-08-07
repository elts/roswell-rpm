# Roswell rpm build spec

[![Fedora Copr](https://copr.fedorainfracloud.org/coprs/elts/roswell/package/roswell/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/elts/roswell/package/roswell/)

This repository is used as a spec source for building with Fedora Copr.

## Using rpm from copr

If you’re using a version of Linux with dnf:

    dnf copr enable elts/roswell

you need to have dnf-plugins-core installed

If you have older distribution with yum:

    yum copr enable elts/roswell

you need to have `yum-plugin-copr` installed

If you are on centos 7 you can download a repo file and place it to `/etc/yum.repos.d/` from project homepage.
