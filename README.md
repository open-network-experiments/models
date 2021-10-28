[DataModel](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdatamodel_openapi.yaml)
| [Fabric API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexfabric_openapi.yaml)
| [Dataflow API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdataflow_openapi.yaml)
# ONEx API and Data Models
This ONEx repository produces OpenAPI artifacts that describe APIs and Data Models neccessary for creating open network experiments.

# Fabric example

Here's a simple fabric example, creating a clos fabric with 1 spine, 2 pods and 1 ToR + host in each pod:


![fabric sample](/assets/sample_fabric.png)


```json
{
    "topology": {
        "choice": "spine_pod_rack",
        "spine_pod_rack": {
            "spines": [
                { 
                    "count": 1
                }
            ],
            "pods": [
                {
                    "count": 2,
                    "pod_profile_name": ["Pod Profile 1"]
                }
            ]
        }
    },
    "pod_profiles": [
        {
            "name": "Pod Profile 1",
            "pod_switch": {
                "count": 1
            },
            "rack": {
                "count": 1,
                "rack_profile_names": ["Rack Profile 1"]
            }
        }
    ],
    "rack_profiles": [
        {
            "name": "Rack Profile 1",
            "oversubscription": "2:1"
        }
    ],
    "hosts": [
        {
            "name": "Compute East",
            "ipv4_address": "1.1.1.1"
        },
        {
            "name": "Storage West",
            "ipv4_address": "2.2.2.2"
        }
    ],
}
```
