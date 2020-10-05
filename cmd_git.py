import os
import git

#Pushしたいリポジトリに移動
os.chdir(r'/home/pi/Documents/Github/cocoa-getinfo')
repo = git.Repo()

#最新を取り込むため一旦Pull
#o = repo.remotes.origin
#o.pull()

#Commit(サブディレクトリ含めて全て)
repo.git.commit('.','-m','\"Commit Log\"')

#Push
origin = repo.remote(name='origin')
origin.push()
