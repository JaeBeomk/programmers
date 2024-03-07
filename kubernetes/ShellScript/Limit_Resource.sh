#! bin/bash
# deployment별 cpu/mem Limit값과 현재값 
alias k='kubectl'

k get ns
read -p "Enter NameSpace: " ns

k get deploy -n $ns
read -p "Enter Deployment: " deploy

result=$(k get deploy $deploy -n $ns -ojson|jq '.spec.template.spec.containers[0].resources.limits')

resource_limits=$(kubectl get pods -n "$ns" -o=jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\n"}{range .spec.containers[*]}{"  "}{.name}{":\n"}{"    CPU: "}{.resources.limits.cpu}{", Memory: "}{.resources.limits.memory}{"\n"}{end}{end}'|grep -A4 $deploy)
# $1,2,3,4,5

echo "$resource_limits" | head -n 5

Lcpu=$(echo "$result" | jq -r '.cpu')
Lmem=$(echo "$result" | jq -r '.memory')

# Gi -> Mi 변환
if echo "$Lmem" | grep -q "Gi"; then
    l1=$(echo "$Lmem" | sed 's/Gi//')
    l2=$((l1 * 1024))
    Lmem1="${l2}Mi"
else
    Lmem1=$Lmem
fi

if echo "$Lcpu" | grep -q "m"; then
    Lcpu1=$Lcpu
else
    Lcpu1=$((Lcpu * 1000))
fi
# echo "$Lcpu,$Lmem"

top=$(k top pods -n $ns --containers |grep $deploy)

while IFS= read -r line; do
    pod_name=$(echo "$line" | awk '{print $1}')
    containers_name=$(echo "$line" | awk '{print $2}')
    cpu_usage=$(echo "$line" | awk '{print $3}')
    memory_usage=$(echo "$line" | awk '{print $4}')
    if echo "$containers_name"| grep -q "$deploy"; then
        PercnetMem=$Lmem
        PercnetCPU=$LCPU
    else
        PercnetCPU="2000"
        PercnetMem="512Mi"
    fi
    echo "$pod_name - $containers_name CPU Usage: $cpu_usage/$PercnetCPU, Memory Usage: $memory_usage/$PercnetMem"
done <<< "$top"