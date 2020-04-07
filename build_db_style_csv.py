import collections
import csv
import re
import sys



def read_file(fn):
  with open(fn) as infile:
    return [x for x in csv.DictReader(infile)]

def write_file(fn, rows):
  with open(fn, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Country", "Date", "Count"])
    for row in rows:
      writer.writerow(row)

def classify_country_and_date(raw_data):
  out_dict = collections.OrderedDict()
  date_re = re.compile("(\d+)/(\d+)/(\d+)")
  for row in raw_data:
    country = row["Country/Region"]
    for name, val in row.items():
      m = date_re.match(name)
      if m:
        m, d, y = m.groups()
        primary_out_key = (country, "20%s/%s/%s" % (y, m, d))
        old_count = out_dict.get(primary_out_key, 0)
        out_dict[primary_out_key] = old_count + int(val)
  return out_dict

def classified_to_rows(country_and_date_to_count):
  out = []
  for country_and_date, count in sorted(country_and_date_to_count.items()):
    country, date = country_and_date
    out.append((country, date, count))
  return out

def main(args):
  in_fn = args[1]
  out_fn = args[2]
  rows = read_file(in_fn)
  country_and_date_to_count = classify_country_and_date(rows)
  output_rows = classified_to_rows(country_and_date_to_count)
  write_file(out_fn, output_rows)

if __name__ == "__main__":
  main(sys.argv)
