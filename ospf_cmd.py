from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from pprint import pprint


device = {
    "device_type": "cisco_ios",
    "host": "10.0.100.150",
    "username": "ansible",
    "password": "1234QWer",
}

with ConnectHandler(**device) as conn:
    commands = [
        "show ip ospf interface brief",
        "show ip ospf database",
        "show ip ospf neighbor",
    ]
    results = []
    for cmd in commands:
        result = conn.send_command(cmd)
        results.append(result)

print(
    f"""
    ======== SHOW IP OSPF INT BRIEF ========
    {results[0]}

    ======== SHOW IP OSPF DATABASE ========
    {results[1]}

    ======== SHOW IP OSPF NEIGHBOR ========
    {results[2]}

    ======== ENDE ========
    """
)

parsed_results = {}
for i in range(len(results)):
    parsed_rslt = parse_output(
        platform=device["device_type"],
        command=commands[i],
        data=results[i],
    )
    parsed_results[commands[i]] = parsed_rslt
pprint(parsed_results)

for element in parsed_results["show ip ospf database"]:
    print(
        f"""
Beim Router ID {element['router_id']} \
fuer OSPF Process ID {element['process_id']} \
gibt es Advertising Router {element['adv_router']}\
"""
    )

print("\n\nNUR ROUTER LINK STATES")
for element in parsed_results["show ip ospf database"]:
    if element["link_count"] != "":
        print(
            f"""
Beim Router ID {element['router_id']} \
fuer OSPF Process ID {element['process_id']} \
gibt es Advertising Router {element['adv_router']}\
"""
        )
