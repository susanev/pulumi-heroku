// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class Space extends pulumi.CustomResource {
    /**
     * Get an existing Space resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpaceState, opts?: pulumi.CustomResourceOptions): Space {
        return new Space(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'heroku:space/space:Space';

    /**
     * Returns true if the given object is an instance of Space.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Space {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Space.__pulumiType;
    }

    public readonly cidr!: pulumi.Output<string | undefined>;
    public readonly dataCidr!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly organization!: pulumi.Output<string>;
    public /*out*/ readonly outboundIps!: pulumi.Output<string[]>;
    public readonly region!: pulumi.Output<string | undefined>;
    public readonly shield!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Space resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SpaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SpaceArgs | SpaceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SpaceState | undefined;
            resourceInputs["cidr"] = state ? state.cidr : undefined;
            resourceInputs["dataCidr"] = state ? state.dataCidr : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["organization"] = state ? state.organization : undefined;
            resourceInputs["outboundIps"] = state ? state.outboundIps : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["shield"] = state ? state.shield : undefined;
        } else {
            const args = argsOrState as SpaceArgs | undefined;
            if ((!args || args.organization === undefined) && !opts.urn) {
                throw new Error("Missing required property 'organization'");
            }
            resourceInputs["cidr"] = args ? args.cidr : undefined;
            resourceInputs["dataCidr"] = args ? args.dataCidr : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["organization"] = args ? args.organization : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["shield"] = args ? args.shield : undefined;
            resourceInputs["outboundIps"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Space.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Space resources.
 */
export interface SpaceState {
    cidr?: pulumi.Input<string>;
    dataCidr?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    organization?: pulumi.Input<string>;
    outboundIps?: pulumi.Input<pulumi.Input<string>[]>;
    region?: pulumi.Input<string>;
    shield?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a Space resource.
 */
export interface SpaceArgs {
    cidr?: pulumi.Input<string>;
    dataCidr?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    organization: pulumi.Input<string>;
    region?: pulumi.Input<string>;
    shield?: pulumi.Input<boolean>;
}