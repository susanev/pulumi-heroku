// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class PeeringConnectionAccepter extends pulumi.CustomResource {
    /**
     * Get an existing PeeringConnectionAccepter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PeeringConnectionAccepterState, opts?: pulumi.CustomResourceOptions): PeeringConnectionAccepter {
        return new PeeringConnectionAccepter(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'heroku:space/peeringConnectionAccepter:PeeringConnectionAccepter';

    /**
     * Returns true if the given object is an instance of PeeringConnectionAccepter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PeeringConnectionAccepter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PeeringConnectionAccepter.__pulumiType;
    }

    public readonly space!: pulumi.Output<string>;
    public /*out*/ readonly status!: pulumi.Output<string>;
    public /*out*/ readonly type!: pulumi.Output<string>;
    public readonly vpcPeeringConnectionId!: pulumi.Output<string>;

    /**
     * Create a PeeringConnectionAccepter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PeeringConnectionAccepterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PeeringConnectionAccepterArgs | PeeringConnectionAccepterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PeeringConnectionAccepterState | undefined;
            resourceInputs["space"] = state ? state.space : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["vpcPeeringConnectionId"] = state ? state.vpcPeeringConnectionId : undefined;
        } else {
            const args = argsOrState as PeeringConnectionAccepterArgs | undefined;
            if ((!args || args.space === undefined) && !opts.urn) {
                throw new Error("Missing required property 'space'");
            }
            if ((!args || args.vpcPeeringConnectionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcPeeringConnectionId'");
            }
            resourceInputs["space"] = args ? args.space : undefined;
            resourceInputs["vpcPeeringConnectionId"] = args ? args.vpcPeeringConnectionId : undefined;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PeeringConnectionAccepter.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PeeringConnectionAccepter resources.
 */
export interface PeeringConnectionAccepterState {
    space?: pulumi.Input<string>;
    status?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
    vpcPeeringConnectionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PeeringConnectionAccepter resource.
 */
export interface PeeringConnectionAccepterArgs {
    space: pulumi.Input<string>;
    vpcPeeringConnectionId: pulumi.Input<string>;
}
