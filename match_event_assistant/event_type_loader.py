import yaml


class EventTypeLoader:
    def __init__(self, yaml_path="event_types.yaml"):
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        self.name_to_code = {et["name"]: et["code"] for et in data["event_types"]}
        self.code_to_name = {et["code"]: et["name"] for et in data["event_types"]}

    def validate(self, event_type, event_type_id):
        if event_type not in self.name_to_code:
            raise ValueError(f"Invalid event_type: {event_type}")
        if event_type_id != self.name_to_code[event_type]:
            raise ValueError(
                f"event_type_id {event_type_id} does not match event_type {event_type}"
            )
        return True
