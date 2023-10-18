#!/usr/local/autopkg/python
from autopkglib import Processor, ProcessorError
import re

__all__ = ["FilenameVersioner"]

class FilenameVersioner(Processor):
    input_variables = {
        "pathname": {
            "required": True,
            "description": "Path to a file. Can be a glob style path such as /path/to/download/*.dmg.",
        },
    }
    output_variables = {
        "version": {
            "description": "Version of the item.",
        },
    }

    description = __doc__

    def main(self):
        path = self.env["pathname"]
        filename = path.split("/")[-1]  # extract the filename from the path
        version_regex = r"(\d+\.\d+(\.\d+)*)"
        match = re.search(version_regex, filename)

        if match:
            self.env["version"] = match.group(1)
        else:
            raise ProcessorError("Unable to extract version from filename.")

if __name__ == "__main__":
    PROCESSOR = FilenameVersioner()
    PROCESSOR.execute_shell()
