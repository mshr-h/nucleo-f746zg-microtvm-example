import tvm
from tvm import relay
import onnx
import tvm.micro
from tvm.micro.contrib import zephyr
import os
import numpy as np

model_path = "add.onnx"

onnx_model = onnx.load(model_path)

input1_name = "Input1"
input2_name = "Input2"
shape_dict = {input1_name: [1], input2_name: [1]}
mod, params = relay.frontend.from_onnx(onnx_model, shape_dict)

target = tvm.target.target.micro("stm32f746xx")
board = "nucleo_f746zg"

with tvm.transform.PassContext(opt_level=3, config={"tir.disable_vectorize": True}):
    module = tvm.relay.build(mod, target=target, params=params)
    graph_json, compiled_model, simplified_params = module.get_graph_json(), module.get_lib(), module.get_params()

repo_root = "/home/ubuntu/workspace/tvm"
project_dir = os.path.join(repo_root, "apps", "microtvm", "zephyr", "demo_runtime")
compiler = zephyr.ZephyrCompiler(
    project_dir=project_dir,
    board=board,
    zephyr_toolchain_variant="zephyr",
)

opts = tvm.micro.default_options(f"{project_dir}/crt")

workspace = tvm.micro.Workspace(debug=True)
micro_bin = tvm.micro.build_static_runtime(workspace, compiler, compiled_model, opts)

dtype = "float32"
with tvm.micro.Session(binary=micro_bin, flasher=compiler.flasher()) as sess:
    m_ = tvm.micro.create_local_graph_executor(graph_json, sess.get_system_lib(), sess.device)

    input1 = tvm.nd.array(np.array([4], dtype=dtype))
    input2 = tvm.nd.array(np.array([7], dtype=dtype))
    m_.set_input("Input1", input1)
    m_.set_input("Input2", input2)
    m_.run()
    output = m_.get_output(0).asnumpy()

print('microTVM:', output)
