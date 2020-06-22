from wca.perf_const import PREDEFINED_RAW_EVENTS
from wca.platforms import CPUCodeName
import json

cadvisor_perf_config = {
    "events": [],
    "custom_events": []
}

code_name = CPUCodeName.SKYLAKE

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

with open("perf-wca.json", "w") as f:
    f.write(json.dumps(cadvisor_perf_config))

