import os

def generate_latex_for_files(folder_path, Channel, plotFolder):
    folder_path = os.path.join(folder_path, plotFolder)
    for filename in sorted(os.listdir(folder_path)): # List all files in the directory and sort them alphabetically
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)) or filename.startswith("Ignore"):
            continue # Skip the plots that start with "ignore"

        if filename.lower().endswith('.pdf'):
            # Extract filename without extension
            base_filename = os.path.splitext(filename)[0]

            # Check if base_filename starts with two numbers followed by an underscore
            if base_filename[:2].isdigit() and base_filename[2] == '_':
                modified_base_filename = base_filename[3:]
            else:
                modified_base_filename = base_filename

            # Generate LaTeX code for each file
            latex_code = (
                "\\begin{figure}[h]\n"
                "\\centering\n"
                "\\begin{subfigure}{.45\\textwidth}\n"
                "  \\centering\n"
                "  \\includegraphics[width=.95\\linewidth]{Chapter5_tHq/BDT_Results/" + plotFolder + "/" + base_filename + "}\n"
                "  %\\caption{}\n"
                "\\end{subfigure}%\n"
                "\\begin{subfigure}{.55\\textwidth}\n"
                "  \\centering\n"
                "  \\includegraphics[width=.95\\linewidth]{Chapter5_tHq/BDT_Results/" + plotFolder + "/Separation/" + base_filename + "}\n"
                "  %\\caption{}\n"
                "\\end{subfigure}\n"
                "\\caption{Distribution and separation plot for }\n"
                "\\label{fig:Appendix:BDTVARS:" + Channel + ":" + modified_base_filename + "}\n"
                "\\end{figure}\n"
            )
            
            print(latex_code)

# Change this
Channel = "tHqSS"

if Channel == "ttbarOS":
    plotFolder = "BDT_Variables_ttbar_OS"
elif Channel == "tHqOS":
    plotFolder = "BDT_Variables_tHq_OS"
elif Channel == "tHqSS":
    plotFolder = "BDT_Variables_tHq_SS"


generate_latex_for_files('/Users/pablo/Desktop/tHq_Analysis/8-Thesis/Thesis/Figures/Chapter5_tHq/BDT_Results/', Channel, plotFolder)
