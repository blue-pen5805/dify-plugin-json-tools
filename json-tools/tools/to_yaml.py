from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import json
import yaml

class ToYamlTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        json_string: str = tool_parameters.get("json_string")

        try:
            json_object = json.loads(json_string)

            yield self.create_text_message(yaml.dump(json_object))
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {str(e)}")
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
