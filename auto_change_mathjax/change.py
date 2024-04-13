# Python
import glob
import argparse

inline_symbol = {
  "start_symbol": '{% mathjax %}',
  "end_symbol": '{% endmathjax %}'
}

block_symbol = {
  "start_symbol": '<div align=center>{% mathjax %}',
  "end_symbol": '{% endmathjax %}</div>'
}

def get_all_indices(text, substring):
  indices = []
  index = -1

  while True:
    index = text.find(substring, index + 1)
    if index == -1:
      break
    indices.append(index)

  return indices


def render_formula(content, indices, origin_symbol='$', start_symbol='$', end_symbol='$'):

  if len(indices) == 0:
    return content

  new_content = ''
  last_idx = 0
  for i, idx in enumerate(indices):
    if i%2 == 0:
      new_content += content[last_idx:idx] + start_symbol
    else:
      new_content += content[last_idx:idx] + end_symbol
    
    last_idx = idx + len(origin_symbol)
  
  new_content += content[last_idx:]

  return new_content


def preprocess(file_path):
  with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
      
  indices = get_all_indices(content, '$$')
  assert (len(indices) % 2 == 0)
  new_content = render_formula(content, indices, origin_symbol='$$', **block_symbol)

  lines = new_content.split('\n')
  new_lines = []
  for line in lines:
    indices = get_all_indices(line, '$')
    if len(indices) == 1:
      new_lines.append(line)
    else:
      assert (len(indices) % 2 == 0)
      new_lines.append(render_formula(line, indices, origin_symbol='$', **inline_symbol))

  with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(list(map(lambda x:x+'\n', new_lines[:-1])) + [new_lines[-1]])


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file', dest='file', type=str)
  parser.add_argument('-d', '--dir', dest='dir', type=str)

  args = parser.parse_args()

  if args.dir:
    markdown_files = glob.glob(f"{args.dir}/*.md")
    for file_path in markdown_files:
      print(f'processing {file_path}')
      preprocess(file_path)
  elif args.file:
    print(f'processing {args.file}')
    preprocess(args.file)
  else:
    print("Please specify a .md file or a directory containing .md files")