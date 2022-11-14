// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package formation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Formation struct {
	pulumi.CustomResourceState

	AppId    pulumi.StringOutput `pulumi:"appId"`
	Quantity pulumi.IntOutput    `pulumi:"quantity"`
	Size     pulumi.StringOutput `pulumi:"size"`
	Type     pulumi.StringOutput `pulumi:"type"`
}

// NewFormation registers a new resource with the given unique name, arguments, and options.
func NewFormation(ctx *pulumi.Context,
	name string, args *FormationArgs, opts ...pulumi.ResourceOption) (*Formation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AppId == nil {
		return nil, errors.New("invalid value for required argument 'AppId'")
	}
	if args.Quantity == nil {
		return nil, errors.New("invalid value for required argument 'Quantity'")
	}
	if args.Size == nil {
		return nil, errors.New("invalid value for required argument 'Size'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Formation
	err := ctx.RegisterResource("heroku:formation/formation:Formation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFormation gets an existing Formation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFormation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FormationState, opts ...pulumi.ResourceOption) (*Formation, error) {
	var resource Formation
	err := ctx.ReadResource("heroku:formation/formation:Formation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Formation resources.
type formationState struct {
	AppId    *string `pulumi:"appId"`
	Quantity *int    `pulumi:"quantity"`
	Size     *string `pulumi:"size"`
	Type     *string `pulumi:"type"`
}

type FormationState struct {
	AppId    pulumi.StringPtrInput
	Quantity pulumi.IntPtrInput
	Size     pulumi.StringPtrInput
	Type     pulumi.StringPtrInput
}

func (FormationState) ElementType() reflect.Type {
	return reflect.TypeOf((*formationState)(nil)).Elem()
}

type formationArgs struct {
	AppId    string `pulumi:"appId"`
	Quantity int    `pulumi:"quantity"`
	Size     string `pulumi:"size"`
	Type     string `pulumi:"type"`
}

// The set of arguments for constructing a Formation resource.
type FormationArgs struct {
	AppId    pulumi.StringInput
	Quantity pulumi.IntInput
	Size     pulumi.StringInput
	Type     pulumi.StringInput
}

func (FormationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*formationArgs)(nil)).Elem()
}

type FormationInput interface {
	pulumi.Input

	ToFormationOutput() FormationOutput
	ToFormationOutputWithContext(ctx context.Context) FormationOutput
}

func (*Formation) ElementType() reflect.Type {
	return reflect.TypeOf((**Formation)(nil)).Elem()
}

func (i *Formation) ToFormationOutput() FormationOutput {
	return i.ToFormationOutputWithContext(context.Background())
}

func (i *Formation) ToFormationOutputWithContext(ctx context.Context) FormationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FormationOutput)
}

// FormationArrayInput is an input type that accepts FormationArray and FormationArrayOutput values.
// You can construct a concrete instance of `FormationArrayInput` via:
//
//          FormationArray{ FormationArgs{...} }
type FormationArrayInput interface {
	pulumi.Input

	ToFormationArrayOutput() FormationArrayOutput
	ToFormationArrayOutputWithContext(context.Context) FormationArrayOutput
}

type FormationArray []FormationInput

func (FormationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Formation)(nil)).Elem()
}

func (i FormationArray) ToFormationArrayOutput() FormationArrayOutput {
	return i.ToFormationArrayOutputWithContext(context.Background())
}

func (i FormationArray) ToFormationArrayOutputWithContext(ctx context.Context) FormationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FormationArrayOutput)
}

// FormationMapInput is an input type that accepts FormationMap and FormationMapOutput values.
// You can construct a concrete instance of `FormationMapInput` via:
//
//          FormationMap{ "key": FormationArgs{...} }
type FormationMapInput interface {
	pulumi.Input

	ToFormationMapOutput() FormationMapOutput
	ToFormationMapOutputWithContext(context.Context) FormationMapOutput
}

type FormationMap map[string]FormationInput

func (FormationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Formation)(nil)).Elem()
}

func (i FormationMap) ToFormationMapOutput() FormationMapOutput {
	return i.ToFormationMapOutputWithContext(context.Background())
}

func (i FormationMap) ToFormationMapOutputWithContext(ctx context.Context) FormationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FormationMapOutput)
}

type FormationOutput struct{ *pulumi.OutputState }

func (FormationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Formation)(nil)).Elem()
}

func (o FormationOutput) ToFormationOutput() FormationOutput {
	return o
}

func (o FormationOutput) ToFormationOutputWithContext(ctx context.Context) FormationOutput {
	return o
}

func (o FormationOutput) AppId() pulumi.StringOutput {
	return o.ApplyT(func(v *Formation) pulumi.StringOutput { return v.AppId }).(pulumi.StringOutput)
}

func (o FormationOutput) Quantity() pulumi.IntOutput {
	return o.ApplyT(func(v *Formation) pulumi.IntOutput { return v.Quantity }).(pulumi.IntOutput)
}

func (o FormationOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v *Formation) pulumi.StringOutput { return v.Size }).(pulumi.StringOutput)
}

func (o FormationOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Formation) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type FormationArrayOutput struct{ *pulumi.OutputState }

func (FormationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Formation)(nil)).Elem()
}

func (o FormationArrayOutput) ToFormationArrayOutput() FormationArrayOutput {
	return o
}

func (o FormationArrayOutput) ToFormationArrayOutputWithContext(ctx context.Context) FormationArrayOutput {
	return o
}

func (o FormationArrayOutput) Index(i pulumi.IntInput) FormationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Formation {
		return vs[0].([]*Formation)[vs[1].(int)]
	}).(FormationOutput)
}

type FormationMapOutput struct{ *pulumi.OutputState }

func (FormationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Formation)(nil)).Elem()
}

func (o FormationMapOutput) ToFormationMapOutput() FormationMapOutput {
	return o
}

func (o FormationMapOutput) ToFormationMapOutputWithContext(ctx context.Context) FormationMapOutput {
	return o
}

func (o FormationMapOutput) MapIndex(k pulumi.StringInput) FormationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Formation {
		return vs[0].(map[string]*Formation)[vs[1].(string)]
	}).(FormationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FormationInput)(nil)).Elem(), &Formation{})
	pulumi.RegisterInputType(reflect.TypeOf((*FormationArrayInput)(nil)).Elem(), FormationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*FormationMapInput)(nil)).Elem(), FormationMap{})
	pulumi.RegisterOutputType(FormationOutput{})
	pulumi.RegisterOutputType(FormationArrayOutput{})
	pulumi.RegisterOutputType(FormationMapOutput{})
}
