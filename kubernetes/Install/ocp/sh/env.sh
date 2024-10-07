# ip
bastion='192.168.200.1'
master1='192.168.200.11'
master2='192.168.200.12'
master3='192.168.200.13'
bootstap='192.168.200.10'
worker1='192.168.200.21'
worker2='192.168.200.22'
infra1='192.168.200.31'

# ip2
lm1=$(echo $master1 | awk -F '.' '{print $4""$5}')
lm2=$(echo $master2 | awk -F '.' '{print $4""$5}')
lm3=$(echo $master3 | awk -F '.' '{print $4""$5}')
lw1=$(echo $worker1 | awk -F '.' '{print $4""$5}')
lw2=$(echo $worker2 | awk -F '.' '{print $4""$5}')
li1=$(echo $infra1 | awk -F '.' '{print $4""$5}')
lbt=$(echo $bastion | awk -F '.' '{print $4""$5}')
lbr=$(echo $bootstap | awk -F '.' '{print $4""$5}')

# domain
sub_domain='ocp'
domain='beomzh'
TLD='local'


# hostname
host_name=$(hostname)

# habor 계정정보
REG_SECRET_INT=`echo -n 'admin:beomzh' | base64 -w0`

# oc_env
export OCP_RELEASE=4.16.10  #oc 및 openshift-install 버전과 동일
export LOCAL_REGISTRY=$(hostname):5000
export LOCAL_REPOSITORY='ocp/ocp4'
export PRODUCT_REPO='openshift-release-dev'
export LOCAL_SECRET_JSON='/root/ocp/pull-secret.json'
export RELEASE_NAME='ocp-release'
export ARCHITECTURE=x86_64
