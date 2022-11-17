# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 customizations: Optional[pulumi.Input['ProviderCustomizationsArgs']] = None,
                 delays: Optional[pulumi.Input['ProviderDelaysArgs']] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['ProviderTimeoutsArgs']] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if customizations is not None:
            pulumi.set(__self__, "customizations", customizations)
        if delays is not None:
            pulumi.set(__self__, "delays", delays)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter
    def customizations(self) -> Optional[pulumi.Input['ProviderCustomizationsArgs']]:
        return pulumi.get(self, "customizations")

    @customizations.setter
    def customizations(self, value: Optional[pulumi.Input['ProviderCustomizationsArgs']]):
        pulumi.set(self, "customizations", value)

    @property
    @pulumi.getter
    def delays(self) -> Optional[pulumi.Input['ProviderDelaysArgs']]:
        return pulumi.get(self, "delays")

    @delays.setter
    def delays(self, value: Optional[pulumi.Input['ProviderDelaysArgs']]):
        pulumi.set(self, "delays", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ProviderTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ProviderTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 customizations: Optional[pulumi.Input[pulumi.InputType['ProviderCustomizationsArgs']]] = None,
                 delays: Optional[pulumi.Input[pulumi.InputType['ProviderDelaysArgs']]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[pulumi.InputType['ProviderTimeoutsArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the heroku package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the heroku package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 customizations: Optional[pulumi.Input[pulumi.InputType['ProviderCustomizationsArgs']]] = None,
                 delays: Optional[pulumi.Input[pulumi.InputType['ProviderDelaysArgs']]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[pulumi.InputType['ProviderTimeoutsArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["customizations"] = pulumi.Output.from_input(customizations).apply(pulumi.runtime.to_json) if customizations is not None else None
            __props__.__dict__["delays"] = pulumi.Output.from_input(delays).apply(pulumi.runtime.to_json) if delays is not None else None
            __props__.__dict__["email"] = email
            __props__.__dict__["headers"] = headers
            __props__.__dict__["timeouts"] = pulumi.Output.from_input(timeouts).apply(pulumi.runtime.to_json) if timeouts is not None else None
            __props__.__dict__["url"] = url
        super(Provider, __self__).__init__(
            'heroku',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "url")
