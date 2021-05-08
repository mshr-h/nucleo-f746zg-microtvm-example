import tvm
from tvm import relay
import numpy as np
import onnx
from tvm.contrib import graph_executor

model_path = "add.onnx"

onnx_model = onnx.load(model_path)

input1_name = "Input1"
input2_name = "Input2"
shape_dict = {input1_name: [1], input2_name: [1]}
mod, params = relay.frontend.from_onnx(onnx_model, shape_dict)

target = "llvm"
with tvm.transform.PassContext(opt_level=3):
    lib = relay.build(mod, target, params=params)

dev = tvm.cpu(0)
dtype = "float32"

m_ = graph_executor.GraphModule(lib["default"](dev))

input1 = tvm.nd.array(np.array([4], dtype=dtype))
input2 = tvm.nd.array(np.array([7], dtype=dtype))
m_.set_input("Input1", input1)
m_.set_input("Input2", input2)
m_.run()
output = m_.get_output(0).asnumpy()

print('TVM:', output)
