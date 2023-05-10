from pydriller import Repository
import pandas as pd

dataframe = []

for commit in Repository('https://github.com/Wolfterro/Projetos-em-C').traverse_commits():
    #Author
    print(f'Author Name: {commit.author.name}: {commit.author.email}')
    print(f'Date(Author): {commit.author_date}')
    #Commiter
    print(f'Commiter Name: {commit.committer.name}: {commit.committer.email}')
    print(f'Date(Commiter): {commit.committer_date}')
    #Data of Commit
    print(f'Hash: {commit.hash}')
    for branch in commit.branches:
        print(f'Branch: {branch}')
        print(f'Is it in main branch? {commit.in_main_branch}')
    print(f'Is it a merge commit? {commit.merge}')
    print(f'Project Name: {commit.project_name}')
    print(f'Local Path: {commit.project_path}')
    print(f'Commit Message: {commit.msg}')
    print(f'Number of Files: {commit.files}')
    print(f'Total of modified Lines: {commit.lines}')
    #DMM
    print(f'DMM size: {commit.dmm_unit_size}')
    print(f'DMM complexity: {commit.dmm_unit_complexity}')
    print(f'DMM Interfacing: {commit.dmm_unit_interfacing}')

    #Info per Commit
    for file in commit.modified_files:
        print(f'File Name: {file.filename}')
        print(f'Change Type: {file.change_type}')
        #PATH
        if file.new_path != file.old_path:
            print(f'Old PATH: {file.old_path}')
            print(f'New PATH: {file.new_path}')
        else:
            print(f'File PATH: {file.new_path}')
        '''#Source Code
        print(f'Source Code Before: {file.source_code_before}')
        print(f'Source Code: {file.source_code}')'''
        #Complexity
        print(f'Complexity: {file.complexity}')
        #Methods
        print(f'Methods: {len(file.methods)}')
        if len(file.methods) != 0:
            print('Methods Before:')
            for method in file.methods_before:
                print(method)
            print('Changed Method: ')
            for method in file.changed_methods:
                print(method)
        '''#Diff
        print(f'Diff: {file.diff}')
        print(f'Diff Parsed: {file.diff_parsed}')'''
        #Tokens
        print(f'Tokens: {file.token_count}')
        #Lines
        print(f'Lines Of Code(nloc): {file.nloc}')
        print(f'Lines added: {file.added_lines}')
        print(f'Lines deleted: {file.deleted_lines}')
        print(f'Lines modified per File: {file.added_lines + file.deleted_lines}')
        print(f'Lines Balance: {file.added_lines - file.deleted_lines}')



for commit in Repository('https://github.com/Wolfterro/Projetos-em-C').traverse_commits():

    for branch in commit.branches:
        for file in commit.modified_files:
            summary = pd.DataFrame({
                'Hash': [commit.hash],
                'Project Name': [commit.project_name],
                'Local Commit PATH': [commit.project_path],
                'Message': [commit.msg],
                'Branch': [branch],
                'Main Branch': [commit.in_main_branch],
                #'DMM size': [commit.dmm_unit_size],
                #'DMM complexity': [commit.dmm_unit_complexity],
                #'DMM Interfacing': [commit.dmm_unit_interfacing],
                'Number of Files': [commit.files],
                'Modified Lines': [commit.lines],
                'File Name': [file.filename],
                'Change Type': [file.change_type],
                'Local File PATH Old': [file.old_path],
                'Local File PATH New': [file.new_path],
                'Author Name': [commit.author.name],
                'Author Email': [commit.author.email],
                'Author Commit Date': [commit.author_date],
                'Committer Name': [commit.committer.name],
                'Committer Email': [commit.committer.email],
                'Committer Commit Date': [commit.committer_date],
                'Merge Commit': [commit.merge],
                'Complexity': [file.complexity],
                'Methods': [len(file.methods)],
                #if len(file.methods) != 0:
                #    print('Methods Before:')
                #    for method in file.methods_before:
                #        print(method)
                #    print('Changed Method: ')
                #    for method in file.changed_methods:
                #        print(method)
                'Tokens': [file.token_count],
                'Lines Of Code(nloc)': [file.nloc],
                'Lines Added': [file.added_lines],
                'Lines Deleted': [file.deleted_lines],
                'Lines Modified per File': [file.added_lines + file.deleted_lines],
                'Lines Balance': [file.added_lines - file.deleted_lines]
            })
            dataframe.append(summary)
            summary = pd.DataFrame()

summary_df = pd.concat(dataframe, ignore_index=True)

summary_df.to_csv('Python\Drill\\summary.csv')
