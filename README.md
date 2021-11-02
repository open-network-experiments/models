[![CICD](https://github.com/open-network-experiments/models/workflows/CICD/badge.svg)](https://github.com/open-network-experiments/models/actions)

[DataModel](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdatamodel_openapi.yaml)
| [Fabric API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexfabric_openapi.yaml)
| [Dataflow API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdataflow_openapi.yaml)
# ONEx API and Data Models
This ONEx repository produces OpenAPI artifacts that describe APIs and Data Models neccessary for creating open network experiments.

# Fabric example

Here's a simple fabric example, creating a clos fabric with 1 spine, 2 pods and 1 ToR + host in each pod:

<p align="center">
    <img src="./assets/sample_fabric.png" />
</p>

Click on language/format node to expand the sample!

<details><summary>JSON</summary>
<p>

```json
{
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
                "pod_profile_name": [ "Pod Profile 1" ]
            }
        ],
        "pod_profiles": [
            {
                "name": "Pod Profile 1",
                "pod_switch": {
                    "count": 1
                },
                "rack": {
                    "count": 2,
                    "rack_profile_names": [ "Rack Profile 1" ]
                }
            }
        ],
        "rack_profiles": [
            {
                "name": "Rack Profile 1",
                "tor_to_pod_oversubscription": "2:1"
            }
        ]
    }
}
```
</p>
</details>

<details><summary>yaml</summary>
<p>


```yaml
choice: spine_pod_rack
spine_pod_rack:
  spines:
  - count: 1
  pods:
  - count: 2
    pod_profile_name:
    - Pod Profile 1
  pod_profiles:
  - name: Pod Profile 1
    pod_switch:
      count: 1
    rack:
      count: 2
      rack_profile_names:
      - Rack Profile 1
  rack_profiles:
  - name: Rack Profile 1
    tor_to_pod_oversubscription: '2:1'
```
</p>
</details>


<details><summary>Python</summary>
<p>

```python
def fabric_sample():
    config = onex.api().config()
    config.fabric.spine_pod_rack.spines.add(count=1)
    config.fabric.spine_pod_rack.pods.add(
        count=2,
        pod_profile_name=["Pod Profile 1"]
    )

    pod_profile = config.fabric.spine_pod_rack.pod_profiles.add(name="Pod Profile 1")
    pod_profile.pod_switch.count = 1
    rack_profile = config.fabric.spine_pod_rack.rack_profiles.add(
        name="Rack Profile 1",
        tor_to_pod_oversubscription="2:1"
    )
    pod_profile.rack.rack_profile_names = [ rack_profile.name ]
    pod_profile.rack.count = 2
```
</p>
</details>

