import tvm

standalone_crt_dir = os.path.join(os.path.dirname(tvm._ffi.libinfo.find_lib_path()[0]), "standalone_crt")
