from netmiko import ConnectHandler
from cfg.logins import devices


def speichern(filename, content):
    with open(filename, "w") as f:
        f.write(content)


for device in devices:
    with ConnectHandler(**device) as conn:
        command = "show run"
        result = conn.send_command(command)
        speichern(f'cfg/{device["host"]}_running-config.cfg', result)

print("Alle Konfigurationen wurden erfolgreich gespeichert")
