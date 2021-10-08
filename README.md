# ONEX (open network experiments)
This repository contains vendor agnostic data models for creating open network experiments.

Get started with these links.
- [Go sample](#a-go-fabric-and-dataflow-script)
- [Python sample](#a-python-fabric-and-dataflow-script)
- [Documentation](#api-and-data-model-documentation)

### Getting Started with Python
Install the python API clients
```cmd
# ONEX fabric client
pip install onexfabric

# ONEX dataflow client
pip install onexdataflow
```

### A python fabric and dataflow script
```python
import onexfabric
import onexdataflow

fabric_api = onexfabric.Api()
dataflow_api = onexdataflow.Api()
```

### Getting Started with Go
Install the go API clients
```cmd
# ONEX fabric client
go get https://open-network-experiments/onexfabric

# ONEX dataflow client
go get https://open-network-experiments/onexdataflow
```
### A go fabric and dataflow script
```go
package main

func main() {
    fabricApi = onexfabric.Api()
    for i = 1; i < 6; i++ {
        fabricApi.Hosts().Add().
            SetName(fmt.Sprintf("HOST-%i", i)).
            SetLocation(fmt.Sprintf("1.1.1.%i", i))
    }
    dataflowApi = onexdataflow.Api()
}
```
### API and Data Model Documentation
- [Fabric API and Data Model Documentation](https://open-network-experiments/fabric_openapi.html)
- [Dataflow API and Data Model Documentation](https://open-network-experiments/dataflow_openapi.html)
