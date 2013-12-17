# -*- coding: utf-8 -*-
import os
import sys
import imp
import plistlib


here = os.path.dirname(__file__)


def load_wflow():
    wflow = plistlib.readPlist(os.path.join(here, 'Show Time in Local Time Zone.workflow', 'Contents', 'document.wflow'))
    source = wflow['actions'][0]['action']['ActionParameters']['COMMAND_STRING']
    module = imp.new_module('wflow')
    exec source in module.__dict__    
    sys.modules['wflow'] = module


testcases = [
    ('', (0, 0), None),
    ('aaaaa', (0, 0), None),
    ('0:0', (1, 0), (0, 0)),
    ('2:0', (1, 0), (2, 0)),
    ('2:10', (1, 0), (2, 10)),
    ('0am', (1, 0), (0, 0)),
    ('2am', (1, 0), (2, 0)),
    ('0pm', (1, 0), (12, 0)),
    ('2pm', (1, 0), (14, 0)),
    ('2PM', (1, 0), (14, 0)),
    ('0:0 PST', (0, 0), (8, 0)),
    ('0am PST', (0, 0), (8, 0)),
    ('0am PST', (1, 0), (9, 0)),
    ('0am PST', (-13, 0), (19, 0)),
    ('1am PST', (-13, 0), (20, 0)),
    ('0pm PST', (0, 0), (20, 0)),
    ('0pm PST', (1, 0), (21, 0)),
    ('0pm PST', (-13, 0), (7, 0)),
    ('1pm PST', (-13, 0), (8, 0)),
    ('0:0 am PST', (0, 0), (8, 0)),
    ('0:0am PST', (0, 0), (8, 0)),
    ('0:0AM PST', (0, 0), (8, 0)),
    ('0:0 pm PST', (0, 0), (20, 0)),
    ('0:0pm PST', (0, 0), (20, 0)),
    ('0:0PM PST', (0, 0), (20, 0)),
]


def to_seconds(hour, minute):
    return (hour * 3600 + minute * 60)


def run_test():
    import wflow
    for i, (time_str, offset, expected) in enumerate(testcases):
        local_seconds, _ = wflow.to_local_time(time_str, to_seconds(*offset))
        assert local_seconds == (to_seconds(*expected) if expected else None), (wflow.format_seconds(local_seconds), testcases[i])


if __name__ == '__main__':
    load_wflow()
    run_test()
