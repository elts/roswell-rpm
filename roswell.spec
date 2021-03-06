Name:    roswell
Version: 17.10.10.85
Release: 1%{?dist}
Summary: Common Lisp environment setup Utility
URL:     https://github.com/roswell/roswell
License: MIT

Source0: https://github.com/roswell/roswell/archive/v%{version}.tar.gz
BuildRequires: automake, libcurl-devel

%description
Roswell is a Lisp implementation installer/manager, launcher, and much more!
Roswell has now evolved into a full-stack environment for Common Lisp
development, and has many features that makes it easy to test, share, and
distribute your Lisp applications.

%prep
%autosetup

%build
sh bootstrap
%configure
%make_build

%install
%make_install

%files
%license COPYING
%attr(0755, -, -) /etc/%{name}/*.ros
# Not setting 'noreplace' as these files not meant to be edited by hand
# and will be replaced on update with high probability.
%config /etc/%{name}/*.lisp
%config /etc/%{name}/*.el
%{_bindir}/ros
%{_mandir}/man1/ros*

%changelog
* Mon Nov 22 2017 Eldar Tsraev <elts@culab.org> - 17.10.10.85-1
- New upstream version: 17.10.10.85

* Mon Nov 22 2017 Eldar Tsraev <elts@culab.org> - 17.10.10.84-1
- New upstream version: 17.10.10.84

* Mon Oct 16 2017 Eldar Tsraev <elts@culab.org> - 17.10.10.83-1
- New upstream version: 17.10.10.83

* Mon Sep 04 2017 Eldar Tsraev <elts@culab.org> - 17.8.9.81-1
- New upstream version: 17.8.9.81

* Mon Aug 07 2017 Eldar Tsraev <elts@culab.org> - 17.7.9.80-1
- Initital Spec file

