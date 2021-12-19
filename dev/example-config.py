
import json

config = {
    'keywords': {
        'kywrd1': 'method1',
        'kywrd2': 'method2'
    },
    'methods': {
        "method1": {
            'arguments': None
        }
    },
    'group_assign': {
        'group1': {
            'method2': {
                'arguments': {
                        'flags': {
                            't': {
                                'type': 'FILE',
                                'idx': 'target_file'
                            }
                        },
                        'values': {
                            'IPADDR': 'target_ip'
                        }
                    },
                } 
            }
        }
    }


with open('cfg.json', 'w') as f:
    f.write(json.dumps(config, indent=4))