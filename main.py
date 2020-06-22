import json

from wca.perf_const import PREDEFINED_RAW_EVENTS
from wca.perf_uncore import UNCORE_IMC_EVENTS
from wca.platforms import CPUCodeName


uncore_config = {
    "events": [],
    "custom_events": []
}

CODE_NAMES = [code_name
              for code_name in CPUCodeName
              if code_name != CPUCodeName.UNKNOWN]

for event in UNCORE_IMC_EVENTS:
    event_name = "uncore_imc/{}".format(event.name.lower().replace("platform_", ""))
    uncore_config["events"].append([event_name])
    uncore_config["custom_events"].append({
        "config": [
            hex(UNCORE_IMC_EVENTS[event].event),
            hex(UNCORE_IMC_EVENTS[event].umask)
        ],
        "name": event_name
    })

for code_name in CODE_NAMES:
    config = {
        "core": {
            "events": [],
            "custom_events": []
        },
        "uncore": uncore_config
    }
    for event in PREDEFINED_RAW_EVENTS:
        if code_name in PREDEFINED_RAW_EVENTS[event]:
            event_name = event.replace("task_", "")
            config["core"]["events"].append([event_name])
            config["core"]["custom_events"].append({
                "type": 4,
                "config": list(
                    hex(code) for code in
                    PREDEFINED_RAW_EVENTS[event][code_name]),
                "name": event_name
            })

    with open("perf-wca-%s.json" % code_name.value, "w") as f:
        f.write(json.dumps(config, indent=4))

print("Done")
