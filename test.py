from MTU import MTU
cinta = '*10110-001/0010100/0110110/0101010/#'

mtu = MTU(cinta)
print(mtu.output())
mtu.execute()
print(mtu.output())