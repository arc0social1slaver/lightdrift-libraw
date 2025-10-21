{
    "targets": [
        {
            "target_name": "raw_addon",
            "sources": ["src/addon.cpp", "src/libraw_wrapper.cpp"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "deps/LibRaw-Source/LibRaw-0.21.4/libraw",
                "deps/LibRaw-Source/LibRaw-0.21.4",
            ],
            "libraries": ["-lraw"],
            "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
        }
    ]
}
