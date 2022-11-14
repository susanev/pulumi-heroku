// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.App
{
    [HerokuResourceType("heroku:app/feature:Feature")]
    public partial class Feature : global::Pulumi.CustomResource
    {
        [Output("appId")]
        public Output<string> AppId { get; private set; } = null!;

        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Feature resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Feature(string name, FeatureArgs args, CustomResourceOptions? options = null)
            : base("heroku:app/feature:Feature", name, args ?? new FeatureArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Feature(string name, Input<string> id, FeatureState? state = null, CustomResourceOptions? options = null)
            : base("heroku:app/feature:Feature", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Feature resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Feature Get(string name, Input<string> id, FeatureState? state = null, CustomResourceOptions? options = null)
        {
            return new Feature(name, id, state, options);
        }
    }

    public sealed class FeatureArgs : global::Pulumi.ResourceArgs
    {
        [Input("appId", required: true)]
        public Input<string> AppId { get; set; } = null!;

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public FeatureArgs()
        {
        }
        public static new FeatureArgs Empty => new FeatureArgs();
    }

    public sealed class FeatureState : global::Pulumi.ResourceArgs
    {
        [Input("appId")]
        public Input<string>? AppId { get; set; }

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public FeatureState()
        {
        }
        public static new FeatureState Empty => new FeatureState();
    }
}
