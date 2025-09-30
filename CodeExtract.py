import pathlib

def scan_and_collate_to_separate_files():
    """
    Scans 'Usermode' and 'Bootkit' subdirectories for C/C++ source/header files
    and collates their content into separate output files ('usermode.txt' and 'efi.txt')
    in the parent directory of the script. Now recursively searches all subdirectories.
    Excludes blacklisted folders from extraction.
    """
    
    # Define blacklist of folder names to skip during scanning
    folder_blacklist = {"node_modules"}
    
    def is_path_allowed(path):
        """Check if any part of the path is in the blacklist"""
        return not any(part in folder_blacklist for part in path.parts)

    try:
        # Get the directory where the script is located and resolve to an absolute path
        script_file_path = pathlib.Path(__file__).resolve()
        script_dir = script_file_path.parent
    except NameError:
        # Fallback for environments where __file__ might not be defined
        script_dir = pathlib.Path.cwd().resolve()
        print(f"Info: __file__ not defined. Using current working directory as script directory: {script_dir}")

    # Define mapping from source folder names (expected in script's directory)
    # to their desired output filenames (will be placed in script_dir.parent)
    source_to_output_map = {
        "todolist.client": "todolist.client.txt",
        "ToDoList.Server": "ToDoList.Server.txt"
    }

    # Define target file extensions (case-insensitive matching for suffix)
    target_extensions = {".cs", ".ts", ".js", ".json", ".css"}

    print(f"Python script directory: {script_dir}")
    print(f"Target source folders (relative to script dir): {', '.join(source_to_output_map.keys())}")
    print(f"Target file extensions: {', '.join(target_extensions)}")
    print(f"Blacklisted folders: {', '.join(folder_blacklist)}")

    try:
        output_parent_dir = script_dir.parent
        # Check if the script is in the root directory, as its parent would be itself.
        if script_dir == output_parent_dir:
            print(f"Error: Script is located in the root directory ({script_dir}). "
                  "Cannot create output files in a parent directory that is also the root.")
            return
    except Exception as e: # Should generally not fail for pathlib.Path.parent
        print(f"Error: Could not determine output parent directory from script_dir {script_dir}. Error: {e}")
        return

    print(f"Output files will be created in: {output_parent_dir}")

    all_tasks_summary = [] # To store a summary of what happened for each task

    for source_folder_name, output_filename in source_to_output_map.items():
        current_source_folder_path = script_dir / source_folder_name
        current_output_file_path = output_parent_dir / output_filename

        print(f"\nProcessing source folder: '{source_folder_name}' for output file: '{current_output_file_path}'")

        # Check if the source folder itself is blacklisted
        if any(part in folder_blacklist for part in current_source_folder_path.parts):
            message = f" Info: Source folder '{current_source_folder_path}' is blacklisted. Skipping."
            print(message)
            all_tasks_summary.append(f"'{source_folder_name}' -> '{output_filename}': Skipped (blacklisted folder).")
            continue

        if not current_source_folder_path.exists():
            message = (f" Info: Source folder '{current_source_folder_path}' does not exist. "
                      f"Output file '{current_output_file_path}' will not be created/modified.")
            print(message)
            all_tasks_summary.append(f"'{source_folder_name}' -> '{output_filename}': Source folder not found.")
            continue

        if not current_source_folder_path.is_dir():
            message = (f" Info: Source '{current_source_folder_path}' is not a directory. "
                      f"Output file '{current_output_file_path}' will not be created/modified.")
            print(message)
            all_tasks_summary.append(f"'{source_folder_name}' -> '{output_filename}': Source path is not a directory.")
            continue

        # Use rglob to recursively find all relevant files in folder and all subfolders
        # Apply blacklist filtering to exclude files in blacklisted directories
        relevant_files_in_folder = sorted([
            item_path for item_path in current_source_folder_path.rglob('*')
            if item_path.is_file() and 
               item_path.suffix.lower() in target_extensions and 
               is_path_allowed(item_path)
        ])

        try:
            # Open the output file (creates if not exists, truncates if exists)
            with open(current_output_file_path, "w", encoding="utf-8") as outfile:
                if not relevant_files_in_folder:
                    print(f" Info: No files with specified extensions found in '{source_folder_name}' or its subdirectories (excluding blacklisted folders).")
                    print(f" Output file '{current_output_file_path}' has been created and is empty.")
                    all_tasks_summary.append(
                        f"'{source_folder_name}' -> '{output_filename}': Created empty (no relevant source files)."
                    )
                else:
                    file_count = len(relevant_files_in_folder)
                    print(f" Found {file_count} relevant file(s) recursively (excluding blacklisted folders). Writing to '{current_output_file_path}'.")
                    
                    for item_path in relevant_files_in_folder:
                        # Show relative path from the source folder for better context
                        relative_path = item_path.relative_to(current_source_folder_path)
                        print(f" Adding file: {relative_path}")
                        outfile.write(f"//{relative_path}\n")
                        
                        try:
                            content = item_path.read_text(encoding="utf-8")
                            outfile.write(content)
                            # Ensure a newline after the content to separate from the next file's header or EOF
                            outfile.write("\n")
                        except Exception as e:
                            print(f" Error reading file '{relative_path}': {e}")
                            outfile.write(f"// Error: Could not read content of file: {relative_path}\n\n")

                    all_tasks_summary.append(
                        f"'{source_folder_name}' -> '{output_filename}': {file_count} file(s) collated recursively (blacklisted folders excluded)."
                    )

            # This message applies if the 'with open' block executed successfully.
            print(f" ✅ Successfully processed '{source_folder_name}' recursively. Output is at '{current_output_file_path}'")

        except IOError as e:
            message = (f" ❌ Error: Could not write to output file '{current_output_file_path}'. "
                      f"Check permissions or path. Details: {e}")
            print(message)
            all_tasks_summary.append(f"'{source_folder_name}' -> '{output_filename}': Failed (IOError writing output).")

        except Exception as e:
            message = f" ❌ An unexpected error occurred while processing '{source_folder_name}': {e}"
            print(message)
            all_tasks_summary.append(f"'{source_folder_name}' -> '{output_filename}': Failed (Unexpected error).")

    print("\n--- Processing Summary ---")
    if not all_tasks_summary:
        print("No tasks were defined or processed.")
    else:
        for summary_item in all_tasks_summary:
            print(summary_item)
    
    print("-------------------------")
    print("Script execution finished.")

if __name__ == "__main__":
    scan_and_collate_to_separate_files()
