from kubernetes import client, config

config.load_kube_config()

api_client = client.ApiClient()

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-monitoring-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-monitoring-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-monitoring-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-monitoring-container",
                        image="449669968169.dkr.ecr.us-east-1.amazonaws.com/cloud_monitoring_app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-monitoring-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-monitoring-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)