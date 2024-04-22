def seek_line_tail(fp,last_bytes):
  file_size = fp.seek(0,2)
  offset = file_size - last_bytes
  if offset <= 0:
    fp.seek(0)
  else:
    fp.seek(offset)
    fp.readline() # go to the beginning of the next line
  return fp.tell()
