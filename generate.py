import sys
import os
import openapiart


def generate():
    files = {
        "datamodel": ["./common/common.yaml", "./datamodel/api.yaml"],
        "fabric": ["./common/common.yaml", "./fabric/api.yaml"],
        "dataflow": ["./common/common.yaml", "./dataflow/api.yaml"],
    }
    for package_name, file_names in files.items():
        art = openapiart.OpenApiArt(
            api_files=file_names,
            protobuf_name="onex" + package_name,
            artifact_dir=os.path.join(os.path.dirname(__file__), "artifacts", package_name),
        )
        art.GeneratePythonSdk(package_name=package_name)
        if package_name == "datamodel":
            art.GenerateGoSdk(
                package_dir="github.com/open-network-experiments/onexgo",
                package_name="onexgo",
            )


if __name__ == "__main__":
    generate()
