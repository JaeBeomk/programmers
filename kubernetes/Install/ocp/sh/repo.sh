cat <<EOF > /etc/yum.repos.d/local.repo
[local_BaseOS]
name=local_BaseOS
baseurl=file:///mnt/BaseOS/
enabled=1
gpgcheck=0
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

[local_AppStream]
name=local_AppStreammo
baseurl=file:///mnt/AppStream
enabled=1
gpgcheck=0
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
EOF

mount /dev/sr0 /mnt
