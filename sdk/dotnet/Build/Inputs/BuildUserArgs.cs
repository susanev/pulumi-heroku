// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.Build.Inputs
{

    public sealed class BuildUserArgs : global::Pulumi.ResourceArgs
    {
        [Input("email")]
        public Input<string>? Email { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        public BuildUserArgs()
        {
        }
        public static new BuildUserArgs Empty => new BuildUserArgs();
    }
}