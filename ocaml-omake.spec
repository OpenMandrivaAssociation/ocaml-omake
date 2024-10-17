%define beta rc1
%define debug_package	%{nil}

Summary:	Build system with automated dependency analysis
Name:		ocaml-omake
Version:	0.9.8.6
Release:	0.%{beta}.1
License:	LGPLv2+
Group:		Development/Other
Url:		https://omake.metaprl.org/download.html
Source0:	http://omake.metaprl.org/downloads/omake-%{version}-0.%{beta}.tar.gz
Patch0:		omake-debian-disable-ocaml-warnings.patch
Patch1:		omake-0.9.8.6-fix-and-or-operators.patch
Patch2:         omake-0.9.8.6-kill-warn-error.patch
BuildRequires:	chrpath
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(ncurses)
BuildRequires: gcc-c++, gcc, gcc-cpp


Conflicts:	osh
# omake can be used on non-OCaml projects (RHBZ#548536).
Provides:	omake = %{EVRD}

%description
OMake is a build system designed for scalability and portability. It
uses a syntax similar to make utilities you may have used, but it
features many additional enhancements, including the following.

 * Support for projects spanning several directories or directory
   hierarchies.

 * Fast, reliable, automated, scriptable dependency analysis using MD5
   digests, with full support for incremental builds.

 * Dependency analysis takes the command lines into account — whenever
   the command line used to build a target changes, the target is
   considered out-of-date.

 * Fully scriptable, includes a library that providing support for
   standard tasks in C, C++, OCaml, and LaTeX projects, or a mixture
   thereof.

%files
%doc LICENSE LICENSE.OMake
%doc CHANGELOG.txt
%doc doc/txt/omake-doc.txt doc/ps/omake-doc.pdf doc/html/
%{_libdir}/omake/
%{_bindir}/omake
%{_bindir}/osh
%{_bindir}/cvs_realclean

#----------------------------------------------------------------------------

%prep
%setup -q -n omake-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CC=gcc
export CXX=g++

make all \
  PREFIX=%{_prefix} MANDIR=%{_mandir} BINDIR=%{_bindir} LIBDIR=%{_libdir}

%install
make install \
  INSTALL_ROOT=%{buildroot} \
  PREFIX=%{_prefix} MANDIR=%{_mandir} BINDIR=%{_bindir} LIBDIR=%{_libdir}

chmod 0755 %{buildroot}%{_bindir}/*

