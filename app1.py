from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
ret1 = v1.list_service_for_all_namespaces(watch=False)
#print(ret1)
for i in ret1.items:
    print("%s\t\t\t%s\t\t\t%s" % ( i.metadata.name,i.spec.cluster_ip,i.spec.ports[0].node_port))
