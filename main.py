import sys
import json
from configuration_service import read_configuration
from database import initialize_database
#from zone_state_service import poll_zone_state
#from event_processing_service import process_event

def main():
    # Read config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    # Initialize database
    initialize_database()

    # Read configuration
    configuration = read_configuration(config)

    # Poll zone state
    poll_zone_state(config, configuration)

    # Process event
    process_event(config, configuration)

if __name__ == '__main__':
    main()