# TODO:
# - Build it from sources (sorry, -ENOTIME now and it must work today...)
#   Is it main repo? Or just atlassian mirror?
#   http://svn.atlassian.com/svn/public/contrib/common/libraries/org.randombits.source/source/trunk

### # Conditional build:
### %bcond_without	javadoc		# don't build javadoc
### %bcond_without	tests		# don't build and run tests
###
### %if "%{pld_release}" == "ti"
### %bcond_without	java_sun	# build with gcj
### %else
### %bcond_with	java_sun	# build with java-sun
### %endif
### #

%include	/usr/lib/rpm/macros.java

# Name without java- prefix. If it is application, not a library,
# just do s/srcname/name/g
%define		srcname		randombits-source
Summary:	Source
Name:		java-randombits-source
Version:	1.3.0
Release:	0.1
License:	BSD-Like
Group:		Libraries/Java
Source0:	https://maven.atlassian.com/contrib/org/randombits/source/source/1.3.0/source-%{version}.jar
# Source0-md5:	df39a2bf8c58e4983f8e003cfc125dbd
URL:		http://randombits.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
Requires:	jpackage-utils
Provides:	java(org.randombits.source)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Randombit source

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
