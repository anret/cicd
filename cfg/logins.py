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

configurations = []
for i in range(1, 4):
    with open(f"cfg/csr-{i}.cfg") as f:
        contents = f.readlines()
        configurations.append(contents)

if __name__ == "__main__":
    print(configurations)
