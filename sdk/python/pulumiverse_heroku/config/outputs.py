# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'Customizations',
    'Delays',
    'Timeouts',
]

@pulumi.output_type
class Customizations(dict):
    def __init__(__self__, *,
                 set_app_all_config_vars_in_state: Optional[bool] = None):
        if set_app_all_config_vars_in_state is not None:
            pulumi.set(__self__, "set_app_all_config_vars_in_state", set_app_all_config_vars_in_state)

    @property
    @pulumi.getter(name="setAppAllConfigVarsInState")
    def set_app_all_config_vars_in_state(self) -> Optional[bool]:
        return pulumi.get(self, "set_app_all_config_vars_in_state")


@pulumi.output_type
class Delays(dict):
    def __init__(__self__, *,
                 post_app_create_delay: Optional[int] = None,
                 post_domain_create_delay: Optional[int] = None,
                 post_space_create_delay: Optional[int] = None):
        if post_app_create_delay is not None:
            pulumi.set(__self__, "post_app_create_delay", post_app_create_delay)
        if post_domain_create_delay is not None:
            pulumi.set(__self__, "post_domain_create_delay", post_domain_create_delay)
        if post_space_create_delay is not None:
            pulumi.set(__self__, "post_space_create_delay", post_space_create_delay)

    @property
    @pulumi.getter(name="postAppCreateDelay")
    def post_app_create_delay(self) -> Optional[int]:
        return pulumi.get(self, "post_app_create_delay")

    @property
    @pulumi.getter(name="postDomainCreateDelay")
    def post_domain_create_delay(self) -> Optional[int]:
        return pulumi.get(self, "post_domain_create_delay")

    @property
    @pulumi.getter(name="postSpaceCreateDelay")
    def post_space_create_delay(self) -> Optional[int]:
        return pulumi.get(self, "post_space_create_delay")


@pulumi.output_type
class Timeouts(dict):
    def __init__(__self__, *,
                 addon_create_timeout: Optional[int] = None):
        if addon_create_timeout is not None:
            pulumi.set(__self__, "addon_create_timeout", addon_create_timeout)

    @property
    @pulumi.getter(name="addonCreateTimeout")
    def addon_create_timeout(self) -> Optional[int]:
        return pulumi.get(self, "addon_create_timeout")


