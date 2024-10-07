source /root/sh/env.sh

export OCP_RELEASE=4.16.10  #oc 및 openshift-install 버전과 동일
export LOCAL_REGISTRY='${host_name}:5000'
export LOCAL_REPOSITORY='ocp/ocp4'
export PRODUCT_REPO='openshift-release-dev'
export LOCAL_SECRET_JSON='/root/ocp/pull-secret.json'
export RELEASE_NAME='ocp-release'
export ARCHITECTURE=x86_64
