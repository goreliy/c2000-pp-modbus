def calculate_modbus_address(zone, field):
    return ((zone - 1) * 4) + field