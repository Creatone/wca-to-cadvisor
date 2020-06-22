import json

from wca.perf_const import PREDEFINED_RAW_EVENTS
from wca.platforms import CPUCodeName

cadvisor_perf_config = {
    "events": [],
    "custom_events": []
}

CODE_NAMES = [code_name
              for code_name in CPUCodeName
              if code_name != CPUCodeName.UNKNOWN]

for code_name in CODE_NAMES:
    for event in PREDEFINED_RAW_EVENTS:
        if code_name in PREDEFINED_RAW_EVENTS[event]:
            cadvisor_perf_config["events"].append([event])
            cadvisor_perf_config["custom_events"].append({
                "type": 4,
                "config": list(
                    hex(code) for code in
                    PREDEFINED_RAW_EVENTS[event][code_name]),
                "name": event
            })
    with open("perf-wca-%s.json" % code_name.value, "w") as f:
        f.write(json.dumps(cadvisor_perf_config, indent=4))

print("Done")
