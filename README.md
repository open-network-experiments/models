# ONEx 
The ONEx models repository contains vendor agnostic APIs and Data Models for creating open network experiments.

Get started with these links.
- [Go sample](#a-go-fabric-and-dataflow-script)
- [Python sample](#a-python-fabric-and-dataflow-script)
- [Documentation](#api-and-data-model-documentation)

### Getting Started with Python
Install the python API clients
```cmd
# ONEx fabric client
pip install onexfabric

# ONEx dataflow client
pip install onexdataflow
```

### A ONEx python fabric and dataflow script
```python
import onexfabric
import onexdataflow

fabric_api = onexfabric.Api()
dataflow_api = onexdataflow.Api()
```

### Getting Started with Go
Install the go API clients
```cmd
# ONEx fabric client
go get https://open-network-experiments/onexfabric

# ONEx dataflow client
go get https://open-network-experiments/onexdataflow
```
### A ONEx go fabric and dataflow script
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
