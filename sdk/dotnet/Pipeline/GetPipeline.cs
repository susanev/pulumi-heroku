// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.Pipeline
{
    public static class GetPipeline
    {
        public static Task<GetPipelineResult> InvokeAsync(GetPipelineArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPipelineResult>("heroku:pipeline/getPipeline:getPipeline", args ?? new GetPipelineArgs(), options.WithDefaults());

        public static Output<GetPipelineResult> Invoke(GetPipelineInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPipelineResult>("heroku:pipeline/getPipeline:getPipeline", args ?? new GetPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPipelineArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetPipelineArgs()
        {
        }
        public static new GetPipelineArgs Empty => new GetPipelineArgs();
    }

    public sealed class GetPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetPipelineInvokeArgs()
        {
        }
        public static new GetPipelineInvokeArgs Empty => new GetPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPipelineResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string OwnerId;
        public readonly string OwnerType;

        [OutputConstructor]
        private GetPipelineResult(
            string id,

            string name,

            string ownerId,

            string ownerType)
        {
            Id = id;
            Name = name;
            OwnerId = ownerId;
            OwnerType = ownerType;
        }
    }
}