# Getting Started with Go

### Install the go API clients
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
