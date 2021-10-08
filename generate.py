import sys
import os
import openapiart


def generate():
    files = {
        # "fabric": ["./models/common.yaml", "./models/fabric/api.yaml"],
        "dataflow": ["./models/common.yaml", "./models/dataflow/api.yaml"],
    }
    for package_name, file_names in files.items():
        art = openapiart.OpenApiArt(
            api_files=file_names,
            protobuf_name=package_name + "pb",
            artifact_dir=os.path.join(os.path.dirname(__file__), package_name),
        )
        art.GeneratePythonSdk(package_name=package_name)
        art.GenerateGoSdk(
            package_dir="github.com/ajbalogh/distributed-system-emulation/go{}".format(package_name),
            package_name="go" + package_name,
        )


if __name__ == "__main__":
    generate()
