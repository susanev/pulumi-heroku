// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.Slug.Inputs
{

    public sealed class SlugBlobGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("method")]
        public Input<string>? Method { get; set; }

        [Input("url")]
        public Input<string>? Url { get; set; }

        public SlugBlobGetArgs()
        {
        }
        public static new SlugBlobGetArgs Empty => new SlugBlobGetArgs();
    }
}
