# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReleaseArgs', 'Release']

@pulumi.input_type
class ReleaseArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 slug_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Release resource.
        """
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "slug_id", slug_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="slugId")
    def slug_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "slug_id")

    @slug_id.setter
    def slug_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "slug_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ReleaseState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 slug_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Release resources.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if slug_id is not None:
            pulumi.set(__self__, "slug_id", slug_id)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="slugId")
    def slug_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug_id")

    @slug_id.setter
    def slug_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug_id", value)


class Release(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 slug_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Release resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReleaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Release resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ReleaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReleaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 slug_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReleaseArgs.__new__(ReleaseArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["description"] = description
            if slug_id is None and not opts.urn:
                raise TypeError("Missing required property 'slug_id'")
            __props__.__dict__["slug_id"] = slug_id
        super(Release, __self__).__init__(
            'heroku:app/release:Release',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            slug_id: Optional[pulumi.Input[str]] = None) -> 'Release':
        """
        Get an existing Release resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReleaseState.__new__(_ReleaseState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["description"] = description
        __props__.__dict__["slug_id"] = slug_id
        return Release(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="slugId")
    def slug_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug_id")
