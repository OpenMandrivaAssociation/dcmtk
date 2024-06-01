%define major		3
%define oldlibname	%mklibname dcmtk 3
%define libname		%mklibname dcmtk
%define develname	%mklibname dcmtk -d

Name:		dcmtk
Version:	3.6.7
Release:	2
Summary:	DICOM libraries and applications
Group:		System/Libraries
License:	BSD and MIT
URL:		http://dicom.offis.de/dcmtk.php.en
Source0:	https://dicom.offis.de/download/dcmtk/dcmtk%(echo %{version} |sed -e 's,\.,,g')/dcmtk-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	tiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	wrap-devel
BuildRequires:	pkgconfig(libjpeg)

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

%package -n %{develname}
Summary:	DICOM libraries development files
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}

%description -n %{develname}
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing
and converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers. DCMTK is is written in a mixture of ANSI C and C++.
It comes in complete source code and is made available as "open source"
software.

This package contains files required for development only.

%prep
%setup -q

%build
%cmake
%make_build

%install
pushd build
%makeinstall_std
popd

mv %{buildroot}%{_prefix}/etc %{buildroot}/

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_datadir}/dcmtk
%{_mandir}/man1/cda2dcm.1.*
%{_mandir}/man1/dcm2json.1.*
%{_mandir}/man1/dcm2pdf.1.*
%{_mandir}/man1/dcm2pnm.1.*
%{_mandir}/man1/dcm2xml.1.*
%{_mandir}/man1/dcmcjpeg.1.*
%{_mandir}/man1/dcmcjpls.1.*
%{_mandir}/man1/dcmconv.1.*
%{_mandir}/man1/dcmcrle.1.*
%{_mandir}/man1/dcmdjpeg.1.*
%{_mandir}/man1/dcmdjpls.1.*
%{_mandir}/man1/dcmdrle.1.*
%{_mandir}/man1/dcmdspfn.1.*
%{_mandir}/man1/dcmdump.1.*
%{_mandir}/man1/dcmftest.1.*
%{_mandir}/man1/dcmgpdir.1.*
%{_mandir}/man1/dcmicmp.1.*
%{_mandir}/man1/dcmj2pnm.1.*
%{_mandir}/man1/dcml2pnm.1.*
%{_mandir}/man1/dcmmkcrv.1.*
%{_mandir}/man1/dcmmkdir.1.*
%{_mandir}/man1/dcmmklut.1.*
%{_mandir}/man1/dcmodify.1.*
%{_mandir}/man1/dcmp2pgm.1.*
%{_mandir}/man1/dcmprscp.1.*
%{_mandir}/man1/dcmprscu.1.*
%{_mandir}/man1/dcmpschk.1.*
%{_mandir}/man1/dcmpsmk.1.*
%{_mandir}/man1/dcmpsprt.1.*
%{_mandir}/man1/dcmpsrcv.1.*
%{_mandir}/man1/dcmpssnd.1.*
%{_mandir}/man1/dcmqridx.1.*
%{_mandir}/man1/dcmqrscp.1.*
%{_mandir}/man1/dcmqrti.1.*
%{_mandir}/man1/dcmquant.1.*
%{_mandir}/man1/dcmrecv.1.*
%{_mandir}/man1/dcmscale.1.*
%{_mandir}/man1/dcmsend.1.*
%{_mandir}/man1/dcmsign.1.*
%{_mandir}/man1/dcod2lum.1.*
%{_mandir}/man1/dconvlum.1.*
%{_mandir}/man1/drtdump.1.*
%{_mandir}/man1/dsr2html.1.*
%{_mandir}/man1/dsr2xml.1.*
%{_mandir}/man1/dsrdump.1.*
%{_mandir}/man1/dump2dcm.1.*
%{_mandir}/man1/echoscu.1.*
%{_mandir}/man1/findscu.1.*
%{_mandir}/man1/getscu.1.*
%{_mandir}/man1/img2dcm.1.*
%{_mandir}/man1/movescu.1.*
%{_mandir}/man1/pdf2dcm.1.*
%{_mandir}/man1/stl2dcm.1.*
%{_mandir}/man1/storescp.1.*
%{_mandir}/man1/storescu.1.*
%{_mandir}/man1/termscu.1.*
%{_mandir}/man1/wlmscpfs.1.*
%{_mandir}/man1/xml2dcm.1.*
%{_mandir}/man1/xml2dsr.1.*

%doc %{_defaultdocdir}/dcmtk/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/dcmtk/
%{_libdir}/cmake/dcmtk/DCMTKConfig.cmake
%{_libdir}/cmake/dcmtk/DCMTKConfigVersion.cmake
%{_libdir}/cmake/dcmtk/DCMTKTargets.cmake
%{_libdir}/cmake/dcmtk/DCMTKTargets-*.cmake
%{_libdir}/pkgconfig/dcmtk.pc
