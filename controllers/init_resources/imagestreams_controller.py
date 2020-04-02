from handlers.imagestreams import create_imagestream, delete_imagestream
from interfaces.openshift_api import Api
from utils.imagestreams import get_formatted_imagestream_template


def create_imagestreams(openshift_api: Api, namespace: str, imagestreams_names_list: list) -> list:
    res = []
    for imagestream_name in imagestreams_names_list:
        imagestream_template = get_formatted_imagestream_template(imagestream_name, namespace)
        res.append(create_imagestream(openshift_api, namespace, imagestream_template))
    return res


def delete_imagestreams(openshift_api: Api, namespace: str, imagestreams_names_list: list) -> list:
    res = []
    for imagestream_name in imagestreams_names_list:
        res.append(delete_imagestream(openshift_api, namespace, imagestream_name))

    return res
