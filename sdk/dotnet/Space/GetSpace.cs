// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.Space
{
    public static class GetSpace
    {
        public static Task<GetSpaceResult> InvokeAsync(GetSpaceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSpaceResult>("heroku:space/getSpace:getSpace", args ?? new GetSpaceArgs(), options.WithDefaults());

        public static Output<GetSpaceResult> Invoke(GetSpaceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSpaceResult>("heroku:space/getSpace:getSpace", args ?? new GetSpaceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSpaceArgs : global::Pulumi.InvokeArgs
    {
        [Input("cidr")]
        public string? Cidr { get; set; }

        [Input("dataCidr")]
        public string? DataCidr { get; set; }

        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetSpaceArgs()
        {
        }
        public static new GetSpaceArgs Empty => new GetSpaceArgs();
    }

    public sealed class GetSpaceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        [Input("dataCidr")]
        public Input<string>? DataCidr { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetSpaceInvokeArgs()
        {
        }
        public static new GetSpaceInvokeArgs Empty => new GetSpaceInvokeArgs();
    }


    [OutputType]
    public sealed class GetSpaceResult
    {
        public readonly string Cidr;
        public readonly string DataCidr;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string Organization;
        public readonly ImmutableArray<string> OutboundIps;
        public readonly string Region;
        public readonly bool Shield;
        public readonly string State;

        [OutputConstructor]
        private GetSpaceResult(
            string cidr,

            string dataCidr,

            string id,

            string name,

            string organization,

            ImmutableArray<string> outboundIps,

            string region,

            bool shield,

            string state)
        {
            Cidr = cidr;
            DataCidr = dataCidr;
            Id = id;
            Name = name;
            Organization = organization;
            OutboundIps = outboundIps;
            Region = region;
            Shield = shield;
            State = state;
        }
    }
}
