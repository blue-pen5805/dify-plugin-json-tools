from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import json

class JsonDumpsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        json_object: dict = tool_parameters.get("json_object")

        try:
            json_string = json.dumps(json_object)

            yield self.create_json_message(json_string)
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
