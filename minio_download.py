from minio import Minio
from datetime import timedelta

# Create client with anonymous access.
#client = Minio("play.min.io")

# Create client with access and secret key.
#client = Minio("s3.amazonaws.com", "ACCESS-KEY", "SECRET-KEY")

# Create client with access key and secret key with specific region.
client = Minio(
    "minio.192-168-49-2.nip.io/",
    access_key="eoepca",
    secret_key="changeme"
)

objects = (client.list_objects("eoepca"))
for obj in objects:
    print(obj)

# # Create client with custom HTTP client using proxy server.
# import urllib3
# client = Minio(
#     "SERVER:PORT",
#     access_key="ACCESS_KEY",
#     secret_key="SECRET_KEY",
#     secure=True,
#     http_client=urllib3.ProxyManager(
#         "https://PROXYSERVER:PROXYPORT/",
#         timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
#         cert_reqs="CERT_REQUIRED",
#         retries=urllib3.Retry(
#             total=5,
#             backoff_factor=0.2,
#             status_forcelist=[500, 502, 503, 504],
#         ),
#     ),
# )

print(client)

# my_bucket = "eoepca"
# my_object = "catalog.json"
# my_filename = "catalog.json"

# url = client.get_presigned_url(
#     "GET",
#     my_bucket,
#     my_object,
#     expires=timedelta(hours=2),
# )
# print(url)



# client.fget_object(my_bucket, my_object, my_filename)