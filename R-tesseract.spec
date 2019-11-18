#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tesseract
Version  : 4.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/tesseract_4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tesseract_4.1.tar.gz
Summary  : Open Source OCR Engine
Group    : Development/Tools
License  : Apache-2.0
Requires: R-tesseract-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-curl
Requires: R-digest
Requires: R-pdftools
Requires: R-rappdirs
Requires: R-spelling
Requires: R-tibble
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : R-digest
BuildRequires : R-pdftools
BuildRequires : R-rappdirs
BuildRequires : R-spelling
BuildRequires : R-tibble
BuildRequires : buildreq-R
BuildRequires : pkgconfig(tesseract)

%description
a powerful optical character recognition (OCR) engine that supports over 100 languages.
     The engine is highly configurable in order to tune the detection algorithms and
     obtain the best possible results.

%package lib
Summary: lib components for the R-tesseract package.
Group: Libraries

%description lib
lib components for the R-tesseract package.


%prep
%setup -q -c -n tesseract

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574093093

%install
export SOURCE_DATE_EPOCH=1574093093
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tesseract
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tesseract
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tesseract
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tesseract || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tesseract/AUTHORS
/usr/lib64/R/library/tesseract/COPYRIGHT
/usr/lib64/R/library/tesseract/DESCRIPTION
/usr/lib64/R/library/tesseract/INDEX
/usr/lib64/R/library/tesseract/Meta/Rd.rds
/usr/lib64/R/library/tesseract/Meta/features.rds
/usr/lib64/R/library/tesseract/Meta/hsearch.rds
/usr/lib64/R/library/tesseract/Meta/links.rds
/usr/lib64/R/library/tesseract/Meta/nsInfo.rds
/usr/lib64/R/library/tesseract/Meta/package.rds
/usr/lib64/R/library/tesseract/Meta/vignette.rds
/usr/lib64/R/library/tesseract/NAMESPACE
/usr/lib64/R/library/tesseract/NEWS
/usr/lib64/R/library/tesseract/R/tesseract
/usr/lib64/R/library/tesseract/R/tesseract.rdb
/usr/lib64/R/library/tesseract/R/tesseract.rdx
/usr/lib64/R/library/tesseract/WORDLIST
/usr/lib64/R/library/tesseract/doc/index.html
/usr/lib64/R/library/tesseract/doc/intro.R
/usr/lib64/R/library/tesseract/doc/intro.Rmd
/usr/lib64/R/library/tesseract/doc/intro.html
/usr/lib64/R/library/tesseract/help/AnIndex
/usr/lib64/R/library/tesseract/help/aliases.rds
/usr/lib64/R/library/tesseract/help/paths.rds
/usr/lib64/R/library/tesseract/help/tesseract.rdb
/usr/lib64/R/library/tesseract/help/tesseract.rdx
/usr/lib64/R/library/tesseract/html/00Index.html
/usr/lib64/R/library/tesseract/html/R.css
/usr/lib64/R/library/tesseract/tests/spelling.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tesseract/libs/tesseract.so
