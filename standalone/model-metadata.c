#include <tvm/runtime/crt/module.h>
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_contrib_dense_pack_add_cast_right_shift_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_cast_subtract_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_batch_flatten(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_avg_pool2d_cast_1(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_avg_pool2d_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_conv2d_cast_add_cast_right_shift_cast_cast_nn_relu_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_max_pool2d_cast_nn_relu_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_conv2d_add_right_shift_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t fused_nn_conv2d_cast_add_cast_right_shift_cast_nn_relu_cast_cast(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
#ifdef __cplusplus
extern "C"
#endif
TVM_DLL int32_t _lookup_linked_param(TVMValue* args, int* type_code, int num_args, TVMValue* out_value, int* out_type_code);
static TVMBackendPackedCFunc _tvm_func_array[] = {
    (TVMBackendPackedCFunc)fused_nn_contrib_dense_pack_add_cast_right_shift_cast,
    (TVMBackendPackedCFunc)fused_cast_subtract_cast,
    (TVMBackendPackedCFunc)fused_nn_batch_flatten,
    (TVMBackendPackedCFunc)fused_nn_avg_pool2d_cast_1,
    (TVMBackendPackedCFunc)fused_nn_avg_pool2d_cast,
    (TVMBackendPackedCFunc)fused_nn_conv2d_cast_add_cast_right_shift_cast_cast_nn_relu_cast,
    (TVMBackendPackedCFunc)fused_nn_max_pool2d_cast_nn_relu_cast,
    (TVMBackendPackedCFunc)fused_nn_conv2d_add_right_shift_cast,
    (TVMBackendPackedCFunc)fused_nn_conv2d_cast_add_cast_right_shift_cast_nn_relu_cast_cast,
    (TVMBackendPackedCFunc)_lookup_linked_param,
};
static const TVMFuncRegistry _tvm_func_registry = {
    "\nfused_nn_contrib_dense_pack_add_cast_right_shift_cast\000fused_cast_subtract_cast\000fused_nn_batch_flatten\000fused_nn_avg_pool2d_cast_1\000fused_nn_avg_pool2d_cast\000fused_nn_conv2d_cast_add_cast_right_shift_cast_cast_nn_relu_cast\000fused_nn_max_pool2d_cast_nn_relu_cast\000fused_nn_conv2d_add_right_shift_cast\000fused_nn_conv2d_cast_add_cast_right_shift_cast_nn_relu_cast_cast\000_lookup_linked_param\000",    _tvm_func_array,
};
static const TVMModule _tvm_system_lib = {
    &_tvm_func_registry,
};
const TVMModule* TVMSystemLibEntryPoint(void) {
    return &_tvm_system_lib;
}
;