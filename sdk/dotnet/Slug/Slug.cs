// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Heroku.Slug
{
    [HerokuResourceType("heroku:slug/slug:Slug")]
    public partial class Slug : global::Pulumi.CustomResource
    {
        [Output("appId")]
        public Output<string> AppId { get; private set; } = null!;

        [Output("blobs")]
        public Output<ImmutableArray<Outputs.SlugBlob>> Blobs { get; private set; } = null!;

        [Output("buildpackProvidedDescription")]
        public Output<string?> BuildpackProvidedDescription { get; private set; } = null!;

        [Output("checksum")]
        public Output<string> Checksum { get; private set; } = null!;

        [Output("commit")]
        public Output<string?> Commit { get; private set; } = null!;

        [Output("commitDescription")]
        public Output<string?> CommitDescription { get; private set; } = null!;

        [Output("filePath")]
        public Output<string?> FilePath { get; private set; } = null!;

        [Output("fileUrl")]
        public Output<string?> FileUrl { get; private set; } = null!;

        [Output("processTypes")]
        public Output<ImmutableDictionary<string, object>> ProcessTypes { get; private set; } = null!;

        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        [Output("stack")]
        public Output<string> Stack { get; private set; } = null!;

        [Output("stackId")]
        public Output<string> StackId { get; private set; } = null!;


        /// <summary>
        /// Create a Slug resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Slug(string name, SlugArgs args, CustomResourceOptions? options = null)
            : base("heroku:slug/slug:Slug", name, args ?? new SlugArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Slug(string name, Input<string> id, SlugState? state = null, CustomResourceOptions? options = null)
            : base("heroku:slug/slug:Slug", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Slug resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Slug Get(string name, Input<string> id, SlugState? state = null, CustomResourceOptions? options = null)
        {
            return new Slug(name, id, state, options);
        }
    }

    public sealed class SlugArgs : global::Pulumi.ResourceArgs
    {
        [Input("appId", required: true)]
        public Input<string> AppId { get; set; } = null!;

        [Input("buildpackProvidedDescription")]
        public Input<string>? BuildpackProvidedDescription { get; set; }

        [Input("checksum")]
        public Input<string>? Checksum { get; set; }

        [Input("commit")]
        public Input<string>? Commit { get; set; }

        [Input("commitDescription")]
        public Input<string>? CommitDescription { get; set; }

        [Input("filePath")]
        public Input<string>? FilePath { get; set; }

        [Input("fileUrl")]
        public Input<string>? FileUrl { get; set; }

        [Input("processTypes", required: true)]
        private InputMap<object>? _processTypes;
        public InputMap<object> ProcessTypes
        {
            get => _processTypes ?? (_processTypes = new InputMap<object>());
            set => _processTypes = value;
        }

        [Input("stack")]
        public Input<string>? Stack { get; set; }

        public SlugArgs()
        {
        }
        public static new SlugArgs Empty => new SlugArgs();
    }

    public sealed class SlugState : global::Pulumi.ResourceArgs
    {
        [Input("appId")]
        public Input<string>? AppId { get; set; }

        [Input("blobs")]
        private InputList<Inputs.SlugBlobGetArgs>? _blobs;
        public InputList<Inputs.SlugBlobGetArgs> Blobs
        {
            get => _blobs ?? (_blobs = new InputList<Inputs.SlugBlobGetArgs>());
            set => _blobs = value;
        }

        [Input("buildpackProvidedDescription")]
        public Input<string>? BuildpackProvidedDescription { get; set; }

        [Input("checksum")]
        public Input<string>? Checksum { get; set; }

        [Input("commit")]
        public Input<string>? Commit { get; set; }

        [Input("commitDescription")]
        public Input<string>? CommitDescription { get; set; }

        [Input("filePath")]
        public Input<string>? FilePath { get; set; }

        [Input("fileUrl")]
        public Input<string>? FileUrl { get; set; }

        [Input("processTypes")]
        private InputMap<object>? _processTypes;
        public InputMap<object> ProcessTypes
        {
            get => _processTypes ?? (_processTypes = new InputMap<object>());
            set => _processTypes = value;
        }

        [Input("size")]
        public Input<int>? Size { get; set; }

        [Input("stack")]
        public Input<string>? Stack { get; set; }

        [Input("stackId")]
        public Input<string>? StackId { get; set; }

        public SlugState()
        {
        }
        public static new SlugState Empty => new SlugState();
    }
}
