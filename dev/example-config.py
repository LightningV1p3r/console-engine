
import json

config = {
    'keywords': {},
    'methods': {
        "method1": {
            'arguments': None
        }
    },
    'groups': {
        'group1': {
            'method1': {
                'arguments': {
                    'required': {
                        'flags': {
                            't': {
                                'type': 'FILE',
                                'idx': 'target_file'
                            }
                        },
                        'values': {}
                    },
                    'optional': {}
                } 
            }
        }
    }
}

with open('cfg.json', 'w') as f:
    f.write(json.dumps(config, indent=4))