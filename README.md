[![Python application](https://github.com/LightningV1p3r/console-engine/actions/workflows/python-app.yml/badge.svg)](https://github.com/LightningV1p3r/console-engine/actions/workflows/python-app.yml)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)]()
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/LightningV1p3r/console-engine/blob/main/LICENSE.txt)

!!!DISCLAIMER!!!
---
> ⚠️ **This tool is experimental** ⚠️ : This project currently is in early beta! The tool is extremly unstable, has a lot of unfixed bugs and currently even has no error control. **USAGE AT YOU OWN RISK**! We are currently working on getting everything properly working.


Console Engine
---

This is a simple to integrate Shell (_Metasploit like_)

Installation
---

```
pip3 install console-engine
```

Usage
---

You will have to pass a configuaration as Dictionary into the Shell instance. In the configuration you define the commands and their needed arguments.

Example config:
```python
config = {
    'keywords': {
        'help': 'help_menu',
        'exit': 'exit',
        'commandone': 'method1',
        'commandtwo': 'method2',
    },
    'methods': {
        'help_menu': {
            'arguments': None
        },
        'exit': {
            'arguments': None
        },
        'method1': {
            'arguments': {
                'flags': {
                    'i': {
                        'type': 'IPADDR',
                        'idx': 'target_ip'
                    }
                }

            }
        },
        'method2': {
            'arguments': {
                'values': {
                    'STR': 'text'
                }
            }
        }
    },
}

```
After having made the config implement console engine into your script like in this demo script:

```python
import cengine

if __name__=='__main__':

    shell_ = cengine.Shell(config, header='>> ')

    while True:

        inst, count = shell_.prompt()
        res = inst[0]
        
        if res['idx'] == 'help_menu':
            print("""
    command1 - returns given ip
    command2 - echos given str
    help - diplays this msg
    exit - terminates script    
    """)
        elif res['idx'] == 'exit':
            exit()
        elif res['idx'] == 'method1':
            print(res['data']['target_ip'])
        elif res['idx'] == 'method2':
            print(res['data']['text'])
```
 

