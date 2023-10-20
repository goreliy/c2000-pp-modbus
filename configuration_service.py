import json
from pymodbus.client.sync import ModbusSerialClient
from helpers import calculate_modbus_address

def read_configuration(config):
    # Connect to Modbus device
    client = ModbusSerialClient(
        method='rtu',
        port=config['port'],
        baudrate=config['baudrate'],
        stopbits=config['stopbits'],
        parity=config['parity']
    )
    client.connect()

    # Read configuration from Modbus registers
    configuration = {}
    for zone in range(1, 256):
        ad_orion = client.read_input_registers(address=calculate_modbus_address(zone, 0)).registers[0]
        orion_shs = client.read_input_registers(address=calculate_modbus_address(zone, 1)).registers[0]
        group_pp = client.read_input_registers(address=calculate_modbus_address(zone, 2)).registers[0]
        polling_type = client.read_input_registers(address=calculate_modbus_address(zone, 3)).registers[0]
        if ad_orion != 0 or orion_shs != 0 or group_pp != 0 or polling_type != 0:
            configuration[zone] = {
                'ad_orion': ad_orion,
                'orion_shs': orion_shs,
                'group_pp': group_pp,
                'polling_type': polling_type
            }
    
    # Save configuration to zones.json
    with open('zones.json', 'w') as zones_file:
        json.dump(configuration, zones_file)

    return configuration