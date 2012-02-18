%global packname  humanStemCell
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.5
Release:          1
Summary:          Human Stem Cells time course experiment
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-Biobase R-hgu133plus2.db 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase R-hgu133plus2.db

%description
Affymetrix time course experiment on human stem cells (two time points:
undifferentiated and differentiated).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/script
