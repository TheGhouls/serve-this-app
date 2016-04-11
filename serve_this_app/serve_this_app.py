import argparse
import socket
from subprocess import call

def get_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    addr, port = s.getsockname()
    s.close()
    return port


def main():
    parser = argparse.ArgumentParser("Serve this app ! Lunch any webapp with free port localy")
    parser.add_argument("commands", nargs='+', type=str, help="all commands without port")
    parser.add_argument("-s", "--stick", action="store_true", default=False)
    
    args = parser.parse_args()
    port = get_port()
    print("Gonna use port : %d" % port)
    if args.stick:
        args.commands[-1] += str(port)
        call(args.commands)
    else:
        call(args.commands + [str(port)])
    
