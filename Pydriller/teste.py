from pydriller import Repository

for commit in Repository('https://github.com/Wolfterro/Projetos-em-C').traverse_commits():
    print(f'{commit.author.name}: {commit.author.email}')
    print(commit.modified_files)
    print(commit.author_date)
