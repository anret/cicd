from unittest import result
from netmiko import ConnectHandler
from cfg.logins import devices, configurations

#
for device, configuration in zip(devices, configurations):
    with ConnectHandler(**device) as conn:
        cfg_result = conn.send_config_set(configuration)
        print(f'{device["host"]} wurde erfolgreich konfiguriert')
