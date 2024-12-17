%define major		3
%define oldlibname	%mklibname dcmtk 3
%define libname		%mklibname dcmtk
%define devname		%mklibname dcmtk -d

Name:		dcmtk
Version:	3.6.9
Release:	1
Summary:	DICOM libraries and applications
Group:		System/Libraries
License:	BSD and MIT
URL:		https://dicom.offis.de/dcmtk.php.en
Source0:	https://dicom.offis.de/download/dcmtk/dcmtk%(echo %{version} |sed -e 's,\.,,g')/dcmtk-%{version}.tar.gz
Patch0:		dcmtk-3.6.9-fix_installation_paths.patch
BuildRequires:	cmake ninja
BuildRequires:	cmake(libjpeg-turbo)
BuildRequires:	cmake(libxml2)
BuildRequires:	cmake(openssl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	wrap-devel

%description
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

DCMTK has been used at numerous DICOM demonstrations to provide central,
vendor-independent image storage and worklist servers (CTNs - Central Test
Nodes). It is used by hospitals and companies all over the world for a wide
variety of purposes ranging from being a tool for product testing to being
a building block for research projects, prototypes and commercial products.

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_datadir}/%{name}/
%{_mandir}/man1/*.1.*

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	DICOM libraries
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

This package contains shared libraries.

%files -n %{libname}
%{_libdir}/*.so.*

#-----------------------------------------------------------------------

%package -n %{devname}
Summary:	DICOM libraries development files
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}

%description -n %{devname}
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

This package contains files required for development only.

%files -n %{devname}
%license COPYRIGHT
%doc CHANGES CONTRIBUTING.md FAQ HISTORY README README.md
%doc %{_defaultdocdir}/%{name}/*
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -Wno-dev \
	-DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
	-GNinja
%ninja_build

%install
%ninja_install -C build

