# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ResourceIdentityType(str, Enum):

    none = "None"
    system_assigned = "SystemAssigned"


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    provisioning = "Provisioning"
    updating = "Updating"
    deleting = "Deleting"
    accepted = "Accepted"


class ConnectivityStatus(str, Enum):

    connecting = "Connecting"
    connected = "Connected"
    offline = "Offline"
    expired = "Expired"


class AuthenticationMethod(str, Enum):

    token = "Token"
