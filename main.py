from MTU import MTU
import sys

def main():

    if "-f" in sys.argv:
        with open(sys.argv[2], "r") as f:
            cinta = f.read()
    else:
        cinta = sys.argv[1]

    mtu = MTU(cinta)
    print("Initial state")
    print(mtu.output())
    mtu.execute()
    print("Final state")
    print(mtu.output())

if __name__ == "__main__":
    main()