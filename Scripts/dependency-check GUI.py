import subprocess
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import os
import shutil
import shlex
import logging

home_dir = os.path.expanduser("~")

dependency_check_path = os.path.join(
    home_dir, "Desktop\\DependencyCheckGUI\\dependency-check\\bin\\dependency-check.bat")

log_file_path = os.path.join(
    home_dir, "Desktop\\DependencyCheckGUI\\dependency_check_gui.log")

# Configure logging
logging.basicConfig(filename=log_file_path, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def run_dependency_check():
    run_button.config(state=tk.DISABLED)

    try:
        home_dir = os.path.expanduser("~")
        dependency_check_path = os.path.join(
            home_dir, "Desktop\\DependencyCheckGUI\\dependency-check\\bin\\dependency-check.bat")

        # Check if dependency-check is in PATH
        dependency_check_path = shutil.which(dependency_check_path)
        if dependency_check_path is None:
            logging.error("dependency-check is not available in the PATH.")
            run_button.config(state=tk.NORMAL)
            return

        # Fetch or set API key
        api_key_path = home_dir + \
            "\\Desktop\\DependencyCheckGUI\\dependency-check\\NVD API KEY.txt"
        if os.path.exists(api_key_path):
            with open(api_key_path, 'r') as file:
                default_api_key = file.read().strip()
        else:
            default_api_key = ""

        api_key = os.getenv('NVD_API_KEY', default_api_key)
        if not api_key:
            api_key = api_key_entry.get().strip()

        if update_only_var.get():
            command = f"\"{dependency_check_path}\" --updateonly --nvdApiKey {api_key}"
        else:
            project_name = project_entry.get().strip()
            app_version = version_entry.get().strip()
            app_path = app_path_entry.get().strip()
            report_dir = report_entry.get().strip()

            missing_fields = []
            if not project_name:
                missing_fields.append("Project Name")
            if not app_version:
                missing_fields.append("Application Version")
            if not app_path:
                missing_fields.append("Path to Application")

            if missing_fields:
                messagebox.showerror(
                    "Missing Information", f"The following fields are required: {', '.join(missing_fields)}")
                run_button.config(state=tk.NORMAL)
                return

            project_versioned = f"{project_name}_v{app_version}"
            report_dir_versioned = os.path.join(report_dir, project_versioned)
            report_dir_versioned = os.path.normpath(report_dir_versioned)

            try:
                os.makedirs(report_dir_versioned, exist_ok=True)
            except OSError as e:
                logging.error(
                    f"Failed to create report directory: {report_dir_versioned}", exc_info=True)
                run_button.config(state=tk.NORMAL)
                return

            if offline_var.get():
                command = (
                    f"\"{dependency_check_path}\" "
                    f"--project \"{project_versioned}\" "
                    f"-f ALL "
                    f"--disableOssIndex "
                    f"--noupdate "
                    f"--nvdApiKey \"{api_key}\" "
                    f"-s \"{app_path}\" "
                    f"-o \"{report_dir_versioned}\""
                )
            else:
                command = (
                    f"\"{dependency_check_path}\" "
                    f"--project \"{project_versioned}\" "
                    f"-f ALL "
                    f"--nvdApiKey \"{api_key}\" "
                    f"-s \"{app_path}\" "
                    f"-o \"{report_dir_versioned}\""
                )

        logging.info(f"Executing command: {command}")
        print(f"Executing command: {command}")

        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        stdout, stderr = result.stdout, result.stderr

        # Update GUI with command output
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(
            tk.END, f"Command: {command}\n\nOutput:\n{stdout}\n\nErrors:\n{stderr}")
        output_text.config(state=tk.DISABLED)

        if result.returncode != 0:
            logging.error(f"Dependency-Check encountered an error: {stderr}")

    except Exception as e:
        logging.exception("An error occurred in run_dependency_check:")
    finally:
        run_button.config(state=tk.NORMAL)


def browse_app_path():
    folder_selected = filedialog.askdirectory(initialdir=r"C:\Program Files")
    if folder_selected:
        app_path_entry.delete(0, tk.END)
        app_path_entry.insert(0, os.path.normpath(folder_selected))


def browse_report_dir():
    folder_selected = filedialog.askdirectory(
        initialdir=rf"{home_dir}\Desktop\DependencyCheckGUI\Reports")
    if folder_selected:
        report_entry.delete(0, tk.END)
        report_entry.insert(0, os.path.normpath(folder_selected))


def toggle_fields():
    state = tk.DISABLED if update_only_var.get() else tk.NORMAL
    for widget in [project_entry, version_entry, app_path_entry, report_entry, app_browse_button, report_browse_button, view_logs_button]:
        widget.config(state=state)


def exit_gui():
    root.destroy()


def open_reports_directory():
    reports_dir = rf"{home_dir}\Desktop\DependencyCheckGUI\Reports"
    if os.path.exists(reports_dir):
        subprocess.Popen(f'explorer "{reports_dir}"')
    else:
        messagebox.showwarning("Directory Not Found",
                               "The default reports directory does not exist.")


def view_logs_file():
    logs_location = rf"{home_dir}\Desktop\DependencyCheckGUI\dependency_check_gui.log"
    if os.path.exists(logs_location):
        subprocess.Popen(f'explorer "{logs_location}"')
    else:
        messagebox.showwarning("File Not Found",
                               "The logs file does not exist.")


def main():
    global root, update_only_var, project_entry, version_entry, app_path_entry, report_entry, offline_var
    global api_key_entry, run_button, output_text, app_browse_button, report_browse_button, view_logs_button

    root = tk.Tk()
    root.title("Dependency-Check GUI")
    root.geometry("650x700")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    update_only_var = tk.BooleanVar()
    update_checkbox = tk.Checkbutton(
        main_frame, text="Update Only", variable=update_only_var, command=toggle_fields)
    update_checkbox.grid(row=0, column=0, columnspan=3, sticky=tk.W)

    offline_var = tk.BooleanVar()
    offline_checkbox = tk.Checkbutton(
        main_frame, text="Air-Gapped System", variable=offline_var)
    offline_checkbox.grid(row=0, column=1, columnspan=3, sticky=tk.W)

    # Project Name
    tk.Label(main_frame, text="Project Name: (Required)").grid(
        row=1, column=0, sticky=tk.W)
    project_entry = tk.Entry(main_frame, width=50)
    project_entry.grid(row=1, column=1, pady=5)

    # Application Version
    tk.Label(main_frame, text="Application Version (Required):").grid(
        row=2, column=0, sticky=tk.W)
    version_entry = tk.Entry(main_frame, width=50)
    version_entry.grid(row=2, column=1, pady=5)

    # Application Path
    tk.Label(main_frame, text="Path to Application (Required):").grid(
        row=3, column=0, sticky=tk.W)
    app_path_entry = tk.Entry(main_frame, width=50)
    app_path_entry.grid(row=3, column=1, pady=5)
    app_browse_button = tk.Button(
        main_frame, text="Browse", command=browse_app_path)
    app_browse_button.grid(row=3, column=2, padx=5)

    # Reports Directory
    tk.Label(main_frame, text="Reports Directory:").grid(
        row=4, column=0, sticky=tk.W)
    report_entry = tk.Entry(main_frame, width=50)
    report_entry.grid(row=4, column=1, pady=5)
    report_entry.insert(
        # Default value
        0, rf"{home_dir}\Desktop\DependencyCheckGUI\Reports")
    report_browse_button = tk.Button(
        main_frame, text="Browse", command=browse_report_dir)
    report_browse_button.grid(row=4, column=2, padx=5)

    # API Key
    tk.Label(main_frame, text="API Key (Leave blank to use default):").grid(
        row=5, column=0, sticky=tk.W)
    api_key_entry = tk.Entry(main_frame, width=50)
    api_key_entry.grid(row=5, column=1, pady=5)

    # Run, Open Reports, View Logs and Exit buttons
    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=6, column=0, columnspan=3, pady=10)

    run_button = tk.Button(
        button_frame, text="Run Dependency-Check", command=run_dependency_check)
    run_button.pack(side=tk.LEFT, padx=5)

    open_reports_button = tk.Button(
        button_frame, text="Open Reports", command=open_reports_directory)
    open_reports_button.pack(side=tk.LEFT, padx=5)

    view_logs_button = tk.Button(
        button_frame, text="View Logs", command=view_logs_file)
    view_logs_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_gui)
    exit_button.pack(side=tk.LEFT, padx=5)

    # Output field
    output_text = scrolledtext.ScrolledText(
        main_frame, width=70, height=30, state=tk.DISABLED)
    output_text.grid(row=7, column=0, columnspan=3, pady=10)

    toggle_fields()
    root.mainloop()


if __name__ == '__main__':
    main()
