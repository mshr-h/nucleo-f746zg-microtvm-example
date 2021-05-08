import onnx

model_name = "add.onnx"

input_tensors = [
    onnx.helper.make_tensor_value_info("Input1", onnx.TensorProto.FLOAT, [1]),
    onnx.helper.make_tensor_value_info("Input2", onnx.TensorProto.FLOAT, [1]),
]

output_tensors = [
    onnx.helper.make_tensor_value_info("Output", onnx.TensorProto.FLOAT, [1]),
]

nodes = []
nodes.append(onnx.helper.make_node("Add", ["Input1", "Input2"], ["Output"]))

graph = onnx.helper.make_graph(nodes, "add-graph", input_tensors, output_tensors)
onnx.checker.check_graph(graph)

model = onnx.helper.make_model(graph, producer_name="mshr-h", producer_version="0.1")
model.opset_import[0].version = 10
onnx.checker.check_model(model)

with open(model_name, "wb") as f:
    f.write(model.SerializeToString())
