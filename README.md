[![CICD](https://github.com/open-network-experiments/models/workflows/CICD/badge.svg)](https://github.com/open-network-experiments/models/actions)

[DataModel](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdatamodel_openapi.yaml)
| [Fabric API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexfabric_openapi.yaml)
| [Dataflow API](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/open-network-experiments/models/main/docs/onexdataflow_openapi.yaml)
# ONEx API and Data Models
This ONEx repository produces OpenAPI artifacts that describe APIs and Data Models neccessary for creating open network experiments.

# Fabric example

Here's a simple fabric example, creating a clos fabric with 1 spine, 2 pods and 1 ToR in each pod:

<p align="center">
    <img src="./assets/sample_fabric.png" />
</p>

Click on language/format node to expand the sample!

<details><summary>Json</summary>
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

<details><summary>Yaml</summary>
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



# Dataflow example

Below is a simple scatter-gather dataflow example:

<p align="center">
    <img src="./assets/sample_dataflow.png" />
</p>

<details><summary>Json</summary>
<p>

```json
{
    "dataflow": {
        "flow_profiles": [
            {
                "name": "data transfer",
                "data_size": 1073741824
            }
        ],
        "workload": [
            {
                "name": "Scatter",
                "choice": "scatter",
                "scatter": {
                    "destinations": [
                        "Compute 1",
                        "Compute 2"
                    ],
                    "flow_profile_name": "data transfer",
                    "sources": [
                        "Aggregator"
                    ]
                }
            },
            {
                "name": "Gather",
                "choice": "gather",
                "gather": {
                    "destinations": [
                        "Aggregator"
                    ],
                    "flow_profile_name": "data transfer",
                    "sources": [
                        "Compute 1",
                        "Compute 2"
                    ]
                }
            }
        ]
    },
    "hosts": [
        {
            "name": "Aggregator",
            "address": "1.1.1.1"
        },
        {
            "name": "Compute 1",
            "address": "3.3.3.3"
        },
        {
            "name": "Compute 2",
            "address": "4.4.4.4"
        }
    ]
}
```
</p>
</details>

<details><summary>Yaml</summary>
<p>


```yaml
dataflow:
  flow_profiles:
  - name: data transfer
    data_size: 1073741824
  workload:
  - name: Scatter
    choice: scatter
    scatter:
      destinations:
      - Compute 1
      - Compute 2
      flow_profile_name: data transfer
      sources:
      - Aggregator
  - name: Gather
    choice: gather
    gather:
      destinations:
      - Aggregator
      flow_profile_name: data transfer
      sources:
      - Compute 1
      - Compute 2
hosts:
- name: Aggregator
  address: 1.1.1.1
- name: Compute 1
  address: 3.3.3.3
- name: Compute 2
  address: 4.4.4.4
```
</p>
</details>


<details><summary>Python</summary>
<p>

```python
def dataflow_sample():
    api = onex.api()
    config = api.config()
    aggregator = config.hosts.add(name="Aggregator", address="1.1.1.1")    
    compute1 = config.hosts.add(name="Compute 1", address="3.3.3.3")
    compute2 = config.hosts.add(name="Compute 2", address="4.4.4.4")
    data_transfer = config.dataflow.flow_profiles.add(name='data transfer', data_size=1*1024*1024*1024)
    
    scatter = config.dataflow.workload.add(name="Scatter").scatter
    scatter.sources = [ aggregator.name ]
    scatter.destinations = [ compute1.name, compute2.name ]
    scatter.flow_profile_name = data_transfer.name

    gather = config.dataflow.workload.add(name="Gather").gather
    gather.sources = [ compute1.name, compute2.name ]
    gather.destinations = [ aggregator.name ]
    gather.flow_profile_name = data_transfer.name 

    api.set_config(config)
    api.run_experiment(api.experiment_request())
    jct = api.get_metrics(api.metrics_request()).jct
    print (f"Experiment complete, JCT: {jct}")
 ```
</p>
</details>


# Contributing

The open-network-experiment organization welcomes new members to join this open source community project and contribute to its development.