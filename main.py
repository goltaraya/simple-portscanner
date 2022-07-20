import socket       # CONNECT TO OTHER MACHINE USING TCP/UDP
import termcolor    # DEPLOY DIFFERENT COLORS IN TERMINAL


def scan(target, ports):
    print(termcolor.colored(f"\n[*]Starting Scan for: '{target}'", "red", attrs=["bold"]))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] {port} - Port Open", "green"))
        sock.close()
    except KeyboardInterrupt:
        print(termcolor.colored("Bye bye!!!", "yellow", attrs=["bold"]))
    except socket.gaierror:
        print(termcolor.colored("Hostname Could Not Be Resolved!!!", "red", attrs=["bold"]))
    except socket.error:
        pass


sock = socket.socket()
targets = input(termcolor.colored("[*] Enter Targets To Scan (split them by ,): ", "yellow", attrs=["bold"]))
ports = int(input(termcolor.colored("[*] How Many Ports You Want To Scan: ", "yellow", attrs=["bold"])))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets... ", "yellow", attrs=["bold"]))
    for target in targets.split(","):
        scan(target.strip(" "), ports)
else:
    scan(targets, ports)

