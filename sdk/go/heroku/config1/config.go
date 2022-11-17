// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Config struct {
	pulumi.CustomResourceState

	SensitiveVars pulumi.StringMapOutput `pulumi:"sensitiveVars"`
	Vars          pulumi.StringMapOutput `pulumi:"vars"`
}

// NewConfig registers a new resource with the given unique name, arguments, and options.
func NewConfig(ctx *pulumi.Context,
	name string, args *ConfigArgs, opts ...pulumi.ResourceOption) (*Config, error) {
	if args == nil {
		args = &ConfigArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource Config
	err := ctx.RegisterResource("heroku:config1/config:Config", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfig gets an existing Config resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigState, opts ...pulumi.ResourceOption) (*Config, error) {
	var resource Config
	err := ctx.ReadResource("heroku:config1/config:Config", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Config resources.
type configState struct {
	SensitiveVars map[string]string `pulumi:"sensitiveVars"`
	Vars          map[string]string `pulumi:"vars"`
}

type ConfigState struct {
	SensitiveVars pulumi.StringMapInput
	Vars          pulumi.StringMapInput
}

func (ConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*configState)(nil)).Elem()
}

type configArgs struct {
	SensitiveVars map[string]string `pulumi:"sensitiveVars"`
	Vars          map[string]string `pulumi:"vars"`
}

// The set of arguments for constructing a Config resource.
type ConfigArgs struct {
	SensitiveVars pulumi.StringMapInput
	Vars          pulumi.StringMapInput
}

func (ConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configArgs)(nil)).Elem()
}

type ConfigInput interface {
	pulumi.Input

	ToConfigOutput() ConfigOutput
	ToConfigOutputWithContext(ctx context.Context) ConfigOutput
}

func (*Config) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil)).Elem()
}

func (i *Config) ToConfigOutput() ConfigOutput {
	return i.ToConfigOutputWithContext(context.Background())
}

func (i *Config) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigOutput)
}

// ConfigArrayInput is an input type that accepts ConfigArray and ConfigArrayOutput values.
// You can construct a concrete instance of `ConfigArrayInput` via:
//
//          ConfigArray{ ConfigArgs{...} }
type ConfigArrayInput interface {
	pulumi.Input

	ToConfigArrayOutput() ConfigArrayOutput
	ToConfigArrayOutputWithContext(context.Context) ConfigArrayOutput
}

type ConfigArray []ConfigInput

func (ConfigArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Config)(nil)).Elem()
}

func (i ConfigArray) ToConfigArrayOutput() ConfigArrayOutput {
	return i.ToConfigArrayOutputWithContext(context.Background())
}

func (i ConfigArray) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigArrayOutput)
}

// ConfigMapInput is an input type that accepts ConfigMap and ConfigMapOutput values.
// You can construct a concrete instance of `ConfigMapInput` via:
//
//          ConfigMap{ "key": ConfigArgs{...} }
type ConfigMapInput interface {
	pulumi.Input

	ToConfigMapOutput() ConfigMapOutput
	ToConfigMapOutputWithContext(context.Context) ConfigMapOutput
}

type ConfigMap map[string]ConfigInput

func (ConfigMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Config)(nil)).Elem()
}

func (i ConfigMap) ToConfigMapOutput() ConfigMapOutput {
	return i.ToConfigMapOutputWithContext(context.Background())
}

func (i ConfigMap) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigMapOutput)
}

type ConfigOutput struct{ *pulumi.OutputState }

func (ConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil)).Elem()
}

func (o ConfigOutput) ToConfigOutput() ConfigOutput {
	return o
}

func (o ConfigOutput) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return o
}

func (o ConfigOutput) SensitiveVars() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Config) pulumi.StringMapOutput { return v.SensitiveVars }).(pulumi.StringMapOutput)
}

func (o ConfigOutput) Vars() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Config) pulumi.StringMapOutput { return v.Vars }).(pulumi.StringMapOutput)
}

type ConfigArrayOutput struct{ *pulumi.OutputState }

func (ConfigArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Config)(nil)).Elem()
}

func (o ConfigArrayOutput) ToConfigArrayOutput() ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) Index(i pulumi.IntInput) ConfigOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Config {
		return vs[0].([]*Config)[vs[1].(int)]
	}).(ConfigOutput)
}

type ConfigMapOutput struct{ *pulumi.OutputState }

func (ConfigMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Config)(nil)).Elem()
}

func (o ConfigMapOutput) ToConfigMapOutput() ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) MapIndex(k pulumi.StringInput) ConfigOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Config {
		return vs[0].(map[string]*Config)[vs[1].(string)]
	}).(ConfigOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigInput)(nil)).Elem(), &Config{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigArrayInput)(nil)).Elem(), ConfigArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigMapInput)(nil)).Elem(), ConfigMap{})
	pulumi.RegisterOutputType(ConfigOutput{})
	pulumi.RegisterOutputType(ConfigArrayOutput{})
	pulumi.RegisterOutputType(ConfigMapOutput{})
}