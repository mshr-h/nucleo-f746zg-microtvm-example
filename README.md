# microTVM example for NUCLEO-F746ZG board

This repo is an simple example for running ONNX model on microTVM targetting NUCLEO-F746ZG board.

## Compatibility

Belows are my testing environment.

- Ubuntu 22.04 on VirtualBox 7.0
  - Host OS: Windows 10
- Python 3.10.6
- Zephyr 2.7
- [TVM@b389d4da](https://github.com/apache/tvm/tree/b389d4dac45bb1fd502940d87126d0a89e15188e)

## Install Zepher

Follow the instruction [here](https://docs.zephyrproject.org/latest/getting_started/index.html).
Note that TVM currently support Zephyr 2.7 so you have to run `west init --mr "v2.7-branch"` instead of `west init`.
You can download the SDK from [Release Zephyr SDK 0.13.2 · zephyrproject-rtos/sdk-ng](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.13.2).

## Install TVM

Follow the instruction [here](https://tvm.apache.org/docs/install/from_source.html).

Add the below lines at the end of `build/config.cmake` file to enable microTVM.

```txt
set(USE_MICRO ON)
set(USE_MICRO_STANDALONE_RUNTIME ON)
```

## Generate ONNX model

Pre-generated ONNX model already in the repo.
It contains `ADD` ONNX operater which adds 2 float typed data and output float typed data.
You can check the model architecture by using [Netron](https://github.com/lutzroeder/netron).

![](docs/netron-add-onnx.png)

If you want to generate it by yourself, follow the instruction below.

Install python package to be able to manipulate onnx format in Python.

```bash
$ pip3 install onnx
```

Run `generate_onnx_model.py` to generate a sample onnx model `add.onnx`.

```bash
$ python3 generate_onnx_model.py
```

## Run ONNX model on TVM

Run `run_onnx_on_tvm.py`.
You'll get the following output.

```bash
$ python3 run_onnx_on_tvm.py
TVM: [11.]
```

## Run ONNX model on microTVM

Run the setup script for Zepyhr.

```bash
$ source ~/zephyrproject/zephyr/zephyr-env.sh
```

Connect the NUCLEO-F746ZG to the PC.

Change the following line in `run_onnx_on_microtvm.py` to the TVM's root directory.

```python
repo_root = "/home/ubuntu/workspace/tvm"
```

Run `run_onnx_on_microtvm.py`.
You'll get the following output.

```
$ run_onnx_on_microtvm.py
Including boilerplate (Zephyr base): /home/ubuntu/zephyrproject/zephyr/cmake/app/boilerplate.cmake
nucleo_f746zg.dts.pre.tmp:97.39-102.5: Warning (simple_bus_reg): /soc/interrupt-controller@40013C00: simple-bus unit address format error, expected "40013c00"
Including boilerplate (Zephyr base): /home/ubuntu/zephyrproject/zephyr/cmake/app/boilerplate.cmake
nucleo_f746zg.dts.pre.tmp:97.39-102.5: Warning (simple_bus_reg): /soc/interrupt-controller@40013C00: simple-bus unit address format error, expected "40013c00"
Including boilerplate (Zephyr base): /home/ubuntu/zephyrproject/zephyr/cmake/app/boilerplate.cmake
nucleo_f746zg.dts.pre.tmp:97.39-102.5: Warning (simple_bus_reg): /soc/interrupt-controller@40013C00: simple-bus unit address format error, expected "40013c00"
Including boilerplate (Zephyr base): /home/ubuntu/zephyrproject/zephyr/cmake/app/boilerplate.cmake
nucleo_f746zg.dts.pre.tmp:97.39-102.5: Warning (simple_bus_reg): /soc/interrupt-controller@40013C00: simple-bus unit address format error, expected "40013c00"
Including boilerplate (Zephyr base): /home/ubuntu/zephyrproject/zephyr/cmake/app/boilerplate.cmake
nucleo_f746zg.dts.pre.tmp:97.39-102.5: Warning (simple_bus_reg): /soc/interrupt-controller@40013C00: simple-bus unit address format error, expected "40013c00"
Open On-Chip Debugger 0.10.0+dev-01508-gf79c90268-dirty (2021-03-26-16:13)
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
066CFF555457888367011946
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
Info : clock speed 2000 kHz
Info : STLINK V2J33M25 (API v2) VID:PID 0483:374B
Info : Target voltage: 3.237870
Warn : Silicon bug: single stepping may enter pending exception handler!
Info : stm32f7x.cpu: hardware has 8 breakpoints, 4 watchpoints
Info : starting gdb server for stm32f7x.cpu on 3333
Info : Listening on port 3333 for gdb connections
    TargetName         Type       Endian TapName            State
--  ------------------ ---------- ------ ------------------ ------------
 0* stm32f7x.cpu       hla_target little stm32f7x.cpu       running

Info : Unable to match requested speed 2000 kHz, using 1800 kHz
Info : Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x080014c0 msp: 0x200108e0
Info : device id = 0x10016449
Info : flash size = 1024 kbytes
auto erase enabled
wrote 65536 bytes from file /tmp/tvm-debug-mode-tempdirs/2021-05-08T14-00-51___v5in0u4j/00000/build/runtime/zephyr/zephyr.hex in 1.609421s (39.766 KiB/s)

Info : Unable to match requested speed 2000 kHz, using 1800 kHz
Info : Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x08002ad4 msp: 0x20049180
verified 40356 bytes in 0.207022s (190.367 KiB/s)

Info : Unable to match requested speed 2000 kHz, using 1800 kHz
Info : Unable to match requested speed 2000 kHz, using 1800 kHz
shutdown command invoked
[14:01:24] ../src/runtime/micro/micro_session.cc:364: remote: microTVM Zephyr runtime - running
microTVM: [11.]
```

If you got `ModuleNotFoundError: No module named 'dtlib'` like the below,

```txt
Traceback (most recent call last):
  File "/home/ubuntu/workspace/nucleo-f746zg-microtvm-example/run_onnx_on_microtvm.py", line 39, in <module>
    with tvm.micro.Session(binary=micro_bin, flasher=compiler.flasher()) as sess:
  File "/home/ubuntu/workspace/tvm/python/tvm/micro/compiler.py", line 218, in flasher
    return self.flasher_factory.override_kw(**kw).instantiate()
  File "/home/ubuntu/workspace/tvm/python/tvm/micro/class_factory.py", line 58, in instantiate
    return self.cls(*self.init_args, **self.init_kw)
  File "/home/ubuntu/workspace/tvm/python/tvm/micro/contrib/zephyr.py", line 346, in __init__
    import dtlib  # pylint: disable=import-outside-toplevel
ModuleNotFoundError: No module named 'dtlib'
```

you have to edit `PATH/TO/tvm/python/tvm/micro/contrib/zephyr.py` around line 344 from

```python
sys.path.insert(0, os.path.join(zephyr_base, "scripts", "dts"))
try:
    import dtlib  # pylint: disable=import-outside-toplevel
```

to

```python
sys.path.insert(0, os.path.join(zephyr_base, "scripts", "dts", "python-devicetree", "src"))
try:
    from devicetree import dtlib  # pylint: disable=import-outside-toplevel
```

## Run ONNX model on standalone microTVM runtime

still working.
