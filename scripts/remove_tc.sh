sif=lan0
dif=dummy0
tc qdisc del dev "$sif" ingress
tc qdisc del dev "$sif" root
