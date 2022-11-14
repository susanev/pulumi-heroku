# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetAppResult',
    'AwaitableGetAppResult',
    'get_app',
    'get_app_output',
]

@pulumi.output_type
class GetAppResult:
    """
    A collection of values returned by getApp.
    """
    def __init__(__self__, acm=None, buildpacks=None, config_vars=None, git_url=None, heroku_hostname=None, id=None, internal_routing=None, name=None, organizations=None, region=None, space=None, stack=None, uuid=None, web_url=None):
        if acm and not isinstance(acm, bool):
            raise TypeError("Expected argument 'acm' to be a bool")
        pulumi.set(__self__, "acm", acm)
        if buildpacks and not isinstance(buildpacks, list):
            raise TypeError("Expected argument 'buildpacks' to be a list")
        pulumi.set(__self__, "buildpacks", buildpacks)
        if config_vars and not isinstance(config_vars, dict):
            raise TypeError("Expected argument 'config_vars' to be a dict")
        pulumi.set(__self__, "config_vars", config_vars)
        if git_url and not isinstance(git_url, str):
            raise TypeError("Expected argument 'git_url' to be a str")
        pulumi.set(__self__, "git_url", git_url)
        if heroku_hostname and not isinstance(heroku_hostname, str):
            raise TypeError("Expected argument 'heroku_hostname' to be a str")
        pulumi.set(__self__, "heroku_hostname", heroku_hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_routing and not isinstance(internal_routing, bool):
            raise TypeError("Expected argument 'internal_routing' to be a bool")
        pulumi.set(__self__, "internal_routing", internal_routing)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organizations and not isinstance(organizations, list):
            raise TypeError("Expected argument 'organizations' to be a list")
        pulumi.set(__self__, "organizations", organizations)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if space and not isinstance(space, str):
            raise TypeError("Expected argument 'space' to be a str")
        pulumi.set(__self__, "space", space)
        if stack and not isinstance(stack, str):
            raise TypeError("Expected argument 'stack' to be a str")
        pulumi.set(__self__, "stack", stack)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if web_url and not isinstance(web_url, str):
            raise TypeError("Expected argument 'web_url' to be a str")
        pulumi.set(__self__, "web_url", web_url)

    @property
    @pulumi.getter
    def acm(self) -> bool:
        return pulumi.get(self, "acm")

    @property
    @pulumi.getter
    def buildpacks(self) -> Sequence[str]:
        return pulumi.get(self, "buildpacks")

    @property
    @pulumi.getter(name="configVars")
    def config_vars(self) -> Mapping[str, Any]:
        return pulumi.get(self, "config_vars")

    @property
    @pulumi.getter(name="gitUrl")
    def git_url(self) -> str:
        return pulumi.get(self, "git_url")

    @property
    @pulumi.getter(name="herokuHostname")
    def heroku_hostname(self) -> str:
        return pulumi.get(self, "heroku_hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalRouting")
    def internal_routing(self) -> bool:
        return pulumi.get(self, "internal_routing")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organizations(self) -> Sequence['outputs.GetAppOrganizationResult']:
        return pulumi.get(self, "organizations")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def space(self) -> str:
        return pulumi.get(self, "space")

    @property
    @pulumi.getter
    def stack(self) -> str:
        return pulumi.get(self, "stack")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="webUrl")
    def web_url(self) -> str:
        return pulumi.get(self, "web_url")


class AwaitableGetAppResult(GetAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppResult(
            acm=self.acm,
            buildpacks=self.buildpacks,
            config_vars=self.config_vars,
            git_url=self.git_url,
            heroku_hostname=self.heroku_hostname,
            id=self.id,
            internal_routing=self.internal_routing,
            name=self.name,
            organizations=self.organizations,
            region=self.region,
            space=self.space,
            stack=self.stack,
            uuid=self.uuid,
            web_url=self.web_url)


def get_app(name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('heroku:app/getApp:getApp', __args__, opts=opts, typ=GetAppResult).value

    return AwaitableGetAppResult(
        acm=__ret__.acm,
        buildpacks=__ret__.buildpacks,
        config_vars=__ret__.config_vars,
        git_url=__ret__.git_url,
        heroku_hostname=__ret__.heroku_hostname,
        id=__ret__.id,
        internal_routing=__ret__.internal_routing,
        name=__ret__.name,
        organizations=__ret__.organizations,
        region=__ret__.region,
        space=__ret__.space,
        stack=__ret__.stack,
        uuid=__ret__.uuid,
        web_url=__ret__.web_url)


@_utilities.lift_output_func(get_app)
def get_app_output(name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
