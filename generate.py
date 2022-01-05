import sys
import os
import openapiart


def generate():
    files = {
        "model": ["./common/common.yaml", "./model/api.yaml"],
        "fabricapi": ["./common/common.yaml", "./fabric-api/api.yaml"],
        "dataflowapi": ["./common/common.yaml", "./dataflow-api/api.yaml"],
    }
    for package_name, file_names in files.items():
        art = openapiart.OpenApiArt(
            api_files=file_names,
            protobuf_name="onex" + package_name, # must not contain '-'
            artifact_dir=os.path.join(os.path.dirname(__file__), "artifacts", f"onex_{package_name}"),
        )
        art.GeneratePythonSdk(package_name=f"onex_{package_name}")
        art.GenerateGoSdk(
            package_dir=f"github.com/open-network-experiments/onexgo{package_name}",
            package_name=f"onexgo{package_name}",
        )


if __name__ == "__main__":
    generate()
