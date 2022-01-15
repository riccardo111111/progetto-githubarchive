import random
from gharchive import GHArchive

git_message = []
commit_id = []
clone_url = []


def download_dati():
    messagi_totali = 0
    messagi_fix_pipe = 0
    print('Beginning file download')

    gh = GHArchive()
    data = gh.get('6/8/2020 15', '6/8/2020 16', filters=[('type', 'PushEvent')])
    for d in data:
        a = d.payload.commits
        for l in a:
            url_clone = ("git@github.com:" + d.repo.name + ".git")
            clone_url.append(url_clone)
            git_message.append(l.message)
            commit_id.append(l.sha)

    github = open("github", "w")

    for s in git_message:
        messagi_totali += 1
        # aggiungere più parole chiavi tipo secure bug
        if s.find("fix") != -1 and s.find("pipe") != -1 or s.find("secure") != -1 or s.find("bug") != -1:
            print(s)
            print("punto 1: ")
            print()
            print()
            print()
            messagi_fix_pipe += 1

            n = git_message.index(s)

            github.write(clone_url[n] + "\n")
            github.write(commit_id[n] + "\n")

    github.close()
    print("messagi_fix/messagi_totali:", messagi_fix_pipe, "/", messagi_totali, " ",
          (messagi_fix_pipe * 100) / messagi_totali, "%")
    return messagi_fix_pipe


def choose_commit(n=int):
    commit = open("id_url_commit", "w")
    f = open("github", "r")
    lines = f.readlines()

    print(n)
    for i in range(0, 10):
        x = random.randint(1, n)
        print(x)

        if (x % 2) == 0:
            commit.write(lines[x])
            commit.write(lines[x + 1])
        else:
            commit.write(lines[x - 1])
            commit.write(lines[x])
    f.close()
    commit.close()


if __name__ == '__main__':
    n=download_dati()
    choose_commit(n)
