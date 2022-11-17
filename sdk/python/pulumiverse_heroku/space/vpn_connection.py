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
from ._inputs import *

__all__ = ['VpnConnectionArgs', 'VpnConnection']

@pulumi.input_type
class VpnConnectionArgs:
    def __init__(__self__, *,
                 public_ip: pulumi.Input[str],
                 routable_cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 space: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tunnels: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]] = None):
        """
        The set of arguments for constructing a VpnConnection resource.
        """
        pulumi.set(__self__, "public_ip", public_ip)
        pulumi.set(__self__, "routable_cidrs", routable_cidrs)
        pulumi.set(__self__, "space", space)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tunnels is not None:
            pulumi.set(__self__, "tunnels", tunnels)

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Input[str]:
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter(name="routableCidrs")
    def routable_cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "routable_cidrs")

    @routable_cidrs.setter
    def routable_cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "routable_cidrs", value)

    @property
    @pulumi.getter
    def space(self) -> pulumi.Input[str]:
        return pulumi.get(self, "space")

    @space.setter
    def space(self, value: pulumi.Input[str]):
        pulumi.set(self, "space", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tunnels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]]:
        return pulumi.get(self, "tunnels")

    @tunnels.setter
    def tunnels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]]):
        pulumi.set(self, "tunnels", value)


@pulumi.input_type
class _VpnConnectionState:
    def __init__(__self__, *,
                 ike_version: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 routable_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 space: Optional[pulumi.Input[str]] = None,
                 space_cidr_block: Optional[pulumi.Input[str]] = None,
                 tunnels: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]] = None):
        """
        Input properties used for looking up and filtering VpnConnection resources.
        """
        if ike_version is not None:
            pulumi.set(__self__, "ike_version", ike_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_ip is not None:
            pulumi.set(__self__, "public_ip", public_ip)
        if routable_cidrs is not None:
            pulumi.set(__self__, "routable_cidrs", routable_cidrs)
        if space is not None:
            pulumi.set(__self__, "space", space)
        if space_cidr_block is not None:
            pulumi.set(__self__, "space_cidr_block", space_cidr_block)
        if tunnels is not None:
            pulumi.set(__self__, "tunnels", tunnels)

    @property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ike_version")

    @ike_version.setter
    def ike_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ike_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter(name="routableCidrs")
    def routable_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "routable_cidrs")

    @routable_cidrs.setter
    def routable_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "routable_cidrs", value)

    @property
    @pulumi.getter
    def space(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "space")

    @space.setter
    def space(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "space", value)

    @property
    @pulumi.getter(name="spaceCidrBlock")
    def space_cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "space_cidr_block")

    @space_cidr_block.setter
    def space_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "space_cidr_block", value)

    @property
    @pulumi.getter
    def tunnels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]]:
        return pulumi.get(self, "tunnels")

    @tunnels.setter
    def tunnels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTunnelArgs']]]]):
        pulumi.set(self, "tunnels", value)


class VpnConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 routable_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 space: Optional[pulumi.Input[str]] = None,
                 tunnels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTunnelArgs']]]]] = None,
                 __props__=None):
        """
        Create a VpnConnection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VpnConnection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VpnConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 routable_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 space: Optional[pulumi.Input[str]] = None,
                 tunnels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTunnelArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnConnectionArgs.__new__(VpnConnectionArgs)

            __props__.__dict__["name"] = name
            if public_ip is None and not opts.urn:
                raise TypeError("Missing required property 'public_ip'")
            __props__.__dict__["public_ip"] = public_ip
            if routable_cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'routable_cidrs'")
            __props__.__dict__["routable_cidrs"] = routable_cidrs
            if space is None and not opts.urn:
                raise TypeError("Missing required property 'space'")
            __props__.__dict__["space"] = space
            __props__.__dict__["tunnels"] = tunnels
            __props__.__dict__["ike_version"] = None
            __props__.__dict__["space_cidr_block"] = None
        super(VpnConnection, __self__).__init__(
            'heroku:space/vpnConnection:VpnConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ike_version: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            routable_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            space: Optional[pulumi.Input[str]] = None,
            space_cidr_block: Optional[pulumi.Input[str]] = None,
            tunnels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTunnelArgs']]]]] = None) -> 'VpnConnection':
        """
        Get an existing VpnConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnConnectionState.__new__(_VpnConnectionState)

        __props__.__dict__["ike_version"] = ike_version
        __props__.__dict__["name"] = name
        __props__.__dict__["public_ip"] = public_ip
        __props__.__dict__["routable_cidrs"] = routable_cidrs
        __props__.__dict__["space"] = space
        __props__.__dict__["space_cidr_block"] = space_cidr_block
        __props__.__dict__["tunnels"] = tunnels
        return VpnConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "ike_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="routableCidrs")
    def routable_cidrs(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "routable_cidrs")

    @property
    @pulumi.getter
    def space(self) -> pulumi.Output[str]:
        return pulumi.get(self, "space")

    @property
    @pulumi.getter(name="spaceCidrBlock")
    def space_cidr_block(self) -> pulumi.Output[str]:
        return pulumi.get(self, "space_cidr_block")

    @property
    @pulumi.getter
    def tunnels(self) -> pulumi.Output[Sequence['outputs.VpnConnectionTunnel']]:
        return pulumi.get(self, "tunnels")
