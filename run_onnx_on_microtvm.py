import os
import pathlib
import json
import numpy as np

import onnx
import tvm
from tvm import relay

model_path = "add.onnx"

## Load onnx model
onnx_model = onnx.load(model_path)
input1_name = "Input1"
input2_name = "Input2"
shape_dict = {input1_name: [1], input2_name: [1]}
mod, params = relay.frontend.from_onnx(onnx_model, shape_dict)

## Define target system
RUNTIME = tvm.relay.backend.Runtime("crt", {"system-lib": True})
boards_file = pathlib.Path(tvm.micro.get_microtvm_template_projects("zephyr")) / "boards.json"
with open(boards_file) as f:
    boards = json.load(f)
BOARD = os.getenv("TVM_MICRO_BOARD", default="nucleo_f746zg")
TARGET = tvm.target.target.micro(boards[BOARD]["model"])
## If you dn't have the target board, comment out the above line and uncomment the below line.
# TARGET = tvm.target.target.micro("host")

## Compile the module
with tvm.transform.PassContext(
    opt_level=3,
    config={"tir.disable_vectorize": True},
    disabled_pass=["AlterOpLayout"]
):
    module = relay.build(mod, target=TARGET, runtime=RUNTIME, params=params)

target = tvm.target.target.micro("stm32f746xx")
board = "nucleo_f746zg"

## Generate project
template_project_path = pathlib.Path(tvm.micro.get_microtvm_template_projects("zephyr"))
project_options = {"project_type": "host_driven", "board": BOARD}
## If you dn't have the target board, comment out the above 2 lines and uncomment the below 2 lines.
# template_project_path = pathlib.Path(tvm.micro.get_microtvm_template_projects("crt"))
# project_options = {}

temp_dir = tvm.contrib.utils.tempdir()
generated_project_dir = temp_dir / "generated-project"
generated_project = tvm.micro.generate_project(
    template_project_path, module, generated_project_dir, project_options
)

## Build and flash the project
generated_project.build()
generated_project.flash()

## Run inference on the target
with tvm.micro.Session(transport_context_manager=generated_project.transport()) as session:
    graph_mod = tvm.micro.create_local_graph_executor(
        module.get_graph_json(),
        session.get_system_lib(),
        session.device
    )

    graph_mod.set_input(**module.get_params())

    ## Generate input values
    input1 = tvm.nd.array(np.array([4], dtype=np.float32))
    input2 = tvm.nd.array(np.array([7], dtype=np.float32))

    ## Set the inputs
    graph_mod.set_input(input1_name, input1)
    graph_mod.set_input(input2_name, input2)

    ## Run inference
    graph_mod.run()

    ## Get output
    tvm_output = graph_mod.get_output(0).numpy()
    print("result is: " + str(tvm_output))
