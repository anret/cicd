devices = [
    {
        "device_type": "cisco_ios",
        "host": "10.0.100.150",
        "username": "ansible",
        "password": "1234QWer",
    },
    {
        "device_type": "cisco_ios",
        "host": "10.0.100.151",
        "username": "ansible",
        "password": "1234QWer",
    },
    {
        "device_type": "cisco_ios",
        "host": "10.0.100.152",
        "username": "ansible",
        "password": "1234QWer",
    },
]

parameter = ["name", "ip", "sm", "descr", "status"]
phys_interfaces = [
    ["gi0/0", "10.0.0.1", "255.255.255.0", "Lan 1", "up"],
    ["gi0/1", "10.0.1.1", "255.255.255.0", "DMZ", "down"],
    ["gi0/2", "10.0.2.1", "255.255.255.0", "Intern", "up"],
    ["gi0/3", "10.0.3.1", "255.255.255.0", "Cloud", "up"],
]
logical_interfaces = [
    ["Tu0", "150.0.0.1", "255.255.255.0", "Tunnel Standort MUC", "up"],
    ["Lo0", "10.10.1.1", "255.255.255.0", "Loopback", "up"],
    ["Null0", "10.10.0.0", "255.255.255.0", "Cloud", "up"],
]


configurations = []
for i in range(1, 4):
    with open(f"cfg/csr-{i}.cfg") as f:
        contents = f.readlines()
        configurations.append(contents)

if __name__ == "__main__":
    print(configurations)
