import socket

def isIP(address):
    count = 0
    for x in address:
        if x == '.':
            count += 1
            continue
        if x.isdigit():
            continue
        else:
            return False
    if count == 3:
        return True
    else:
        return False

def main():
    hostname = raw_input("Enter Host IP or Domain Name\n")
    start_port_no = int(raw_input("Enter Start Port No.\n"))
    end_port_no = int(raw_input("Enter End Port No.\n"))
    try:
        if(isIP(hostname)):
            pass
        else:
            hostname = socket.gethostbyname(hostname)
    except socket.gaierror:
        print("There was error resolving the host")
        sys.exit()
    print("Open Ports are:")
    for i in range(start_port_no, end_port_no + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((hostname, i))
        except:
            pass
        else:
            print(i, "Success")
        sock.close()

if __name__ == "__main__":
    main()
