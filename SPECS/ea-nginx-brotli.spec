Name:           ea-nginx-brotli
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 2
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Enable brotli config for ea-nginx
License:        2-clause BSD-like license
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       ea-nginx >= 1.21.6-7

Source0:        brotli.conf
Source1:        ngx_brotli_module.conf

%description
Makes ea-nginx configure brotli compression.

per NGINX (http://nginx.org/en/docs/http/ngx_http_gzip_module.html):
    - When using the SSL/TLS protocol, compressed responses may be subject to BREACH attacks.
    - https://en.wikipedia.org/wiki/BREACH
The best mitigation (besides not using compression at all) is:
    1. Not sending sensitive data as part of your HTTP response
    2. Use strict samesite cookies
       - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite

If that is not an acceptable risk please uninstall `ea-nginx-brotli`

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/etc/nginx/conf.d/modules
install %{SOURCE0} %{buildroot}/etc/nginx/conf.d/brotli.conf
install %{SOURCE1} %{buildroot}/etc/nginx/conf.d/modules/ngx_brotli_module.conf

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%config(noreplace) /etc/nginx/conf.d/brotli.conf
/etc/nginx/conf.d/modules/ngx_brotli_module.conf

%changelog
* Mon Apr 11 2022 Dan Muey <dan@cpanel.net> - 1.0-2
- ZC-9902: remove conflict w/ gzip

* Thu Feb 24 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9697: Initial version
