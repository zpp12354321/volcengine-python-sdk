# coding: utf-8

# flake8: noqa

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from volcenginesdkautoscaling.api.auto_scaling_api import AUTOSCALINGApi

# import models into sdk package
from volcenginesdkautoscaling.models.alarm_policy_condition_for_create_scaling_policy_input import AlarmPolicyConditionForCreateScalingPolicyInput
from volcenginesdkautoscaling.models.alarm_policy_condition_for_modify_scaling_policy_input import AlarmPolicyConditionForModifyScalingPolicyInput
from volcenginesdkautoscaling.models.alarm_policy_for_create_scaling_policy_input import AlarmPolicyForCreateScalingPolicyInput
from volcenginesdkautoscaling.models.alarm_policy_for_describe_scaling_policies_output import AlarmPolicyForDescribeScalingPoliciesOutput
from volcenginesdkautoscaling.models.alarm_policy_for_modify_scaling_policy_input import AlarmPolicyForModifyScalingPolicyInput
from volcenginesdkautoscaling.models.attach_db_instances_request import AttachDBInstancesRequest
from volcenginesdkautoscaling.models.attach_db_instances_response import AttachDBInstancesResponse
from volcenginesdkautoscaling.models.attach_instances_request import AttachInstancesRequest
from volcenginesdkautoscaling.models.attach_instances_response import AttachInstancesResponse
from volcenginesdkautoscaling.models.attach_server_groups_request import AttachServerGroupsRequest
from volcenginesdkautoscaling.models.attach_server_groups_response import AttachServerGroupsResponse
from volcenginesdkautoscaling.models.complete_lifecycle_activity_request import CompleteLifecycleActivityRequest
from volcenginesdkautoscaling.models.complete_lifecycle_activity_response import CompleteLifecycleActivityResponse
from volcenginesdkautoscaling.models.condition_for_describe_scaling_policies_output import ConditionForDescribeScalingPoliciesOutput
from volcenginesdkautoscaling.models.create_lifecycle_hook_request import CreateLifecycleHookRequest
from volcenginesdkautoscaling.models.create_lifecycle_hook_response import CreateLifecycleHookResponse
from volcenginesdkautoscaling.models.create_scaling_configuration_request import CreateScalingConfigurationRequest
from volcenginesdkautoscaling.models.create_scaling_configuration_response import CreateScalingConfigurationResponse
from volcenginesdkautoscaling.models.create_scaling_group_request import CreateScalingGroupRequest
from volcenginesdkautoscaling.models.create_scaling_group_response import CreateScalingGroupResponse
from volcenginesdkautoscaling.models.create_scaling_policy_request import CreateScalingPolicyRequest
from volcenginesdkautoscaling.models.create_scaling_policy_response import CreateScalingPolicyResponse
from volcenginesdkautoscaling.models.delete_lifecycle_hook_request import DeleteLifecycleHookRequest
from volcenginesdkautoscaling.models.delete_lifecycle_hook_response import DeleteLifecycleHookResponse
from volcenginesdkautoscaling.models.delete_scaling_configuration_request import DeleteScalingConfigurationRequest
from volcenginesdkautoscaling.models.delete_scaling_configuration_response import DeleteScalingConfigurationResponse
from volcenginesdkautoscaling.models.delete_scaling_group_request import DeleteScalingGroupRequest
from volcenginesdkautoscaling.models.delete_scaling_group_response import DeleteScalingGroupResponse
from volcenginesdkautoscaling.models.delete_scaling_policy_request import DeleteScalingPolicyRequest
from volcenginesdkautoscaling.models.delete_scaling_policy_response import DeleteScalingPolicyResponse
from volcenginesdkautoscaling.models.describe_lifecycle_activities_request import DescribeLifecycleActivitiesRequest
from volcenginesdkautoscaling.models.describe_lifecycle_activities_response import DescribeLifecycleActivitiesResponse
from volcenginesdkautoscaling.models.describe_lifecycle_hooks_request import DescribeLifecycleHooksRequest
from volcenginesdkautoscaling.models.describe_lifecycle_hooks_response import DescribeLifecycleHooksResponse
from volcenginesdkautoscaling.models.describe_scaling_activities_request import DescribeScalingActivitiesRequest
from volcenginesdkautoscaling.models.describe_scaling_activities_response import DescribeScalingActivitiesResponse
from volcenginesdkautoscaling.models.describe_scaling_configurations_request import DescribeScalingConfigurationsRequest
from volcenginesdkautoscaling.models.describe_scaling_configurations_response import DescribeScalingConfigurationsResponse
from volcenginesdkautoscaling.models.describe_scaling_groups_request import DescribeScalingGroupsRequest
from volcenginesdkautoscaling.models.describe_scaling_groups_response import DescribeScalingGroupsResponse
from volcenginesdkautoscaling.models.describe_scaling_instances_request import DescribeScalingInstancesRequest
from volcenginesdkautoscaling.models.describe_scaling_instances_response import DescribeScalingInstancesResponse
from volcenginesdkautoscaling.models.describe_scaling_policies_request import DescribeScalingPoliciesRequest
from volcenginesdkautoscaling.models.describe_scaling_policies_response import DescribeScalingPoliciesResponse
from volcenginesdkautoscaling.models.detach_db_instances_request import DetachDBInstancesRequest
from volcenginesdkautoscaling.models.detach_db_instances_response import DetachDBInstancesResponse
from volcenginesdkautoscaling.models.detach_instances_request import DetachInstancesRequest
from volcenginesdkautoscaling.models.detach_instances_response import DetachInstancesResponse
from volcenginesdkautoscaling.models.detach_server_groups_request import DetachServerGroupsRequest
from volcenginesdkautoscaling.models.detach_server_groups_response import DetachServerGroupsResponse
from volcenginesdkautoscaling.models.disable_scaling_group_request import DisableScalingGroupRequest
from volcenginesdkautoscaling.models.disable_scaling_group_response import DisableScalingGroupResponse
from volcenginesdkautoscaling.models.disable_scaling_policy_request import DisableScalingPolicyRequest
from volcenginesdkautoscaling.models.disable_scaling_policy_response import DisableScalingPolicyResponse
from volcenginesdkautoscaling.models.eip_for_create_scaling_configuration_input import EipForCreateScalingConfigurationInput
from volcenginesdkautoscaling.models.eip_for_describe_scaling_configurations_output import EipForDescribeScalingConfigurationsOutput
from volcenginesdkautoscaling.models.eip_for_modify_scaling_configuration_input import EipForModifyScalingConfigurationInput
from volcenginesdkautoscaling.models.enable_scaling_configuration_request import EnableScalingConfigurationRequest
from volcenginesdkautoscaling.models.enable_scaling_configuration_response import EnableScalingConfigurationResponse
from volcenginesdkautoscaling.models.enable_scaling_group_request import EnableScalingGroupRequest
from volcenginesdkautoscaling.models.enable_scaling_group_response import EnableScalingGroupResponse
from volcenginesdkautoscaling.models.enable_scaling_policy_request import EnableScalingPolicyRequest
from volcenginesdkautoscaling.models.enable_scaling_policy_response import EnableScalingPolicyResponse
from volcenginesdkautoscaling.models.instance_protection_result_for_set_instances_protection_output import InstanceProtectionResultForSetInstancesProtectionOutput
from volcenginesdkautoscaling.models.lifecycle_activity_for_describe_lifecycle_activities_output import LifecycleActivityForDescribeLifecycleActivitiesOutput
from volcenginesdkautoscaling.models.lifecycle_hook_for_describe_lifecycle_hooks_output import LifecycleHookForDescribeLifecycleHooksOutput
from volcenginesdkautoscaling.models.modify_lifecycle_hook_request import ModifyLifecycleHookRequest
from volcenginesdkautoscaling.models.modify_lifecycle_hook_response import ModifyLifecycleHookResponse
from volcenginesdkautoscaling.models.modify_scaling_configuration_request import ModifyScalingConfigurationRequest
from volcenginesdkautoscaling.models.modify_scaling_configuration_response import ModifyScalingConfigurationResponse
from volcenginesdkautoscaling.models.modify_scaling_group_request import ModifyScalingGroupRequest
from volcenginesdkautoscaling.models.modify_scaling_group_response import ModifyScalingGroupResponse
from volcenginesdkautoscaling.models.modify_scaling_policy_request import ModifyScalingPolicyRequest
from volcenginesdkautoscaling.models.modify_scaling_policy_response import ModifyScalingPolicyResponse
from volcenginesdkautoscaling.models.related_instance_for_describe_scaling_activities_output import RelatedInstanceForDescribeScalingActivitiesOutput
from volcenginesdkautoscaling.models.remove_instances_request import RemoveInstancesRequest
from volcenginesdkautoscaling.models.remove_instances_response import RemoveInstancesResponse
from volcenginesdkautoscaling.models.scaling_activity_for_describe_scaling_activities_output import ScalingActivityForDescribeScalingActivitiesOutput
from volcenginesdkautoscaling.models.scaling_configuration_for_describe_scaling_configurations_output import ScalingConfigurationForDescribeScalingConfigurationsOutput
from volcenginesdkautoscaling.models.scaling_group_for_describe_scaling_groups_output import ScalingGroupForDescribeScalingGroupsOutput
from volcenginesdkautoscaling.models.scaling_instance_for_describe_scaling_instances_output import ScalingInstanceForDescribeScalingInstancesOutput
from volcenginesdkautoscaling.models.scaling_policy_for_describe_scaling_policies_output import ScalingPolicyForDescribeScalingPoliciesOutput
from volcenginesdkautoscaling.models.scheduled_policy_for_create_scaling_policy_input import ScheduledPolicyForCreateScalingPolicyInput
from volcenginesdkautoscaling.models.scheduled_policy_for_describe_scaling_policies_output import ScheduledPolicyForDescribeScalingPoliciesOutput
from volcenginesdkautoscaling.models.scheduled_policy_for_modify_scaling_policy_input import ScheduledPolicyForModifyScalingPolicyInput
from volcenginesdkautoscaling.models.server_group_attribute_for_attach_server_groups_input import ServerGroupAttributeForAttachServerGroupsInput
from volcenginesdkautoscaling.models.server_group_attribute_for_create_scaling_group_input import ServerGroupAttributeForCreateScalingGroupInput
from volcenginesdkautoscaling.models.server_group_attribute_for_describe_scaling_groups_output import ServerGroupAttributeForDescribeScalingGroupsOutput
from volcenginesdkautoscaling.models.server_group_attribute_for_detach_server_groups_input import ServerGroupAttributeForDetachServerGroupsInput
from volcenginesdkautoscaling.models.set_instances_protection_request import SetInstancesProtectionRequest
from volcenginesdkautoscaling.models.set_instances_protection_response import SetInstancesProtectionResponse
from volcenginesdkautoscaling.models.volume_for_create_scaling_configuration_input import VolumeForCreateScalingConfigurationInput
from volcenginesdkautoscaling.models.volume_for_describe_scaling_configurations_output import VolumeForDescribeScalingConfigurationsOutput
from volcenginesdkautoscaling.models.volume_for_modify_scaling_configuration_input import VolumeForModifyScalingConfigurationInput
