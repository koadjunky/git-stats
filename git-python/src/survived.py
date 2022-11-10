import logging
from git import Repo

def xrange2bnd(xrng):
  start = stop = next(iter(xrng))
  for i in xrng:
    stop = i
  return start, (stop - start + 1)

class BlameFile:
  def __init__(self, fname):
    self.filename = fname
    self.total = 0
    self.authors = {}

  def add_author(self, author, lines):
    if not author in self.authors:
      self.authors[author] = 0
    self.authors[author] += lines

  def add_blame(self, entry):
    author = entry.commit.author.email
    _, count = xrange2bnd(entry.linenos)
    self.add_author(author, count)
    self.total += count


def main(repo_path):
  # Should be -CCC but it is impossible in current GitPython
  repo = Repo(repo_path)
  for entry in repo.commit().tree.traverse():
    fname = entry.path
    if entry.type == 'blob':
      bfile = BlameFile(fname)
      for entry in repo.blame_incremental(None, fname, M=True, C=True, w=True):
        bfile.add_blame(entry)
      for author in bfile.authors.keys():
        print(fname, author, bfile.authors[author], bfile.authors[author] * 100.0 / bfile.total)



if __name__ == '__main__':
  import sys
  logging.basicConfig(level=logging.INFO)
  main(sys.argv[1])
