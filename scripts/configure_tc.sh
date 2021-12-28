sif=lan0
dif=dummy0
# ingress
tc qdisc add dev "$sif" ingress
tc filter add dev "$sif" parent ffff: protocol all u32 match u8 0 0 action mirred egress mirror dev "$dif"
# egress
tc qdisc add dev "$sif" handle 1: root prio
tc filter add dev "$sif" parent 1: protocol all u32 match u8 0 0 action mirred egress mirror dev "$dif"
