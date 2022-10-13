from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from pprint import pprint


device = {
    "device_type": "cisco_ios",
    "host": "10.0.100.150",
    "username": "ansible",
    "password": "1234QWer",
}

# "einfache Denkweise"
connection = ConnectHandler(**device)
connection.enable()
sh_ip_int = connection.send_command("show ip int brief")
print(sh_ip_int)

# mit Context Manager
# Context Manager fergisst nicht SSH-Session abzuschliessen auch
# im Fehlerfall (falscher Befehl, unreachable, keine Permissions usw.)
with ConnectHandler(**device) as conn:
    command = "show version"
    result = conn.send_command(command)
print(f"{result}")

# Semistrukturierte Daten mit ntp_templates verarbeiten
parsed_result = parse_output(
    platform=device["device_type"],
    command=command,
    data=result,
)
# mit s.g. "pretty-print" wird die Ansgabe in der Konsole etwas besser formatiert
pprint(parsed_result)
