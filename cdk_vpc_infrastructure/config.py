from aws_cdk import aws_ec2 as ec2

VPC = "cdk-vpc"
INTERNET_GATEWAY = "internet-gateway"
NAT_GATEWAY = "nat-gateway"
REGION = "us-east-1"
PUBLIC_ROUTE_TABLE = "public-route-table"
PRIVATE_ROUTE_TABLE = "private-route-table"
PUBLIC_SUBNET = "public-subnet"
PRIVATE_SUBNET = "private-subnet"

ROUTE_TABLE_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            "destination_cidr_block": "0.0.0.0/0",
            "gateway_id": INTERNET_GATEWAY,
            "router_type": ec2.RouterType.GATEWAY,
        }
    ],
    PRIVATE_ROUTE_TABLE: [
        {
            "destination_cidr_block": "0.0.0.0/0",
            "nat_gateway_id": NAT_GATEWAY,
            "router_type": ec2.RouterType.NAT_GATEWAY,
        }
    ],
}

SUBNET_CONFIGURATION = {
    PUBLIC_SUBNET: {
        "availability_zone": "us-east-1a",
        "cidr_block": "10.0.1.0/24",
        "map_public_ip_on_launch": True,
        "route_table_id": PUBLIC_ROUTE_TABLE,
    },
    PRIVATE_SUBNET: {
        "availability_zone": "us-east-1b",
        "cidr_block": "10.0.2.0/24",
        "map_public_ip_on_launch": False,
        "route_table_id": PRIVATE_ROUTE_TABLE,
    },
}
