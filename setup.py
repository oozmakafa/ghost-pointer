from cx_Freeze import setup, Executable

# Include necessary packages
build_exe_options = {
    "includes": ["tkinter","pyautogui", "random", "time", "threading"],
    # Add other necessary options if required
}

setup(
    name="MyApp",
    version="1.0",
    description="My GUI App",
    options={"build_exe": build_exe_options},
    executables=[Executable("ghost_pointer.py")],
)
